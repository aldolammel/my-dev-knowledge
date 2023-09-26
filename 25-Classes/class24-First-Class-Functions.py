"""
FIRST-CLASS FUNCTION:

A function you can pass to another function as an argument. All functions in Python (both named and lambda)
are first-class functions.

"""


# Creating the class and its methods -----------------------------------------------------------------------------------
class Car:

    # Initial (and mandatory) function of the class:
    def __init__(self, brand: str, engine_power: float, tires_brand: str, model: str, year: int):
        # these things down below inside the __init__ are the common class attributes that the...
        # ...class methods/functions can call without set parameters, using only "self." to call them:
        self.brand = brand
        self.engine = engine_power
        self.tires_brand = tires_brand
        self.model = model
        self.year = year

    # These things down below are METHODS/FUNCTIONS:
    def start_engine(self):
        print(f"{self.brand}'s engine gets started!")

    def turn_off_engine(self):
        print(f"{self.brand}'s engine gets turned off!")

    def speed_up(self):
        print(f"{self.brand} hit the gas!")

    def speed_down(self):
        print(f"{self.brand}'s braking!")

    def turn_left(self):
        print(f"{self.brand} turned left!")

    def turn_right(self):
        print(f"{self.brand} turned right!")


# Creating the objects to use the class --------------------------------------------------------------------------------

# To use the class, it's need to instantiate it, and this we do by assigning it to one or more objects:
# Para usar a classe, é necessário instanciar ela a uma variável (transformando-a em um objeto):
car1 = Car("Ford", 2.0, "Pirelli", "Fusion", 2014)
car2 = Car("Renault", 1.8, "Goodyear", "Duster", 2020)
car3 = Car("Chevrolet", 4.1, "Firestone", "Tracker", 2024)


# Testing the result ---------------------------------------------------------------------------------------------------

print("\n>> Which is the car2 brand and model and year:")
print(car2.brand, car2.model, car2.year)  # calling the specific object attribute to figure out the car's brand.

print(f"\n>> Make the {car3.brand} starts and goes somewhere else until its stop:")
car3.start_engine()  # calling the specific class function to execute the action.
car3.speed_up()
car3.turn_right()
car3.speed_down()
car3.turn_off_engine()
