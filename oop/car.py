class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, speed):
        self.speed += speed

    def brake(self, speed):
        self.speed -= speed
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed
