import pymysql.cursors

from model.project import Project


class DbFixture:
    def __init__(self, host, database, user, password):
        self.host = host,
        self.database = database,
        self.user = user,
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password, autocommit=True)

    def get_project_list(self):
        list_project = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name from mantis_project_table")
            for row in cursor:
                (id_, name) = row
                list_project.append(Project(id_=str(id_), name=name))
        finally:
            cursor.close()
        return list_project

    def get_project_name_list(self):
        new_project_list = []
        for i in self.get_project_list():
            new_project_list.append(i.name)
        return new_project_list

    def destroy(self):
        self.connection.close()
