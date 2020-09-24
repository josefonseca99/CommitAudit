from database_tasks import AnalystsDBTasks, InformationDBTasks, SprintDBTasks


def save_audit_data(analyst_data_list, sprint_id, date):
    sprint_description = "Sprint %s"
    sprint_information = (sprint_id, sprint_description % sprint_id, date)
    SprintDBTasks.insert_sprint(sprint_information)

    data_list_with_db_ids = AnalystsDBTasks.get_analysts_ids(analyst_data_list)

    InformationDBTasks.insert_information(data_list_with_db_ids, sprint_id)






