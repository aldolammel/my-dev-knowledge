"""
CLASS IN PYTHON: INHERITANCE
When a class is the parent of other ones.

"""


# Main class Animal:
class Animal:
    def __init__(self):
        self.num_eyes = 2
        self.can_move = True

    def breathe(self):
        print("Inhale, Exhale.")


# Subclass Fish:
class Fish(Animal):  # Here I'm calling the parent class "Animal".
    def __init__(self):
        super().__init__()
        self.can_swing = True

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")


nemo = Fish()  # Try with Animal() and Fish().
nemo.breathe()
