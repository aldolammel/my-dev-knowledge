
"""
    PYTHON > COMPREHENSIONS: DICTIONARY COMPREHENRION

    >> What is dictionary:
        ./dictionary.py
    
    >> What is Python Comprehension:
        ./comprehension.txt

    Syntax with no conditional:
        my_dict = { <code to create my_dict> for k, v in a_container.items() }
    Systax with conditional:
        my_dict = { <code to create my_dict> for k, v in a_container.items() if <conditional> }
    
    - - - 

    >> List Comprehension:
        ./list-comprehension.py

    >> Set Comprehension:
        ./set-comprehension.py
"""

# Example > Sanitizing a dictionary - - - - - - - - - - - - - - - - - - - - - - - - -

raw_dict = {
    'elm_key': '12314243',
    'elm_css': '',
    'elm_img': None,
    'elm_target': False,
}

# Removing "None" and empty string values from a dictionary:
sanitized_dict = {k: v for k, v in data.items() if v is not None and v != ""} for data in raw_dict

print(sanitized_dict)
# Output: { 'elm_key': '12314243', 'elm_target': False }
