class Restuarants:
    def __init__(self,restuarant_name,restuarant_cuisines):
        self.restuarant_name = restuarant_name
        self.restuarant_cuisines  = restuarant_cuisines
        self.number_served = 0

    def describe_restuarant(self):
        print(f"Our restuarant '{self.restuarant_name}' is a {self.restuarant_cuisines} restuarant")
        
    def open_restuarant(self):
        print(f"The {self.restuarant_name} is opened.")

    def set_number_served(self,set_number):
        self.number_served = set_number
        print(F"The number of customers in the restuarant are: {self.number_served}")

    def increment_served(self,plus):
        self.number_served += plus
        print(f"This is today's increased customers: {self.number_served}")

class IceCreamStand(Restuarants):
    def __init__(self,restuarant_name,restuarant_cuisines='ice cream'):
        super().__init__(restuarant_name,restuarant_cuisines)
        self.restuarant_name = restuarant_name
        self.flavours = ['venila','butterscoch','pista']

    def icecream_flavours(self):
        print(f"The {self.restuarant_name} has Ice cream flavours are:")
        for flavour in self.flavours:
            print("-",flavour)