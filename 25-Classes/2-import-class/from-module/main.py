"""

CLASSES: Calling a class from a previously installed module.


"""

import prettytable

# Creating the object with a class from a previously installed module:
table = prettytable.PrettyTable()  # creating the object.

table.add_column("Planet", ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
table.add_column("Moons amount", [0, 0, 1, 2, 79, 82, 27, 14])
# table.set_style(prettytable.MSWORD_FRIENDLY)
print(table)
