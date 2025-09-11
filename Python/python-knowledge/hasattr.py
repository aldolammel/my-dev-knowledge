"""
    hasattr(object, name) -> bool
    Return whether the object has an attribute with the given name.
"""

class MyClass:
    def __init__(self):
        self.existing_attr = 922

obj = MyClass()
print(hasattr(obj, 'existing_attr'))  # True
print(hasattr(obj, 'missing_attr'))   # False