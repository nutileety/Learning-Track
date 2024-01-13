class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"The id {self.id} is alloted to the employee: {self.name}")

class Programmer(Employee):
    def programmer_details(self):
        print(f"The Programmer {self.name} learned the Python language.")

employee = Employee('Leo Das',700)
employee.show_details()

programmer = Programmer('Harold Das',800)
programmer.show_details()
programmer.programmer_details()