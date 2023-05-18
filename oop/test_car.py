from car import Car
from electric_car import ElectricCar

# my_car = Car("Toyota", "Corolla", 2022)
# my_car.accelerate(30)
# my_car.accelerate(20)
# print(my_car.get_speed())   # Output: 50
#
# my_car.brake(10)
# my_car.brake(30)
# print(my_car.get_speed())   # Output: 10


my_electric_car = ElectricCar("Tesla", "Model S", 2023, 75)
my_electric_car.accelerate(30)
print(my_electric_car.get_speed())   # Output: 30

my_electric_car.charge(20)
print(my_electric_car.get_charge_level())   # Output: 100
