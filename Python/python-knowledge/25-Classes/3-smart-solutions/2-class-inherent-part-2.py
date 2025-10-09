"""
CLASS IN PYTHON: INHERITANCE
When a class is the parent of other ones.

"""


# Parent class:
class Animal:
    def __init__(self, num_eyes=2, change_pos=True, underwater=False):
        """Built-in method called 'Constructor', designed to initialize the instance."""
        self.num_eyes = num_eyes
        self.change_pos = change_pos
        self.underwater = underwater
        self.breathe()

    def breathe(self):
        print("I'm an animal.")


# child class:
class WhiteShark(Animal):  # Calling the parent class "Animal".
    def __init__(self):
        """Built-in method called 'Constructor', designed to initialize the instance."""
        super().__init__(underwater=True)  # <-- overridden the parent attribute.

    def breathe(self):                       # As the parent has a method w/ the same name, this one's overridden that
        super().breathe()                    # and also calling the original method to show the first msg before the
        print("And I'm moving underwater.")  # next message.


# child class:
class Sponge(Animal):  # Calling the parent class "Animal".
    def __init__(self):
        """Built-in method called 'Constructor', designed to initialize the instance."""
        super().__init__(num_eyes=0, change_pos=False, underwater=True)  # these params overridden the parent attributes
        # The same as the params, but declared in the subclass constructor:
        # self.num_eyes = 0
        # self.change_pos = False
        # self.underwater = True

    def breathe(self):
        super().breathe()
        print("And I'm stuck in the same underwater place forever.")


# ------------------------ TESTING -------------------------------------------------------------------------------------

check = Sponge()     # <---- change only here (options: Animal, WhiteShark, Sponge)

print(
    f"Number of eyes: {check.num_eyes}\n"    
    f"Can change its position: {check.change_pos}\n"
    f"Can live underwater: {check.underwater}\n"
)
