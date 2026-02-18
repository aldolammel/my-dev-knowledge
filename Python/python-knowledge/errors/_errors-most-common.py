
"""
    PYTHON: ERRORS, MOST COMMON OF THEM

    Or how to use 'try-catch' in Python:
        ./errors-exceptions.py

"""


# Generic - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
raise Exception("Unknown error!")



# IndexError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
my_list = ["apple", "banana"]
fruit = my_list[2]

raise IndexError("This index doesn't exist!")



# ValueError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
int("a")
raise ValueError("Age must be positive")



# TypeError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
text = "abc"
print(text + 5)
raise TypeError("Please, use just numbers (0-9)!")



# KeyError - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
a_dict = {"key": "value"}
value = a_dict["non_existent_key"]
raise KeyError("Oops!")



# FileNotFound - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Using try-exception: ./errors-exceptions.py
try:
    with open("zzzzzzzzz.txt") as file:
        file.read()
except FileNotFoundError:
    print("xxxxxxxxxxxxxxxxxxxxxx")
