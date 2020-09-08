import base64
import urllib.request
from urllib.error import URLError

from util import ConstantManagement
import json


class ExtractCodeSmells:
    def __init__(self, repo_name=None):
        if repo_name is not None and repo_name != '':
            self.repo_name = repo_name.replace(" ", "%20")
            self.access_token = ConstantManagement.CREDENTIALS
            self.headers = {}
            self.commit_dict = {}
            self.headers['Content-type'] = "application/json"
            self.items_request = ConstantManagement.CODE_SMELL_REQUEST.format(self.repo_name)

            try:
                self.request = urllib.request.Request(self.items_request, headers=self.headers)
                self.opener = urllib.request.build_opener()
                self.response = json.load(self.opener.open(self.request))
                self.code_smells = self.response["component"]["measures"][0]["value"]
            except URLError as e:
                self.code_smells = 'Sin conexión a la VPN'
            except:
                self.code_smells = 'Sin datos de repositorio'
        else:
            self.code_smells = 'Sin datos de repositorio'

    def get_code_smells_time(self):
        return self.code_smells
