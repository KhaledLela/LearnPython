class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return 'Woof!'


def get_pet(pet='dog'):
    """The factory method"""
