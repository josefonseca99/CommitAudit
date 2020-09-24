import urllib.request
from urllib.error import URLError
from config_files import APIConfiguration
from util import ConstantManagement
import json


class ExtractTechnicalDebt:
    def __init__(self, repo_name=None):

        if repo_name is not None and repo_name != '':
            self.repo_name = repo_name.replace(" ", "%20")
            self.access_token = APIConfiguration.BANCOLOMBIA_API_TOKEN
            self.headers = {}
            self.commit_dict = {}
            self.headers['Content-type'] = "application/json"
            self.items_request = ConstantManagement.TECHNICAL_DEBT_REQUEST.format(self.repo_name)

            try:
                self.request = urllib.request.Request(self.items_request, headers=self.headers)
                self.opener = urllib.request.build_opener()
                self.response = json.load(self.opener.open(self.request))
                self.tech_debt = self.response["component"]["measures"][0]["value"]

            except URLError as e:
                self.tech_debt = 'Sin conexión a la VPN'
            except:
                self.tech_debt = 'Sin datos de repositorio'
        else:
            self.tech_debt = 'Sin datos de repositorio'

    def get_technical_debt_time(self):
        return self.tech_debt
