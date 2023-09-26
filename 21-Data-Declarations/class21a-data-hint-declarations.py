"""
TYPE HINT IN PYTHON: DATA TYPES

Set the data types of an object will help you find potencially bugs easier.

integer = int
float = float
string = str
boolian = bool

"""

# simplest example of object data type declaration:
my_age: int
my_height: float
my_name: str
is_adult = bool


# Function with data type declaration:
def police_check(age: int) -> bool:  # setting the "age" must get an integer and the fnc must return a bool.
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive  # change it to string and see how the declaration will help you to debug.


print(police_check(18))  # change int to string or bool for example to see how the previous declaration helps you.
