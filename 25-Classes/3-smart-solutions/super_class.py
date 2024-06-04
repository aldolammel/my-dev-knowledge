class ParentClass:
    def __init__(self, name):
        self.name = name

    def msg_greet_parent(self):
        return f"Hello, my name is {self.name}."


class Child(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def msg_greet_child(self):
        parent_greeting = super().msg_greet_parent()
        return f"{parent_greeting} I am {self.age} years old."
