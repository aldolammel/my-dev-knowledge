"""
MAGIC OR 'DUNDER' METHODS:

"""


class ClassGarage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):               # defining a method where it will find objects in a list.
        return self.cars[i]


_ford = ClassGarage()
_ford.cars.append('Fiesta')
_ford.cars.append('Focus')
_ford.cars.append('Fusion')

print('How many cars:', len(_ford))        # only works because that '__len__' into the class.
print('The first car:', _ford[0])          # only works because that '__getitem__'.

print('\nAll cars in the ClassGarage list:')
for _car in _ford:
    print(_car)
