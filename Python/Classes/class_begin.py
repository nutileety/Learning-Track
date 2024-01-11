class Dog:
    def __init__(self,name,age):
        name = input("Enter the name of the dog: ")
        self.name = name
        age = input("Enter the age of the dog: ")
        self.age = age

    def sit(self):
        print(f"My Dog {self.name} is sitting")

    def roll_over(self):
        print(f"My Dog {self.name} is rolling")


my_dog = Dog('Maxi',6)
print(f"The name of my dog is: {my_dog.name}")
print(f"The age of {my_dog.name} is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()