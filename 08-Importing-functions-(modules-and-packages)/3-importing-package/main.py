"""

MODULE AND PACKAGE (Módulos e Pacotes):
Packages on Python is the same of libraries in other languages.

"""

from myPackage import module_currency, module_data  # Unlike module, package should avoid "_" but use all-lower.

# How to call functions when it's from modules inside a package:
_userNum = int(input('Type an integer: '))
print(
    f'The factorial of {_userNum} is: {module_currency.calc_factorial(_userNum)}'
    f'\nThe double of {_userNum} is: {module_currency.calc_double(_userNum)}'
    f'\nThe triple of {_userNum} is: {module_currency.calc_triple(_userNum)}'
)

# ----------------------------------------

_userPrice = float(input('Type a price: R$'))
module_currency.resume(_userPrice, 30)

# ----------------------------------------

_userPrice = module_data.money_read('Type a price: R$')
module_currency.resume(_userPrice, 10)

# ----------------------------------------

