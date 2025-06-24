"""
TYPE HINT IN PYTHON: DATA TYPES

Set the data types of an object will help you find potentially bugs easier.

integer = int
float = float
string = str
boolean = bool
containers = list, tuple, set, dict
object = object
anything = any

"""

# simplest example of object data type declaration:
age: int
height: float
name: str
is_adult: bool
user: object
date: str
car: list
store: dict
final_score: tuple


# Function with data type declaration:
def police_check(age: int) -> bool:  # "age" must get integer and fnc return bool.
    can_drive = False
    if age > 18:
        can_drive = True
    return can_drive  # change it to string and see how the declaration will help you to debug.


print(police_check(18))  # change int to string or bool to see how the previous declaration helps.
