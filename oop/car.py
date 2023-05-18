"""
OOP stands for Object-Oriented Programming,
which is a programming paradigm that focuses on the use of objects,
classes, and their interactions to create software applications.
Python is an object-oriented programming language that supports the creation of classes and objects.

In Python, a class is a blueprint or a template for creating objects,
while an object is an instance of a class.
A class defines a set of properties (attributes) and behaviors (methods) that its objects will have.

Here's an example of a class in Python that represents a car:
"""


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
