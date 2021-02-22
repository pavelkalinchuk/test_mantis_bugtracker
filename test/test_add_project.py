from generator.project import project


def test_add_new_group(app, db):
    old_project_list = db.get_project_list()
    app.session.login("administrator", "root")
    app.project.add_new_project(project)
    new_project_list = db.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)
    assert project.name == new_project_list[-1].name
