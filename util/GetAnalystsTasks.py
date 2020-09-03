from tasks import ExtractSprintAttachtment, ExtractCommitAttachment, ExtractPullRequestAttachment, ExtractUSData, \
    ExtractUSIDS
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
            self.sprint_attch = ExtractSprintAttachtment.ExtractSprintAttachment(cell_value,
                                                                                 self.sprint_number).get_sprint_data()

            self.us_identf = ExtractUSIDS.ExtractUSIDS(cell_value, self.sprint_attch.sprint_id).get_uids_list()
            identf_list = list(map(str, self.us_identf))
            self.us_data = ExtractUSData.ExtractUSData(identf_list, x["email"]).get_analyst_data()
            self.pullattch = ExtractPullRequestAttachment.ExtractPullRequestAttachment(
                x["repository"].replace(" ", "%20"),
                x["email"],
                self.sprint_attch.start_date,
                self.sprint_attch.finish_date).pull_requests_number()
            self.us_data["pull_data"] = self.pullattch
            self.commit_attch = ExtractCommitAttachment.ExtractCommitAttachment(self.sprint_attch.start_date,
                                                                                self.sprint_attch.finish_date,
                                                                                x["email"], x["repository"].replace(" ",
                                                                                                                    "%20")).get_commit_number()
            self.us_data["commit_data"] = self.commit_attch

            if self.sprint_attch.sprint_id is not None and self.sprint_attch.start_date is not None:
                analyst_index = analyst_in_dict_list(self.data_collection, x["email"])
                if analyst_index is not None:
                    self.data_collection[analyst_index]['pull_data'] += self.us_data['pull_data']
                    self.data_collection[analyst_index]['commit_data'] += self.us_data['commit_data']

                else:
                    self.data_collection.append(self.us_data)

    def get_data_collection(self):
        return self.data_collection
