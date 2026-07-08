
"""
    CLASSES: USING MAGIC / 'DUNDER' METHODS

    Dunder methods, short for "double underscore methods," are special methods in Python that have double underscores at the beginning and end of their names. They are also known as "magic methods" or "special methods." These methods are predefined by the Python language and allow you to customize the behavior of your objects for built-in operations such as arithmetic operations, comparisons, and type conversions.

    E.g.:

        /python/python-knowledge/dunders/...


    Dunders applied in Django framework:
        /python/web-development/django/dunder-methods-init.py

"""


class MyGarage:
    def __init__(self, city):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        self.city = city
        self.cars = []

    def __len__(self):          # It sets if asked the class length 'len(MyGarage)', it'll return 'len(self.cars)'.
        return len(self.cars)

    def __getitem__(self, i):   # defining a method where it will find objects in a list.
        return self.cars[i]

    def __str__(self):
        return self.city        # if the object is called in a print() with no method applied, it'll print out the city.


home1 = MyGarage('Charqueadas')
home1.cars.append('Chevette 1.6')
home1.cars.append('Uno 1.0')
home1.cars.append('Opalla 4.1')

print(f'House: {home1.city}')
print(f'How many cars in that city: {len(home1)}')           # only works like this 'cause '__len__' into the class.
print(f'The first car in {home1} garage: {home1[0]}')   # only works like this 'cause '__getitem__' into the class.
print('\nAll cars in "MyGarage" list:')
for car in home1.cars:
    print(f'- {car}')
