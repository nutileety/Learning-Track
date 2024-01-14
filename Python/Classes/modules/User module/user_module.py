class User:
    def __init__(self,first_name,last_name,location,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.nationality = nationality
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nThe {self.first_name.title()}'s details are:")
        print(f"- First Name: {self.first_name.title()}")
        print(f"- Last Name: {self.last_name.title()}")
        print(f"- Location: {self.location.title()}")
        print(f"- Nationality: {self.nationality.title()}\n")

    def greet_user(self):
        print(f"--------Thank you '{self.first_name.title()}' for sharing your details.--------") 

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0