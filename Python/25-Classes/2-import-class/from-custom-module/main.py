"""

CLASSES: Calling a class from a custom module.


"""

import my_custom_module

# Creating the object with my custom class stored in an external file (module):
planet_1 = my_custom_module.MyOwnPlanet("Montserrat 1984")
# Output with the current planet name: (object.attribute)
print(f"Original planet name: {planet_1.name}")
# Calling the class function that's able to rename the object:
planet_1.rename("MS84")
# Output with the current planet name after the renaming:
print(planet_1.name)
