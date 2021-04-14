import base64
import urllib.request
from util import ConstantManagement
from config_files import APIConfiguration
import json


class ExtractUSData:
    def __init__(self, us_id_list=None, analyst_email=None, cell_name=None, repository=None):

        self.azure_dev_link = APIConfiguration.AZURE_DEV_LINK
        self.project_name = APIConfiguration.PROJECT
        self.organization = APIConfiguration.ORGANIZATION
        self.analyst_email = analyst_email
        self.cell_name = cell_name
        self.repository = repository
        self.separator = ","
        self.us_id_list_string = self.separator.join(us_id_list)
        self.access_token = APIConfiguration.BANCOLOMBIA_API_TOKEN
        self.headers = {}
        self.commit_dict = {}
        self.headers['Content-type'] = "application/json"
        self.headers['Authorization'] = b'Basic ' + base64.b64encode(self.access_token.encode('utf-8'))
        self.items_request = (ConstantManagement.US_ID_ATTACHMENT_REQUEST
                              ).format(self.azure_dev_link,
                                       self.organization,
                                       self.project_name,
                                       self.us_id_list_string)

        print("La url de : " + self.analyst_email + "es:")
        print(self.items_request)

        self.user_dict = {
            "analyst_email": self.analyst_email,
            "enabler_type": 0,
            "user_story_type": 0,
            "bug_type": 0,
            "new_state": 0,
            "active_state": 0,
            "closed_state": 0,
            "impediment_state": 0,
            "engaged_to": 0,
            "no_scored": 0
        }
        if us_id_list != [] and analyst_email is not None:
            try:
                self.request = urllib.request.Request(self.items_request, headers=self.headers)
                self.opener = urllib.request.build_opener()
                self.response = json.load(self.opener.open(self.request))

                value_field = self.response["value"]

                for value in value_field:

                    if "System.AreaPath" in value["fields"].keys() and "System.Tags" in value["fields"].keys():
                        if self.repository in value["fields"]["System.Tags"] and self.cell_name in value["fields"][
                            "System.AreaPath"]:
                            print("se encontro un true")

                            if value["fields"]["System.WorkItemType"] == "Bug":
                                self.user_dict["bug_type"] += 1

                            if value["fields"]["System.State"] == "New":
                                self.user_dict["new_state"] += 1

                            if value["fields"]["System.State"] == "Active":
                                self.user_dict["active_state"] += 1

                            if value["fields"]["System.State"] == "Closed":
                                self.user_dict["closed_state"] += 1

                            if value["fields"]["System.State"] == "Impedimento":
                                self.user_dict["impediment_state"] += 1

                    if "Microsoft.VSTS.Common.ActivatedBy" in value["fields"].keys():
                        if value["fields"]["Microsoft.VSTS.Common.ActivatedBy"][
                            "uniqueName"].lower() == self.analyst_email.lower():
                            if value["fields"]["System.WorkItemType"] == "Habilitador":
                                self.user_dict["enabler_type"] += 1

                            if value["fields"]["System.WorkItemType"] == "User Story":
                                self.user_dict["user_story_type"] += 1

                            if value["fields"]["System.WorkItemType"] == "Bug":
                                self.user_dict["bug_type"] += 1

                            if value["fields"]["System.State"] == "New":
                                self.user_dict["new_state"] += 1

                            if value["fields"]["System.State"] == "Active":
                                self.user_dict["active_state"] += 1

                            if value["fields"]["System.State"] == "Closed":
                                self.user_dict["closed_state"] += 1

                            if value["fields"]["System.State"] == "Impedimento":
                                self.user_dict["impediment_state"] += 1

                            if "Microsoft.VSTS.Scheduling.StoryPoints" in value["fields"].keys():
                                self.user_dict["engaged_to"] += value["fields"]["Microsoft.VSTS.Scheduling.StoryPoints"]

                            if "Microsoft.VSTS.Scheduling.StoryPoints" not in value["fields"].keys():
                                self.user_dict["no_scored"] += 1

                    if "System.AssignedTo" in value["fields"].keys():
                        if value["fields"]["System.AssignedTo"]["uniqueName"].lower() == self.analyst_email.lower():

                            if value["fields"]["System.WorkItemType"] == "Habilitador":
                                self.user_dict["enabler_type"] += 1

                            if value["fields"]["System.WorkItemType"] == "User Story":
                                self.user_dict["user_story_type"] += 1

                            if value["fields"]["System.WorkItemType"] == "Bug":
                                self.user_dict["bug_type"] += 1

                            if value["fields"]["System.State"] == "New":
                                self.user_dict["new_state"] += 1

                            if value["fields"]["System.State"] == "Active":
                                self.user_dict["active_state"] += 1

                            if value["fields"]["System.State"] == "Closed":
                                self.user_dict["closed_state"] += 1

                            if value["fields"]["System.State"] == "Impedimento":
                                self.user_dict["impediment_state"] += 1

                            if "Microsoft.VSTS.Scheduling.StoryPoints" in value["fields"].keys():
                                self.user_dict["engaged_to"] += value["fields"]["Microsoft.VSTS.Scheduling.StoryPoints"]

                            if "Microsoft.VSTS.Scheduling.StoryPoints" not in value["fields"].keys():
                                self.user_dict["no_scored"] += 1


            except Exception as e:
                print(e)
                pass

    def get_analyst_data(self):
        return self.user_dict