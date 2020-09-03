from util import CreateExcel, GetExcelAnalysts
from tasks import ExtractUSData, ExtractSprintAttachtment, ExtractUSIDS, ExtractPullRequestAttachment, \
    ExtractCommitAttachment

sprint_number = 96
analysts_list = GetExcelAnalysts.GetExcelAnalysts().analysts_dict()
data_collection = []


def analyst_in_dict_list(analysts_copy_list, analyst_email):
    return next((i for i, item in enumerate(analysts_copy_list) if item["analyst_email"] == analyst_email), None)


for x in analysts_list:
    print(x)
    cell_value = x["cell"].replace(" ", "%20") if " " in x["cell"] else x["cell"]
    sprint_attch = ExtractSprintAttachtment.ExtractSprintAttachment(cell_value,
                                                                    sprint_number).get_sprint_data()
    print(sprint_attch.sprint_id)

    us_identf = ExtractUSIDS.ExtractUSIDS(cell_value, sprint_attch.sprint_id).get_uids_list()
    print(us_identf)
    identf_list = list(map(str, us_identf))
    us_data = ExtractUSData.ExtractUSData(identf_list, x["email"]).get_analyst_data()
    print(us_data)
    pullattch = ExtractPullRequestAttachment.ExtractPullRequestAttachment(x["repository"].replace(" ", "%20"),
                                                                          x["email"],
                                                                          sprint_attch.start_date,
                                                                          sprint_attch.finish_date).pull_requests_number()
    print(pullattch)
    us_data["pull_data"] = pullattch
    commit_attch = ExtractCommitAttachment.ExtractCommitAttachment(sprint_attch.start_date,
                                                                   sprint_attch.finish_date,
                                                                   x["email"], x["repository"].replace(" ",
                                                                                                       "%20")).get_commit_number()
    print(commit_attch)
    us_data["commit_data"] = commit_attch

    if sprint_attch.sprint_id is not None and sprint_attch.start_date is not None:
        analyst_index = analyst_in_dict_list(data_collection, x["email"])
        if analyst_index is not None:
            data_collection[analyst_index]['pull_data'] += us_data['pull_data']
            data_collection[analyst_index]['commit_data'] += us_data['commit_data']

        else:
            data_collection.append(us_data)
print(data_collection)



