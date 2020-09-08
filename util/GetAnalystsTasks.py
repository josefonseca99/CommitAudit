from tasks import ExtractSprintAttachtment, ExtractCommitAttachment, ExtractPullRequestAttachment, ExtractUSData, \
    ExtractUSIDS, ExtractCodeSmells, ExtractTechnicalDebt
from util import GetExcelAnalysts


def analyst_in_dict_list(analysts_list, analyst_email):
    return next((i for i, item in enumerate(analysts_list) if item["analyst_email"] == analyst_email), None)


class GetAnalystsTasks:
    def __init__(self, sprint_number):

        self.sprint_number = sprint_number
        self.analysts_list = GetExcelAnalysts.GetExcelAnalysts().analysts_dict()
        self.data_collection = []
        self.commit_attch = {}

    def collect_data(self):
        for x in self.analysts_list:
            cell_value = x["cell"].replace(" ", "%20") if " " in x["cell"] else x["cell"]
            self.analysts_data = {'analyst_name': x['name']}
            self.sprint_attch = ExtractSprintAttachtment.ExtractSprintAttachment(cell_value,
                                                                                 self.sprint_number).get_sprint_data()

            self.us_identf = ExtractUSIDS.ExtractUSIDS(cell_value, self.sprint_attch.sprint_id).get_uids_list()
            identf_list = list(map(str, self.us_identf))
            self.us_data = ExtractUSData.ExtractUSData(identf_list, x["email"]).get_analyst_data()
            self.analysts_data.update(self.us_data)
            self.pullattch = ExtractPullRequestAttachment.ExtractPullRequestAttachment(
                x["repository"],
                x["email"],
                self.sprint_attch.start_date,
                self.sprint_attch.finish_date).pull_requests_number()
            self.analysts_data["pull_data"] = self.pullattch
            self.commit_attch = ExtractCommitAttachment.ExtractCommitAttachment(self.sprint_attch.start_date,
                                                                                self.sprint_attch.finish_date,
                                                                                x["email"],
                                                                                x["repository"]).get_commit_number()
            self.analysts_data["commit_data"] = self.commit_attch

            self.technical_debt = ExtractTechnicalDebt.ExtractTechnicalDebt(x["repository"]).get_technical_debt_time()
            self.analysts_data["technical_debt"] = self.technical_debt

            self.code_smells = ExtractCodeSmells.ExtractCodeSmells(x["repository"]).get_code_smells_time()
            self.analysts_data["code_smells"] = self.code_smells

            if self.sprint_attch.sprint_id is not None and self.sprint_attch.start_date is not None:
                analyst_index = analyst_in_dict_list(self.data_collection, x["email"])
                if analyst_index is not None:

                    if isinstance(self.data_collection[analyst_index]['pull_data'], int):
                        self.data_collection[analyst_index]['pull_data'] += self.analysts_data['pull_data']
                        self.data_collection[analyst_index]['commit_data'] += self.analysts_data['commit_data']
                    else:
                        if isinstance(self.analysts_data["pull_data"], int):
                            self.data_collection[analyst_index]['pull_data'] = self.analysts_data['pull_data']
                            self.data_collection[analyst_index]['commit_data'] = self.analysts_data['commit_data']

                    if isinstance(self.data_collection[analyst_index]['technical_debt'], int):
                        self.data_collection[analyst_index]['technical_debt'] += self.analysts_data['technical_debt']
                    else:
                        if isinstance(self.data_collection[analyst_index]['technical_debt'], int):
                            self.data_collection[analyst_index]['technical_debt'] = self.analysts_data[
                                'technical_debt']

                    if isinstance(self.data_collection[analyst_index]['code_smells'], int):
                        self.data_collection[analyst_index]['code_smells'] += self.analysts_data['code_smells']
                    else:
                        if isinstance(self.data_collection[analyst_index]['code_smells'], int):
                            self.data_collection[analyst_index]['code_smells'] = self.analysts_data[
                                'code_smells']

                else:
                    self.data_collection.append(self.analysts_data)

    def get_data_collection(self):
        return self.data_collection
