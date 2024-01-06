def greet_fun(name):
    print("Hello",name)

greet_fun('Kiccha Sudeep')

#printing about this chapter details
print("\n1.-----------------------------------------------------------")
def display_msg():
    print("Here we will learn about 'Functions'")

display_msg()

#favorite book
print("\n2.-----------------------------------------------------------")
def fav_book(title):
    print("\nOne of my favorite book is :",title.title())

fav_book('ravan - the enemy of aryavarta.')

#multi argument function.
print("\n3.-----------------------------------------------------------")
def describe_pet(pet_type,pet_name):
    print(f"* I has a {pet_type.title()} as my pet.")
    print(f"  And my {pet_type.title()}'s name is {pet_name.title()}.")

describe_pet('dog','bruno')
describe_pet(pet_type='hamster',pet_name='harry')
describe_pet(pet_name='tommy',pet_type='cat')

#default agrument in the function definition
print("\n4. -----------------------------------------------------------")
def describe_pet1(pet_name,pet_type='dog'):
    print(f"My pet is {pet_type} and his name is {pet_name}")

describe_pet1('harrie')