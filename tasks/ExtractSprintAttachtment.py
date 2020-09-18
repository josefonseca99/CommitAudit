import base64
import urllib
import re

from util import ConstantManagement
from config_files import APIConfiguration
from model import SprintData
import json


def find_sprint_coincidence(sprint_query_value, input_sprint):
    x = re.findall(ConstantManagement.US_NUMBER_STR.format(input_sprint),sprint_query_value)
    return bool(x)


class ExtractSprintAttachment:
    def __init__(self, cell_name=None, sprint_number=None):

        self.cell_name = cell_name
        self.sprint_number = sprint_number
        self.azure_dev_link = APIConfiguration.AZURE_DEV_LINK
        self.project_name = APIConfiguration.PROJECT.replace(" ", "%20")
        self.organization = APIConfiguration.ORGANIZATION
        self.sprint_data = SprintData.SprintData()
        self.access_token = ConstantManagement.CREDENTIALS
        self.headers = {}
        self.commit_dict = {}
        self.headers['Content-type'] = "application/json"
        self.headers['Authorization'] = b'Basic ' + base64.b64encode(self.access_token.encode('utf-8'))
        self.items_request = (ConstantManagement.US_ATTACHMENT_REQUEST_1
                              ).format(self.azure_dev_link,
                                       self.organization,
                                       self.project_name,
                                       self.cell_name)

        try:
            self.request = urllib.request.Request(self.items_request, headers=self.headers)
            self.opener = urllib.request.build_opener()
            self.response = json.load(self.opener.open(self.request))
            for x in self.response["value"]:
                if find_sprint_coincidence(x["name"], self.sprint_number):
                    self.sprint_data.sprint_id = x["id"]
                    self.sprint_data.start_date = x["attributes"]["startDate"].split("T")[0]
                    self.sprint_data.finish_date = x["attributes"]["finishDate"].split("T")[0]
                    break
                else:
                    pass

        except:
            pass

    def get_sprint_data(self):
        return self.sprint_data

    def get_total_commits(self):
        return self.response["count"]
