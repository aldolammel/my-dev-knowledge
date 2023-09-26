"""
CLASS IN PYTHON:

All classes have at least an attribute and a method (a function).

"""

# let's create a Netflix class for their clients:


class Clients:

    # creating the basic: the class' attributes/features.
    # A class always has a init for their attributes.
    # In init is where we create all the variables that will be used in this class.
    def __init__(self, name, email, user_plan):
        self.name = name
        self.email = email
        self.plan_list = ['basic', 'family']
        if user_plan in self.plan_list:
            self.user_plan = user_plan
        else:
            print('Invalid plan!')

    def fnc_planChange(self, new_plan):
        if new_plan in self.plan_list:
            self.user_plan = new_plan
        else:
            print('Invalid plan!')

    def fnc_familyMovies(self, movie_to_watch, movie_plan):
        if self.user_plan == movie_plan:
            print('See movie:', movie_to_watch)
        else:
            print('Your plan doesnt support this movie. Sorry!')


# creating a client:
_clientCreated = Clients('Aldo', 'aldolammel@gmail.com', 'basic')
print(_clientCreated.name, _clientCreated.user_plan)

# trying to watch a movie from family plan:
_clientCreated.fnc_familyMovies('Harry Potter', 'family')

# changing the client plan to watch family movies too:
_clientCreated.fnc_planChange('family')
print(_clientCreated.name, _clientCreated.user_plan)
_clientCreated.fnc_familyMovies('Harry Potter', 'family')
