class Restuarants:
    def __init__(self,restuarant_name,restuarant_cuisines):
        self.restuarant_name = restuarant_name
        self.restuarant_cuisines  = restuarant_cuisines
        self.number_served = 0

    def describe_restuarant(self):
        print(f"Our restuarant '{self.restuarant_name}' is a 3-star restuarant")
        
    def open_restuarant(self):
        print(f"The {self.restuarant_name} is opened.")

    def set_number_served(self,set_number):
        self.number_served = set_number
        print(F"The number of customers in the restuarant are: {self.number_served}")

    def increment_served(self,plus):
        self.number_served += plus
        print(f"This is today's increased customers: {self.number_served}")

restuarants = Restuarants('The Fern','Indian')
print(f"The name of our restuarant is: {restuarants.restuarant_name}")
print(f"The cuisines of this retuarants is: {restuarants.restuarant_cuisines}")
restuarants.describe_restuarant()
restuarants.open_restuarant()
restuarants.set_number_served(15)
restuarants.increment_served(10)

# restuarants1 = Restuarants('Royal Arcade','Italian')
# print(f"\nThe name of our restuarant is: {restuarants1.restuarant_name}")
# print(f"The cuisines of this retuarants is: {restuarants1.restuarant_cuisines}")
# restuarants1.describe_restuarant()

# restuarants2 = Restuarants('The clief','chineese')
# print(f"\nThe name of our restuarant is: {restuarants2.restuarant_name}")
# print(f"The cuisines of this retuarants is: {restuarants.restuarant_cuisines}")
# restuarants2.describe_restuarant()