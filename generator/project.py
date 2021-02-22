import random
import string

from model.project import Project


def generate_random_name():
    return "".join([random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(5, 15))])


project = (Project(name=generate_random_name()))
# project_name = generate_random_name()
