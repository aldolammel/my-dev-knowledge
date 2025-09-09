"""
TYPE ANNOTATIONS / DATA HINT DECLARATIONS

    Concept: /Programming-Concepts/type-annotation.txt

    Types in Python:
        integer = int
        float = float
        string = str
        boolean = bool
        object = object
        anything = any
        containers = list, tuple, set, dict
"""

# simplest example of object data type declaration:
age: int
height: float
lastname: str
is_adult: bool
user: object
date: str
car: list
store: dict
final_score: tuple


# Without Type Annotations:

num = 10
name = 'Aldo'
data = {'vini': 1, 'azevedo': 2}

def get_something():
    return {'abc': 1, 'def': 2}

# With Type Annotations:

num: int = 10
name: str = 'Aldo'
data: dict[str, int] = {'vini': 1, 'azevedo': 2}

def get_something() -> dict[str, int]:
    return {'abc': 1, 'def': 2}

def greet_people(people: list[str]) -> None:
    for person in people:
        print(f'Hello, {person}!')