
"""
    PYTHON > COMPREHENSIONS: SET COMPREHENRION

    >> What is set:
        ./set.py
    
    >> What is Python Comprehension:
        ./comprehension.txt

    Syntax with no conditional:
        my_set = { <code to create my_set> for i in a_container }
    Systax with conditional:
        my_set = { <code to create my_set> for i in a_container if <conditional> }
    
    - - - 

    >> List Comprehension:
        ./list-comprehension.py

    >> Dict Comprehension:
        ./dict-comprehension.py
"""

numbers = [1, 2, 3, 4, 5, 1, 2, 3]  # Has duplicates
squares = {x**2 for x in numbers}
print(squares)  # Output: {1, 4, 9, 16, 25}