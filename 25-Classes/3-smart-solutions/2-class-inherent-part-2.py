"""
CLASS IN PYTHON: INHERITANCE
When a class is the parent of other ones.

"""


# Parent class:
class Animal:
    def __init__(self, num_eyes=2, change_pos=True, underwater=False):
        self.num_eyes = num_eyes
        self.change_pos = change_pos
        self.underwater = underwater

    def breathe(self):
        print("I'm an animal, and I'm moving...")


# child class:
class WhiteShark(Animal):  # Calling the parent class "Animal".
    def __init__(self):
        super().__init__(underwater=True)  # <-- overridden the parent attribute.

    def breathe(self):
        super().breathe()
        print("... underwater.")


# child class:
class Sponge(Animal):  # Calling the parent class "Animal".
    def __init__(self):
        super().__init__(num_eyes=0, change_pos=False, underwater=True)  # <-- overridden the parent attributes.

    def breathe(self):
        print("I'm an animal, stuck in a place forever... and underwater.")


# ------------------------ TESTING -------------------------------------------------------------------------------------

check = Animal()     # <---- change only here (options: Animal, WhiteShark, Sponge)

print(
    f"Number of eyes: {check.num_eyes}\n"    
    f"Can change its position: {check.change_pos}\n"
    f"Can live underwater: {check.underwater}\n"
)
