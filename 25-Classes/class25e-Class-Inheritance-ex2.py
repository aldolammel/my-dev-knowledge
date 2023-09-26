"""
CLASS IN PYTHON: INHERITANCE
When a class is the parent of other ones.

"""


# Main class Animal:
class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


# Subclass Fish:
class Fish(Animal):  # Here I'm calling the parent class "Animal".

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")


Nemo = Fish()  # Try with Animal() and Fish().

Nemo.breathe()

