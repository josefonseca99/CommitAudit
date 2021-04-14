import base64
import urllib.request
from config_files import APIConfiguration
from util import ConstantManagement
from config_files import APIConfiguration
from datetime import date, datetime
import json


class ExtractPullRequestAttachment:
    def __init__(self, repo_name=None, analyst_email=None, start_date=None, finish_date=None):

        self.azure_dev_link = APIConfiguration.AZURE_DEV_LINK
        self.project_name = APIConfiguration.PROJECT
        self.organization = APIConfiguration.ORGANIZATION
        self.analyst_email = analyst_email
        self.analyst_counter = 0
        self.date_format = "%Y-%m-%d"

        if start_date is not None and finish_date is not None:
            if repo_name is not None and repo_name != '':
                self.repo_name = repo_name.replace(" ", "%20")
                self.start_date = datetime.strptime(start_date, self.date_format)
                self.finish_date = datetime.strptime(finish_date, self.date_format)
                self.closed_date = ""
                self.access_token = APIConfiguration.BANCOLOMBIA_API_TOKEN
                self.headers = {}
                self.commit_dict = {}
                self.headers['Content-type'] = "application/json"
                self.headers['Authorization'] = b'Basic ' + base64.b64encode(self.access_token.encode('utf-8'))
                self.items_request = (ConstantManagement.COMMIT_STATUS_ATTACHMENT_REQUEST_1
                                      ).format(self.azure_dev_link,
                                               self.organization,
                                               self.project_name,
                                               self.repo_name)
                print(self.items_request)
                self.request = urllib.request.Request(self.items_request, headers=self.headers)

                try:
                    self.opener = urllib.request.build_opener()
                    self.response = json.load(self.opener.open(self.request))
                    for x in self.response["value"]:
                        closed_date = datetime.strptime(x["closedDate"].split("T")[0], self.date_format)
                        if self.start_date <= closed_date <= self.finish_date:
                            if x["createdBy"]["uniqueName"].lower() == self.analyst_email.lower():
                                self.analyst_counter += 1
                except:
                    self.analyst_counter += 0
            else:
                self.analyst_counter += 0

    def pull_requests_number(self):
        return self.analyst_counter