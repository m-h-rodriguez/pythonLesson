class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(self.name)
        print(self.age)


people = [Person("John", 36), Person("Richard", 28)]

for peeps in people:
    peeps.print_details()
