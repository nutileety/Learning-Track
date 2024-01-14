from user_module import User

#importin user class module to the admin class module

class Admin(User):
    def __init__(self, first_name, last_name, location, nationality):
        super().__init__(first_name, last_name, location, nationality)
        self.previlages = Previlages()

class Previlages:
    def __init__(self):
        self.previlages = [
                            'can add post',
                            'can delete post',
                            'can ban post',
                            'can block user'
                            ]
        
    def show_previlages(self):
        print("The admin has the list of previlages he can manages are:")
        for privilage in self.previlages:
            print("-",privilage)