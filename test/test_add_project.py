from generator.project import project


def test_add_new_group(app, username="administrator", password="root"):
    old_project_list = app.soap.get_project_name_list(username, password)
    app.session.login(username, password)
    app.project.add_new_project(project)
    new_project_list = app.soap.get_project_name_list(username, password)
    assert len(old_project_list) + 1 == len(new_project_list)
    assert project.name in new_project_list
