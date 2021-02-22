def test_delete_project(app, db):
    old_project_list = db.get_project_list()
    app.session.login("administrator", "root")
    project = old_project_list[0].name
    app.project.delete_project(project)
    new_project_list = db.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    assert project not in new_project_list
