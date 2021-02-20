class Project:
    def __init__(self, id_=None, name=None):
        self.id = id_
        self.name = name

    def __repr__(self):
        return "%s" % self.name
