class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

person = Person("Ali")
print(person.get_name())

person.set_name("Olim")
print(person.get_name())
