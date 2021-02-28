from generator.project import project


def test_add_new_group(app, db):
    old_project_list = db.get_project_name_list()
    app.session.login("administrator", "root")
    app.project.add_new_project(project)
    new_project_list = db.get_project_name_list()
    assert len(old_project_list) + 1 == len(new_project_list)
    assert project.name in new_project_list
