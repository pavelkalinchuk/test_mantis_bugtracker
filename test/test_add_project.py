from generator.project import name


def test_add_new_group(app):
    app.session.login("administrator", "root")
    app.project.add_new_project(name)
    # href = app.wd.find_element_by_partial_link_text("%s" % name).text
    l = app.wd.find_elements_by_xpath("//a[@href = 'manage_proj_edit_page.php?project_id=']")
    # assert
