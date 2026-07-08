

# SPECIAL/MAGIC METHODS:

# Let's see some of special (or "magic") methods in Python objects/classes:

    
    
    # >> def __init__(self, ...):

        # This method is called the Constructor-Method and is automatically invoked when you create a new instance of a class. Its primary purpose is to initialize the attributes (or properties) of the object.

            # E.g.
                class Person:
                    def __init__(self, name, age):
                        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
                        self.name = name  # Assign the 'name' attribute
                        self.age = age    # Assign the 'age' attribute

                    def introduce(self):
                        return f"Hello, my name is {self.name} and I am {self.age} years old."

                # Create an instance of Person:
                person = Person("Alice", 30)

                # Access attributes and call methods:
                print(person.name)  # Output: Alice
                print(person.introduce())  
                # Output: Hello, my name is Alice and I am 30 years old.



# More about - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#   /python/python-knowledge/dunders/...