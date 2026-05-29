

"""
FUNCTIONS: **KWARGS KEYWORD ARGUMENTS
(Funções: Argumentos nomeados):

It allows us to create a dictionary with many keys in a function.


By convention, it is called "**kwargs".

- args = returns always a TUPLE (more about: ./args.py)
- Kwargs = returns always a DICTIONARY.


MORE IN THIS SECTION OF DRA. ANGELA LEE'S COURSE:
https://www.udemy.com/course/100-days-of-code/learn/lecture/20804136#overview
"""


def all_aboard(a, *args, **kwargs):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)  # important to respect the parameter positions!
# Output: 4 (7, 3, 0) {'x': 10, 'y': 64}


def example(*args, **kwargs):
    print(args, kwargs)
    for i in args:  # args come as a tuple: (something1, something2, ...)
        print(i)
    for k, v in kwargs.items():  # kwargs come as a dict: {"key1": "value1", "key2": "value2", ...}
        print(f"The {k} value is {v}.")


example(10, 20, 100, "text", name="Aldo", age=41, town="Porto Alegre")
"""Output:
    (10, 20, 100, 'text') {'name': 'Aldo', 'age': 41}
    10
    20
    100
    text
    The name value is Aldo.
    The age value is 41.
    The town value is Porto Alegre.
"""

# PACKING / UNPACKING KWARGS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Packing always as dictionary:
my_kwargs = { "name": "Aldo", "age": 41, "town": "Poa" } 

# Unpacking:
**my_kwargs  # Equivalent: name='Aldo', age=41, town='Poa'

# It's perfect to build dynamic parameters in functions/methods.