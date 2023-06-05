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

    # DRY DON'T REPEAT YOURSELF
    # self vs super
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    # pass
    def speak(self):
        print(f"{self.name} & {self.type} barks.")

    # pass
    def test(self):
        super().speak()


# 3. Using the child class:
d = Dog("Rufus", "L2")
d.test()  # Output: Rufus barks.
