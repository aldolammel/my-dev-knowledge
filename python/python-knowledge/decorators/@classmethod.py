
"""
    PYTHON > DECORATOR: @CLASSMETHOD

    The @classmethod is a Python decorator that makes a method belong to the class itself, rather than to a particular instance of that class.
   
    >> WHAT IT DOES:
        - The key difference is what Python automatically passes as the first argument.

    >> REASON TO USE IT:
        - A common use is when the method needs to work with class-level information rather than instance-level information.
"""

# Example NOT using @classmethod - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Person:
    def say_hello(self):  # self = call only an instance!
        print(f"Hello, I am {self.name}.")

person = Person()
person.name = "Aldo"

person.say_hello()


# Example USING @classmethod - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class Person:
    species = "Human"

    @classmethod
    def get_species(cls):  # cls = call an instance OR a class!
        return cls.species

print(Person.get_species())
