import random
import string


def generate_random_name():
    return "".join([random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(3, 10))])


username = generate_random_name()
