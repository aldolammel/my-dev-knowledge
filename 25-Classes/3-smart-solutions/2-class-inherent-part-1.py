"""
CLASS INHERENT: SUPER()

    It's a function used to give access to the methods of a parent class.
    It returns a temporary object of a parent class when used.

"""


class Guitar:
    # "Guitar" is our PARENT class, where its attributes and methods could be called by other classes.
    def __init__(self):
        # Example of an attribute:
        self.n_strings = 6
        self.color = "Black"
        # Calling a simple method automatically when the "Guitar" class runs:
        self.play()

    def play(self):
        # Simple method example.
        print("Playing: pam pam pam pam pam!")


class ElectricGuitar(Guitar):
    # "ElectricGuitar" is a CHILD class of "Guitar" one, where its attribute can or not be overridden.
    def __init__(self):
        super().__init__()
        self.n_strings = 8  # This is overridden the original attribute from "Guitar" class exclusively for this class.


# Here we're creating an object based on Guitar() class, so this class has only 6 strings as one of its attributes:
my_guitar1 = Guitar()
print(my_guitar1.n_strings)
print(my_guitar1.color)

# But here, it's an Electric Guitar that's a child of Guitar() class.
# All Electric Guitars have 8 strings here where the color still been black:
my_guitar2 = ElectricGuitar()
print(my_guitar2.n_strings)
print(my_guitar2.color)

