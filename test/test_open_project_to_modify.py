def test_open_project_list(app):
    app.session.login("administrator", "root")
    l = app.project.get_project_list()
    assert len(l) > 0