"""
PYTHON'S BUILT-IN ERRORS: ANOTHER EXAMPLE OF RAISING ERROR:
Let's create a simple app to raise an error as example down below.

"""


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = list()

    def __len__(self):
        return len(self.cars)

    def fnc_add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a "{car.__class__.__name__}" to the garage, but u can only add "Car" objs.')
        # raise NotImplementedError('Not ready yet.')        # flagging if the function is not done yet.
        self.cars.append(car)


ford = Garage()
# car = Car('Ford', 'Fiesta')
ford.fnc_add_car('Fiesta')    # ford.fnc_add_car(car)  <---- to remove the error.
# print(len(ford))
