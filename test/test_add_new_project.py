def test_add_new_project(app):
    app.session.login("administrator", "root")
    app.project.add_new_project()