class Employee:
    def __init__(self,firstname,lastname,annual_salary):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary

    def raise_salary(self,amount=5000):
        """raising a default salary to the annual salary"""
        self.annual_salary += amount
        
