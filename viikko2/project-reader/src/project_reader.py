from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_dict = tomli.loads(content)
        name = toml_dict['tool']['poetry']['name']
        descr = toml_dict['tool']['poetry']['description']
        dependencies = list(toml_dict['tool']['poetry']['dependencies'].keys())
        dev_dependencies = list(toml_dict['tool']['poetry']['group']['dev']['dependencies'].keys())
        authors = list(toml_dict['tool']['poetry']['authors'])
        license = toml_dict['tool']['poetry']['license']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, descr, dependencies, dev_dependencies, license, authors)
