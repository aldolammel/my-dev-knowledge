"""

CLASSES (Object-oriented Programming):

-class- is the blueprint of an object in OOP.
Using the PrettyTable module to exemplify how classes work.

"""

# # import external_module
# # print(external_module.test_var)
#
# from turtle import Turtle, Screen
#
# donatello = Turtle()
# donatello.shape('turtle')
# donatello.color('red')
# donatello.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()                  # close the app only after a click.

from prettytable import PrettyTable, MSWORD_FRIENDLY

table = PrettyTable()  # creating the object.

table.add_column("Planet", ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
table.add_column("Moons amount", [0, 0, 1, 2, 79, 82, 27, 14])
table.set_style(MSWORD_FRIENDLY)
print(table)
