"""
    BOOLEAN VARIABLES:
    True or false values.
"""

trueNum = 5
userNum = int(input('Integer number (5 = true): '))

# Clever and simpler solution:
result1 = trueNum == userNum
print(f'SOLUTION 1 >> You got it right: {result1}.')

# Conditional solution:
result2 = False
if userNum == trueNum:
    result2 = True
print(f'SOLUTION 2 >> You got it right: {result2}.')

print('\n- - - -\n')
# ------------------------------------------------------

userAge = int(input('Your age: '))
isYoungAdult = userAge >= 18 and userAge <= 25
print(f'You are a young adult: {isYoungAdult}')

print('\n- - - -\n')
# ------------------------------------------------------

"""
-OR- OPERATOR:
One -OR- another boolean command.

"""

name = ''                                    # for boolean, it (emptiness) means False.
surname = 'Lammel'                           # if there is a value, so it is True.

greeting = name or f'Mr. {surname}'        # as name will be False (empty), the surname will be used in this case.
print(greeting)

print('\n- - - -\n')
# ------------------------------------------------------

"""
-NOT- OPERATOR:
It gives you the opposite meaning where "not False" means "True" as "not True" means "False". 

"""

print(not False)                              # means the same of 'print(True)'
