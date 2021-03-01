from generator.project import project


def test_delete_project(app, username="administrator", password="root"):
    app.session.login(username, password)
    if len(app.soap.get_project_name_list(username, password)) == 0:
        app.project.add_new_project(project)
    old_project_list = app.soap.get_project_name_list(username, password)
    project_ = app.soap.get_project_name_list(username, password)[0]
    app.project.delete_project(project_)
    new_project_list = app.soap.get_project_name_list(username, password)
    assert len(old_project_list) - 1 == len(new_project_list)
    assert project_ not in new_project_list
