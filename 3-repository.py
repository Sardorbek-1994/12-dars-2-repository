class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def birthday(self):
        self.age += 1

person = Person("Zarina", 25)
print(person.get_name())
print(person.get_age())

person.set_name("Gulnara")
person.set_age(30)
print(person.get_name())
print(person.get_age())

person.birthday()
print(person.get_age())
