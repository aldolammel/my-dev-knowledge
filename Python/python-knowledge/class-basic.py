"""
    CLASSES IN PYTHON: INTRODUCTION

    Class is like an outline/blueprint for creating a new object. Object-Oriented Programing (OOP) 
    starts with Classes. An object is anything that you wish to manipulate or change while working
    through the code. 
    
    >> In Python, class names must be written as PascalCase!

    A class is built by:

        >> Its attributes:
            Things that never change: color, size, weight, for example.

        >> Its methods:
            what exactly the class does. Generally, the methods name starts with verbs: "to open the
            link", "to give reload", "to turn the app off", etc. A class can have one or more methods
            within. Methods (function into a class) must be written in snake_case().

        >> Differences between methods and functions:
            All methods are functions, but for a function be a method, the function must call "self"
            in its parameters. To call a function, just type the function name:
                play()
            To call a method, first you must call the object/class:
                musician.play()
"""


# Primitive way to build a class -------------------------------------------------------------------


class UserClassExample1:  # declaring a class as PascalCase, never as snake_case or camelCase.
    pass


user_1 = UserClassExample1()  # creating an object based in my UserClassExample.

user_1.id = '001'  # defining attributes to the object-class.
user_1.username = 'aldolammel'  # attribute
user_1.email = 'aldolammel@gmail.com'  # attribute

print("\nCLASS UserClassExample1 outputs (Primitive building):")
print(user_1.id)
print(user_1.username)
print(user_1.email)
print()


# Expected way to build a class --------------------------------------------------------------------


class UserClassExample2:
    def __init__(self, uid, username, email):
        """Built-in method called 'Constructor', designed to initialize the instance."""
        self.uid = uid
        self.username = username
        self.email = email


user_2 = UserClassExample2('002', 'aldolammel', 'aldolammel@gmail.com')

print("\nCLASS UserClassExample2 outputs (Recommended building):")
print(user_2.uid)
print(user_2.username)
print(user_2.email)
print()


# Amplifying the class usage -----------------------------------------------------------------------


class UserClassExample3:
    def __init__(self, uid, user, email):
        """Built-in method called 'Constructor', designed to initialize the instance."""
        self.uid = uid
        self.user = user
        self.email = email
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """
        param: user: user that will be followed by someone (who is colling the function).
        """
        user.followers += 1  # increases the followers number of the user.
        self.following += 1  # the user who called the function will get their following number increased.


user_3 = UserClassExample3('003', 'aldolammel', 'aldolammel@gmail.com')
user_4 = UserClassExample3('004', 'thyhere', 'thyhere@gmail.com')

print("\nCLASS UserClassExample3 outputs:")
print(f"User {user_3.uid} has {user_3.followers} followers.")
print(f"User {user_3.uid} is following {user_3.following}.")
print(f"User {user_4.uid} has {user_4.followers} followers.")
print(f"User {user_4.uid} is following {user_4.following}.")

user_3.follow(user_4)  # user_3 is saying they are following the user_4.

print("After function follow() --------------------- ")
print(f"User {user_3.uid} has {user_3.followers} followers.")
print(f"User {user_3.uid} is following {user_3.following}.")
print(f"User {user_4.uid} has {user_4.followers} followers.")
print(f"User {user_4.uid} is following {user_4.following}.")
