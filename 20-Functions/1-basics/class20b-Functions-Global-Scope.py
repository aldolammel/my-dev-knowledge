"""

FUNCTIONS: GLOBAL SCOPE

"""


# Behavior of _enemies object when in and out of a function:
enemiesA = 1


def adding_enemies_a():
    enemiesA = 2
    print(f'EnemiesA INSIDE function: {enemiesA}')


adding_enemies_a()
print(f'EnemiesA OUTSIDE function: {enemiesA}')


print('\n- - - -\n')

# Now the function adding enemies properly:
enemiesB = 1


def adding_enemies_b():
    global enemiesB                            # creating the reference that the object is global (from out of the fnc).
    enemiesB = 2
    print(f'EnemiesB INSIDE function: {enemiesB}')


adding_enemies_b()
print(f'EnemiesB OUTSIDE function: {enemiesB}')
