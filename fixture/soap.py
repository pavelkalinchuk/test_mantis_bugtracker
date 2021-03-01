from suds import WebFault
from suds.client import Client


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_name_list(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            project_name_list = []
            projects_list = client.service.mc_projects_get_user_accessible(username, password)
            for i in projects_list:
                project_name_list.append(i.name)
            return project_name_list
        except WebFault:
            return False
