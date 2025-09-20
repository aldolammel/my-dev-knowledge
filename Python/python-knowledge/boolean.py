"""
    VARIABLE: BOOLEAN

"""

# Example 1: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
obj_id = 1
is_there_obj = False

if obj_id:
    is_there_obj = True

print(f"Is there object: {is_there_obj}")


# Example 2: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
obj_id = 1

is_there_obj = True if obj_id else False

print(f"Is there object: {is_there_obj}")


# Example 3: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
obj_id = 1

is_there_obj = not obj_id

print(f"Is there object: {is_there_obj}")


# Example 4: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
obj_id = 1

print(f"Is there object: {not obj_id}")