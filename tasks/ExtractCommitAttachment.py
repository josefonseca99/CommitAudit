import base64
import urllib.request

from util import ConstantManagement
import json


class ExtractCommitAttachment:
    def __init__(self, from_date=None, to_date=None, username=None, project_name=None):
        self.from_date = from_date
        self.to_date = to_date
        self.username = username
        self.project_name = project_name
        self.access_token = ConstantManagement.CREDENTIALS
        self.headers = {}
        self.commit_dict = {}
        self.headers['Content-type'] = "application/json"
        self.headers['Authorization'] = b'Basic ' + base64.b64encode(self.access_token.encode('utf-8'))
        self.items_request = (ConstantManagement.ATTACHMENT_REQUEST_1 \
                              + ConstantManagement.FROM_DATE_REQUEST \
                              + ConstantManagement.TO_DATE_REQUEST \
                              + ConstantManagement.USERNAME \
                              + ConstantManagement.ATTACHMENT_REQUEST_2).format(self.project_name,
                                                                                self.from_date,
                                                                                self.to_date,
                                                                                self.username)
        self.counter = 0

        try:
            self.request = urllib.request.Request(self.items_request, headers=self.headers)
            self.opener = urllib.request.build_opener()
            self.response = json.load(self.opener.open(self.request))
            self.counter = self.response["count"]
        except:
            pass

    def get_commit_number(self):
        return self.counter
