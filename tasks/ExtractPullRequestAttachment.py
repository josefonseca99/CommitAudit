import base64
import urllib.request

from util import ConstantManagement
from datetime import date, datetime
import json


class ExtractPullRequestAttachment:
    def __init__(self, repo_name=None, analyst_email=None, start_date=None, finish_date=None,
                 project_name="b267af7c-3233-4ad1-97b3-91083943100d",
                 organization="grupobancolombia"):

        self.project_name = project_name
        self.organization = organization
        self.repo_name = repo_name
        self.analyst_email = analyst_email
        self.analyst_counter = 0
        self.date_format = "%Y-%m-%d"

        if start_date is not None and finish_date is not None:
            self.start_date = datetime.strptime(start_date, self.date_format)
            self.finish_date = datetime.strptime(finish_date, self.date_format)
            self.closed_date = ""
            self.access_token = ConstantManagement.CREDENTIALS
            self.headers = {}
            self.commit_dict = {}
            self.headers['Content-type'] = "application/json"
            self.headers['Authorization'] = b'Basic ' + base64.b64encode(self.access_token.encode('utf-8'))
            self.items_request = (ConstantManagement.COMMIT_STATUS_ATTACHMENT_REQUEST_1
                                  ).format(self.organization,
                                           self.project_name,
                                           self.repo_name)

            self.request = urllib.request.Request(self.items_request, headers=self.headers)
            self.opener = urllib.request.build_opener()
            self.response = json.load(self.opener.open(self.request))
            try:
                for x in self.response["value"]:
                    closed_date = datetime.strptime(x["closedDate"].split("T")[0], self.date_format)
                    if self.start_date <= closed_date <= self.finish_date:
                        if x["createdBy"]["uniqueName"] == self.analyst_email:
                            self.analyst_counter += 1
            except:
                pass

    def pull_requests_number(self):
        return self.analyst_counter
