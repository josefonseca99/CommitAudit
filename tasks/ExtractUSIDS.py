import base64
import urllib.request

from util import ConstantManagement
from config_files import APIConfiguration
import json


class ExtractUSIDS:
    def __init__(self, cell_name=None, iteration_id=None, project_name="b267af7c-3233-4ad1-97b3-91083943100d",
                 organization="grupobancolombia"):

        self.cell_name = cell_name
        self.azure_dev_link = APIConfiguration.AZURE_DEV_LINK
        self.project_name = APIConfiguration.PROJECT
        self.organization = APIConfiguration.ORGANIZATION
        self.iteration_id = iteration_id
        self.access_token = ConstantManagement.CREDENTIALS
        self.headers = {}
        self.US_IDS = []
        self.commit_dict = {}
        self.headers['Content-type'] = "application/json"
        self.headers['Authorization'] = b'Basic ' + base64.b64encode(self.access_token.encode('utf-8'))
        self.items_request = (ConstantManagement.USID_ATTACHMENT_REQUEST_1
                              ).format(self.azure_dev_link,
                                       self.organization,
                                       self.project_name,
                                       self.cell_name,
                                       self.iteration_id
                                       )
        if self.iteration_id is not None and self.cell_name is not None:
            try:
                self.request = urllib.request.Request(self.items_request, headers=self.headers)
                self.opener = urllib.request.build_opener()
                self.response = json.load(self.opener.open(self.request))
                for x in self.response["workItemRelations"]:
                    self.US_IDS.append(x["target"]["id"])
            except:
                pass

    def get_uids_list(self):
        return self.US_IDS
