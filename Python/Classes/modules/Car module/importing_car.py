from car_module import Car 
from electric_car_module import ElectricCar

#importing the car_module and electric_car_module to this this call.

car = Car('BMW','Gtr',2021)
car.car_info()

electriccar = ElectricCar('Nissan','ev100',2022)
print("\nThe electric car info: ")
electriccar.car_info()
electriccar.battery.describe_battery()
