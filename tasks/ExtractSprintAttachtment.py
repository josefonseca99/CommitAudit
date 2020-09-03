import base64
import urllib

from util import ConstantManagement
from model import SprintData
import json


class ExtractSprintAttachment:
    def __init__(self, cell_name=None, sprint_number=None,project_name="b267af7c-3233-4ad1-97b3-91083943100d",
                 organization="grupobancolombia"):

        self.cell_name = cell_name
        self.sprint_number = sprint_number
        self.project_name = project_name.replace(" ", "%20")
        self.organization = organization
        self.sprint_data = SprintData.SprintData()
        self.access_token = ConstantManagement.CREDENTIALS
        self.headers = {}
        self.commit_dict = {}
        self.headers['Content-type'] = "application/json"
        self.headers['Authorization'] = b'Basic ' + base64.b64encode(self.access_token.encode('utf-8'))
        self.items_request = (ConstantManagement.US_ATTACHMENT_REQUEST_1
                              ).format(self.organization,
                                       self.project_name,
                                       self.cell_name)

        self.request = urllib.request.Request(self.items_request, headers=self.headers)

        try:
            self.opener = urllib.request.build_opener()
            self.response = json.load(self.opener.open(self.request))
            for x in self.response["value"]:
                if x["name"] == ConstantManagement.US_NUMBER_STR.format(self.sprint_number):
                    self.sprint_data.sprint_id = x["id"]
                    self.sprint_data.start_date = x["attributes"]["startDate"].split("T")[0]
                    self.sprint_data.finish_date = x["attributes"]["finishDate"].split("T")[0]
                else:
                    pass

        except:
            pass

    def get_sprint_data(self):
        return self.sprint_data

    def get_total_commits(self):
        return self.response["count"]
