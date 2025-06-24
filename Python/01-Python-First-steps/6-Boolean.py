"""
BOOLEAN VARIABLES:
True or false values.

"""

_trueNum = 5
_userNum = int(input('Integer number (5 = true): '))

# Clever and simpler solution:
_result1 = _trueNum == _userNum
print(f'SOLUTION 1 >> You got it right: {_result1}.')

# Conditional solution:
_result2 = False
if _userNum == _trueNum:
    _result2 = True
print(f'SOLUTION 2 >> You got it right: {_result2}.')

print('\n- - - -\n')
# ------------------------------------------------------

_userAge = int(input('Your age: '))
_isYoungAdult = _userAge >= 18 and _userAge <= 25
print(f'You are a young adult: {_isYoungAdult}')

print('\n- - - -\n')
# ------------------------------------------------------

"""
-OR- OPERATOR:
One -OR- another boolean command.

"""

_name = ''                                    # for boolean, it (emptiness) means False.
_surname = 'Lammel'                           # if there is a value, so it is True.

_greeting = _name or f'Mr. {_surname}'        # as _name will be False (empty), the _surname will be used in this case.
print(_greeting)

print('\n- - - -\n')
# ------------------------------------------------------

"""
-NOT- OPERATOR:
It gives you the opposite meaning where "not False" means "True" as "not True" means "False". 

"""

print(not False)                              # means the same of 'print(True)'
