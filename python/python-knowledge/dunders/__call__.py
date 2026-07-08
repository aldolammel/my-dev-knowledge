

# SPECIAL/MAGIC METHODS:

# Let's see some of special (or "magic") methods in Python objects/classes:

    
    # >> def __call__(self, ...):

        # This method allows an instance of a class to be called as if it were a function. When you define the __call__ method in a class, instances of that class become callable objects. This means you can use the instance followed by parentheses () and optionally pass arguments, just like you would with a function.

            # E.g.
                class Adder:
                    def __init__(self, initial_value=0):
                        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
                        self.value = initial_value

                    def __call__(self, x):
                        """This method allows an instance of a class to be called as if it were a function."""
                        self.value += x
                        return self.value
                    # Create an instance of Adder
                    adder = Adder(10)

                    # Call the instance as if it were a function
                    result = adder(5)
                    print(result)  # Output: 15



# More about - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#   /python/python-knowledge/dunders/...