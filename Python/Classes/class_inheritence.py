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

class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:
    def __init__(self,battery_size=40):
         self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size}-KWh battery. ")

    def get_range(self):
        if self.battery_size == 40:
            self.range = 150
        elif self.battery_size == 65:
            self.range = 185

        print(f"The {self.battery_size}-KWh battery can go upto {self.range} miles")

    def upgrade_battery(self,upgrade):
        if self.battery_size != 65:
            self.battery_size = upgrade

my_electric_car = ElectricCar('nissan','gtr',2023)
my_electric_car.car_info()
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()

print("After upgrading the battery size:")
my_electric_car.battery.upgrade_battery(65)
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()