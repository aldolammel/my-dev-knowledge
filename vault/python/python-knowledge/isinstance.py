"""
    ISINSTANCE: 
    The isinstance() function returns True if the specified object is of the specified type, otherwise False. If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

    >> Syntax:
        isinstance(object, type)

    >> Parameters:
        object: object (required)
        type: a type of a class, or a tuple of types and/or classes.


"""

# Simplest example:
name = 123
if not isinstance(name, str):
    raise TypeError("Name must be a string")


# Check if "Hello" is one of the types described in the type parameter:
x = isinstance("Hello", (float, int, str, list, dict, tuple)) 

# Check if y is an instance of myObj:
class myObj:
  name = "John"
y = myObj()
x = isinstance(y, myObj) 


""" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    Related:
        issubclass()
"""