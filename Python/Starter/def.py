class Person:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")

    def info(self):
        print(f"{self.name} is a {self.designation}")

person = Person('Dev','Developer')
person.info()