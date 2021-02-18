class ProjectHelper:
    def __init__(self, appproject):
        self.appproject = appproject

    def add_new_project(self, project):
        wd = self.appproject.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("%s" % project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project(self):
        wd = self.appproject.wd
        self.open_manage_project_page()
        wd.find_element_by_link_text("test_project").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def open_manage_project_page(self):
        wd = self.appproject.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def get_project_list(self):
        project_list = []
        wd = self.appproject.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//tr[@class='row-1']")
        return project_list

    def open_project_to_modify(self, project):
        wd = self.appproject.wd
        self.open_manage_project_page()
        wd.find_element_by_partial_link_text(project).click()

    def find_project_in_page(self, project):
        wd = self.appproject.wd
        self.open_manage_project_page()
        find = wd.find_element_by_partial_link_text(project)
        return find
