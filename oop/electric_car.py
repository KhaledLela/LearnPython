from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
        self.charge_level = 100

    def charge(self, charge_amount):
        self.charge_level += charge_amount
        if self.charge_level > 100:
            self.charge_level = 100

    def get_charge_level(self):
        return self.charge_level
