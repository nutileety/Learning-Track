class User:
    def __init__(self,first_name,last_name,location,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.nationality = nationality
        self.login_attempts = 0

    def describe_user(self):
        print("\nThe User details are:")
        print(f"- First Name: {self.first_name.title()}")
        print(f"- Last Name: {self.last_name.title()}")
        print(f"- Location: {self.location.title()}")
        print(f"- Nationality: {self.nationality.title()}")

    def greet_user(self):
        print(f"--------Thank you '{self.first_name.title()}' for sharing your details.--------") 

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, location, nationality):
        super().__init__(first_name, last_name, location, nationality)
        self.previlages = Previlages()

class Previlages:
    def __init__(self,previlages=[]):
        self.previlages = previlages
       
        
    def show_previlages(self):
        print("The admin has the list of previlages he can manages are:")
        if self.previlages:
            for privilage in self.previlages:
                print("-",privilage)
        else:
            print("There is no previlages")

user1 = User('john','wick','new york','american')
user1.describe_user()
user1.greet_user()

print("Attempting to login in .....")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"The login users attempts are: {str(user1.login_attempts)}")

print("\nReseting the login attempts......")
user1.reset_login_attempts()
print(f"The login attempts are: {user1.login_attempts}")

admin = Admin('john','wick','new york','american')
admin.describe_user()

admin.previlages.show_previlages()

print("\nAdding previlages.....")
admin.previlages.previlages = [
                            'can add post',
                            'can delete post',
                            'can ban post',
                            'can block user'
                            ]
admin.previlages.show_previlages()

# user2 = User('chris','hamsworth','paris','french')
# user2.describe_user()
# user2.greet_user()

# user3 = User('scarlett','johnson','sidney','australian')
# user3.describe_user()
# user3.greet_user()