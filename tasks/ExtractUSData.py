import base64
import urllib.request

from util import ConstantManagement
import json


class ExtractUSData:
    def __init__(self, us_id_list=None, analyst_email=None, project_name="b267af7c-3233-4ad1-97b3-91083943100d",
                 organization="grupobancolombia"):

        self.project_name = project_name
        self.organization = organization
        self.analyst_email = analyst_email
        self.separator = ","
        self.us_id_list_string = self.separator.join(us_id_list)
        self.access_token = ConstantManagement.CREDENTIALS
        self.headers = {}
        self.commit_dict = {}
        self.headers['Content-type'] = "application/json"
        self.headers['Authorization'] = b'Basic ' + base64.b64encode(self.access_token.encode('utf-8'))
        self.items_request = (ConstantManagement.US_ID_ATTACHMENT_REQUEST
                              ).format(self.organization,
                                       self.project_name,
                                       self.us_id_list_string)

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
            "no_scored": []
        }
        if us_id_list != [] and analyst_email is not None:
            try:
                self.request = urllib.request.Request(self.items_request, headers=self.headers)
                self.opener = urllib.request.build_opener()
                self.response = json.load(self.opener.open(self.request))
                for value in self.response["value"]:

                    if value["fields"]["System.AssignedTo"]["uniqueName"] == self.analyst_email:

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
                            self.user_dict["no_scored"].append(value["id"])

            except:
                pass

    def get_analyst_data(self):
        return self.user_dict
