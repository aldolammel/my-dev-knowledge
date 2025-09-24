
"""
    PYTHON BUILT-IN FUNCTIONS: LEN()

        Be aware:
            This is not like the built-in method .count():
                /Python/python-knowledge/count.py


        Purpose:
            Returns the total number of items in a container

        Works with:
            All iterable objects (lists, strings, tuples, dictionaries, sets, etc.)

        Performance:
            O(1) - constant time operation

        Syntax:
            len(iterable)
"""

# Strings
text = "Hello"
print(len(text))  # Output: 5

# Lists
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

# Tuples
my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

# Comparison with len() function:
fruits = ('apple', 'banana', 'apple', 'orange')
print(len(fruits))        # Output: 4 (total items)
print(fruits.count('apple'))  # Output: 2 (occurrences)

# Dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))  # Output: 3

# Sets
my_set = {1, 2, 3, 4}
print(len(my_set))  # Output: 4

# For byte length:
print(len(text.encode('utf-8')))  # Output: 10 (bytes used)

# Checking if Empty
my_list = []
if len(my_list) == 0:
    print("List is empty")

# More Pythonic way:
if not my_list:
    print("List is empty")


# Custom objects with len():
class MyCollection:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

collection = MyCollection([1, 2, 3, 4])
print(len(collection))  # Output: 4