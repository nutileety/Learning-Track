class Car:
    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model= model
        self.year = year
        self.meter = 0

    def update_milage(self,milage):
        if milage >= self.meter:
            self.meter = milage
        else:
            print("Can't rollback the milage, Sorry!")

    def car_info(self):
        print(f"{self.make} {self.model} {self.year}")

    def car_milage(self):
        print(f"The milage of {self.make} is {self.meter} miles")

    def increment(self,miles):
        self.meter += miles

car = Car('Audi','s8',2021)
car.car_info()
car.update_milage(3400)
car.increment(100)
car.car_milage()