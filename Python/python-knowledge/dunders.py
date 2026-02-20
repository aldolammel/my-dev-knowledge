

# OBJECTS AND ITS BUILT-IN/SPECIAL/MAGIC METHODS:

#     Let's see some of special (or "magic") methods in Python objects/classes:

    
    
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



    # >> def __str__(self):

        # This method is used to define a human-readable string representation of an object. When you call the str() function on an object or use the object in a context where a string is expected (e.g., print()), Python automatically calls the __str__ method to get the string representation of the object.

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



    # >> def __call__(self, ...):

        # This method allows an instance of a class to be called as if it were a function. When you define the __call__ method in a class, instances of that class become callable objects. This means you can use the instance followed by parentheses () and optionally pass arguments, just like you would with a function.

            # E.g.
                class Adder:
                    def __init__(self, initial_value=0):
                        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
                        self.value = initial_value

                    def __call__(self, x):
                        self.value += x
                        return self.value
                    # Create an instance of Adder
                    adder = Adder(10)

                    # Call the instance as if it were a function
                    result = adder(5)
                    print(result)  # Output: 15



    # >> More about:
    #     /classes/1-using-magic-dunder-methods.py