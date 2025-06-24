"""

MODULE AND PACKAGE (Módulos e Pacotes):
Packages on Python is the same of libraries in other languages.

"""

import module_example  # importing functions. Name should be snake_case.

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'

# Pre-lessons:

user_n = int(input('Type an integer: '))
factorial = module_example.cal_factorial(user_n)
print(
    f'The factorial of {user_n} is: {factorial}'
    f'\nThe double of {user_n} is: {module_example.cal_double(user_n)}'
    f'\nThe triple of {user_n} is: {module_example.cal_triple(user_n)}'
)

# ----------------------------------------
# LESSON 107 + 108 + 109:

user_p = float(input('Type a price: R$'))

module_example.resume(user_p, 30)
