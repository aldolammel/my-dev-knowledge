

# SPECIAL/MAGIC METHODS:

# Let's see some of special (or "magic") methods in Python objects/classes:

    # This method is used to define a human-readable string representation of an object. When you call the str() function on an object or use the object in a context where a string is expected (e.g., print()), Python automatically calls the __str__ method to get the string representation of the object.

    def __str__(self):
        """Defines the human-readable string representation of an object, used by print() and str()."""

            # E.g.
                class Person:
                    def __init__(self, name, age):
                        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
                        self.name = name
                        self.age = age

                    def __str__(self):
                        return f"{self.name}-{self.age}"

                # Create an instance of Person
                person = Person("Alice", 30)

                # Print the object (automatically calls __str__)
                print(person)  # Output: Alice-30



# More about - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#   /python/python-knowledge/dunders/...