class Eudyptes:
    def __init__(self, name):
        self.name = name


class Chrysolophus(Eudyptes):
    def __init__(self, name):
        super().__init__(name)

    def __eq__(self, other):
        if not isinstance(other, Chrysolophus):
            return False
        return self.name == other.name

    def say_hello(self):
        return "Hello " + self.name + "!"


class Pachyrhynchus(Eudyptes):
    def __init__(self, name):
        super().__init__(name)

    def __eq__(self, other):
        if not isinstance(other, Pachyrhynchus):
            return False
        return self.name == other.name

    def say_goodbye(self):
        return "Good bye " + self.name + "!"
