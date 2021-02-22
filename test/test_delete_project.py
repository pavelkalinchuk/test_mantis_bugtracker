from generator.project import project


def test_delete_project(app, db):
    app.session.login("administrator", "root")
    if len(db.get_project_list()) == 0:
        app.project.add_new_project(project)
    old_project_list = db.get_project_list()
    project_ = db.get_project_list()[0].name
    app.project.delete_project(project_)
    new_project_list = db.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    assert project_ not in new_project_list
