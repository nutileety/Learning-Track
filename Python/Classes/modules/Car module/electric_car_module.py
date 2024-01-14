from car_module import Car

#imported the car_module to this module
#this is also a module.

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