from Employee import Employee

firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")
annual_salary = int(input("Enter the salary: "))
employee1 = Employee(firstname,lastname,annual_salary)
employee2 = Employee(firstname,lastname,annual_salary)

print(f"First Name: {employee1.firstname}")
print(f"Last Name: {employee1.lastname}")
print("Raise of the default salary:")
employee1.raise_salary()
print(f"Annual salary : {employee1.annual_salary}")
print("(If you not saisfied with the default salary raise the custom salary below)")
employee2.raise_salary(6000) 
print(f"Annual salary : {employee2.annual_salary}")