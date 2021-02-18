import unittest


def test_add_new_project(app):
    app.session.login("administrator", "root")
    app.project.add_new_project(name)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)




if __name__ == '__main__':
    unittest.main()


