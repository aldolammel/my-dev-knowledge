"""
    PYTHON: UNPACKING
    
    Unpacking allows you to assign elements of a collection (like a list or tuple) to multiple 
    variables in a single statement.
"""

# Function returns a TUPLE:
def get_user_data():
    return "John", 30, True

# Unpack the returned values
name, age, is_active = get_user_data()
print(name)        # "John"
print(age)         # 30
print(is_active)   # True