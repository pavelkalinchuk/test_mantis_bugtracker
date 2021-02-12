class ProjectHelper:
    def __init__(self, appproject):
        self.appproject = appproject

    def add_new_project(self):
        wd = self.appproject.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("test_project")
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
