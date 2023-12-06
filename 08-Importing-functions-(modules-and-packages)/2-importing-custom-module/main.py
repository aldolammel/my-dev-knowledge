"""

MODULE AND PACKAGE (Módulos e Pacotes):
Packages on Python is the same of libraries in other languages.

"""

import module_example                           # importing functions. Name should be all-lowercase. Can use underscore.

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'

# Pre-lessons:

_userNum = int(input('Type an integer: '))
_factorial = module_example.cal_factorial(_userNum)
print(
    f'The factorial of {_userNum} is: {_factorial}'
    f'\nThe double of {_userNum} is: {module_example.cal_double(_userNum)}'
    f'\nThe triple of {_userNum} is: {module_example.cal_triple(_userNum)}'
)

# ----------------------------------------
# LESSON 107 + 108 + 109:

print('\n\nLesson 107+108+109 >> Build a program xxxxxxxxxxxxxx:\n')

_userPrice = float(input('Type a price: R$'))

module_example.resume(_userPrice, 30)
