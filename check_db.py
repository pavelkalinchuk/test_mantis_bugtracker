import random

from fixture.db import DbFixture
# from model.group import Group

db = DbFixture(host="localhost", database="bugtracker", user="root", password="")

try:
    # if len(db.get_group_list()) > 0:
    #     group = random.choice(db.create_groupid_list())
    # print("\n" + "-" * 10 + "Contacts" + "-" * 10)
    print("-" * 20)
    l = db.get_project_list()
    for item in l:
        print(item)
    print("-" * 20)
    print("Count projects: " + str(len(l)) + "\n")
    # print("*** Total contacts count: " + str(len(l)) + " ***" + "\n" + "\n" + "-" * 10 + "Groups" + "-" * 10)
    # l = db.get_group_list()
    # for item in l:
    #     print(item)
    # print("*** Total groups count: " + str(
    #     len(l)) + " ***" + "\n" + "\n" + "-" * 10 + "Contacts in group" + "-" * 10)
    # if len(db.get_group_list()) > 0:
    #     l = db.get_contacts_in_group(Group(id=group))
    #     for item in l:
    #         print(item)
    # print("*** Total contacts in group id " + group + " count: " + str(
    #     len(l)) + " ***" + "\n" + "\n" + "-" * 10 + "Contacts not in group" + "-" * 10)
    # if len(db.get_group_list()) > 0:
    #     l = db.get_contacts_not_in_group(Group(id=group))
    #     for item in l:
    #         print(item)
    # print("*** Total contacts not in group id " + group + " count: " + str(len(l)) + " ***" + "\n" + "\n" + "Контакты не состоящие в какай-либо группе")
    # l = db.create_contactid_list_from_contacts_not_in_group()
    # print(l)
    # # a = db.get_group_list()
    # # print(random.choice(a).id)
finally:
    pass
