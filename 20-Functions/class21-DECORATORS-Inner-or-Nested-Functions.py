"""
INNER FUNCTIONS:
Inner functions, also known as NESTED FUNCTIONS, are functions that you define inside other functions. In Python,
this kind of function has direct access to variables and names defined in the enclosing function.
Inner functions have many uses, most notably as closure factories and decorator functions.

"""


def replicator(fnc):
    def nested_fnc():
        print("You are using inner functions structure:")
        fnc()
        fnc()
        fnc()
    return nested_fnc


@replicator  # When this function is called, automatically it will use the delay_decorator function structure.
def say_hello():
    print("Hello")


def say_greeting():
    print("How are you?")


@replicator  # When this function is called, automatically it will use the delay_decorator function structure.
def say_bye():
    print("Bye")


""" TRY TO UNCOMMENT EACH LINE BELOW TO CHECK THE RESULTS: """
say_hello()  # it's using the inner function logic.
# say_greeting()  # it's NOT using the inner function logic.
# say_bye()  # it's using the inner function logic.

