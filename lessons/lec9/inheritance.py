# 1. The parent class:

class Animal:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Destroyed")

    def speak(self):
        print(f"{self.name} makes a noise.")


# 2. The child class:

class Dog(Animal):
    # pass
    def speak(self):
        print(f"{self.name} barks.")


# 3. Using the child class:
d = Dog("Rufus")
d.speak()  # Output: Rufus barks.
