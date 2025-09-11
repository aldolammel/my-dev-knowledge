"""
    HANDLING THE INTEGER NUMBERS:
    Integer numbers are all numbers (including the negative ones) with no dots or commas.

    3 = integer number
    '3' = string number (because the '')
    3.1 = float number.
    int('3') = integer number (because I am converting the string to int.

"""

numb1 = int(input('Type a number: '))
numb2 = int(input('Type another number: '))

thisSum = numb1 + numb2

print('The sum between', numb1, 'and', numb2, 'is', thisSum)                         # old way, with no masks.
print('The sum between {} and {} is {}'.format(numb1, numb2, thisSum))               # new way from python 3.
print(f'The sum between {numb1} and {numb2} is {thisSum}')                           # very new way from python 3.9.4

print('\n- - - - -\n')

# -----------------------------------------------

# FAKE INTEGER:

_userString = str(input('Type an integer number (e.g. 20): '))                # setting the number as a string (str).
print(_userString, ' = ', type(_userString))                                  # proofing the 'number' is a string.

# INTEGER:

_userInteger = int(input('Type another integer number: '))                    # setting the number as an integer (int).
print(_userInteger, ' = ', type(_userInteger))                                # proofing the number is an integer.

# CONVERTING a string in an integer:

_userStringAgain = str(input('Type one more integer: '))                      # setting the number as a string...
_userStringAgain = int(_userStringAgain)                                      # but here converting it to integer.
print(_userStringAgain, ' = ', type(_userStringAgain))                        # proofing the number is an integer.
