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

    # def get_contact_list(self):
    #     list_contacts = []
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute(
    #             "select id, firstname, middlename, lastname, address, home, mobile, work, email, phone2 from addressbook where deprecated = '0000-00-00 00:00:00'")
    #         for row in cursor:
    #             (id_, firstname, middlename, lastname, address, home, mobile, work, email, phone2) = row
    #             list_contacts.append(Contact
    #                                  (id=str(id_),
    #                                   first_name=firstname,
    #                                   middle_name=middlename,
    #                                   last_name=lastname,
    #                                   address=address,
    #                                   phone_home=home,
    #                                   phone_mobile=mobile,
    #                                   phone_work=work,
    #                                   email=email,
    #                                   phone_secondary=phone2
    #                                   ))
    #     finally:
    #         cursor.close()
    #     return list_contacts

    def destroy(self):
        self.connection.close()
