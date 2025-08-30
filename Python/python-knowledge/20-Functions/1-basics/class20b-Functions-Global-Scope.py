"""

FUNCTIONS: GLOBAL SCOPE

"""


# Behavior of "enemies" variables when in and out of a function:
enemies_a = 1


def adding_enemies_a():
    enemies_a = 2
    print(f'enemies_a INSIDE function: {enemies_a}')


adding_enemies_a()
print(f'enemies_a OUTSIDE function: {enemies_a}')


print('\n- - - -\n')

# Now the function adding enemies properly:
enemies_b = 1


def adding_enemies_b():
    global enemies_b                           # creating the reference that the object is global (from out of the fnc).
    enemies_b = 2
    print(f'enemies_b INSIDE function: {enemies_b}')


adding_enemies_b()
print(f'enemies_b OUTSIDE function: {enemies_b}')
