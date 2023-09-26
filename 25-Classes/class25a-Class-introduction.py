"""
CLASSES IN PYTHON: INTRODUCTION
Class is like an outline/blueprint for creating a new object. Object-Oriented Programing (OOP) starts with Classes.
An object is anything that you wish to manipulate or change while working through the code.
Class names must be written as PascalCase.

A class is built by:

>> Its attributes:
    Things that never change: color, size, weight, for example.

>> Its methods:
    what exactly the class does. Generally, the methods starts with verbs: "to open the link", "to give reload",
    "to turn the app off", etc. A class can have one or more methods within.
    Methods (function into a class) must be written in snake_case().
"""


# Primitive way to build a class ---------------------------------------------------------------------------------------


class UserClassExample1:  # declaring a class as PascalCase, never as snake_case or camelCase.
    pass


user_1 = UserClassExample1()  # creating an object based in my UserClassExample.

user_1.id = '001'  # defining attributes to the object-class.
user_1.username = 'aldolammel'  # attribute
user_1.email = 'aldolammel@gmail.com'  # attribute

print(user_1.id)
print(user_1.username)
print(user_1.email)
print()


# Expected way to build a class ---------------------------------------------------------------------------------------


class UserClassExample2:
    def __init__(self, uid, username, email):  # "__init__" means "initializing the class attributes".
        self.uid = uid
        self.username = username
        self.email = email


user_2 = UserClassExample2('001', 'aldolammel', 'aldolammel@gmail.com')

print(user_2.uid)
print(user_2.username)
print(user_2.email)
print()


# Amplifying the class usage -------------------------------------------------------------------------------------------


class UserClassExample3:
    def __init__(self, uid, username, email):
        self.uid = uid
        self.username = username
        self.email = email
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_3 = UserClassExample3('003', 'aldolammel', 'aldolammel@gmail.com')
user_4 = UserClassExample3('004', 'thyhere', 'thyhere@gmail.com')

user_3.follow(user_4)

print(user_3.followers)
print(user_3.following)
print()
