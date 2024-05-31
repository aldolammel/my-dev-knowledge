"""
CLASS IN PYTHON:

All classes have at least an attribute and a method (a function).

"""

# let's create a Netflix class for their clients:


class Clients:

    # creating the basic: the class' attributes/features.
    # A class always has a init for their attributes.
    # In init is where we create all the variables that will be used in this class.
    def __init__(self, name, email, plan):
        self.name = name
        self.email = email
        self.plan_list = ['basic', 'family']
        self.plan = None
        if plan in self.plan_list:
            self.plan = plan
        else:
            print('Invalid plan!')

    def plan_change(self, new_plan):
        if new_plan in self.plan_list:
            self.plan = new_plan
        else:
            print('Invalid plan!')

    def family_movies(self, movie_to_watch, movie_plan):
        if self.plan == movie_plan:
            print('See movie:', movie_to_watch)
        else:
            print('Your plan doesnt support this movie. Sorry!')


# creating a client:
client_1 = Clients('Aldo', 'aldolammel@gmail.com', 'basic')
print(client_1.name, client_1.plan)

# trying to watch a movie from family plan:
client_1.family_movies('Harry Potter', 'family')

# changing the client plan to watch family movies too:
client_1.plan_change('family')
print(client_1.name, client_1.plan)
client_1.family_movies('Harry Potter', 'family')
