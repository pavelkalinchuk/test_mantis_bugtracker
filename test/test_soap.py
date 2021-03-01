def test_soap(app):
    project_list = app.soap.get_project_name_list("administrator", "root")
    print("\n" + str(project_list))
    print(len(project_list))
