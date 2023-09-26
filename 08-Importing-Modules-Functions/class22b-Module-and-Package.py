"""

MODULE AND PACKAGE (Módulos e Pacotes):
Packages on Python is the same of libraries in other languages.

"""

from utilitiesClasses import currency, data                           # importing my functions from another file.

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'

# ----------------------------------------
# LESSON 111:

print('\n\nLesson 111 >> Build a program xxxxxxxxxxxxxx:\n')

_userPrice = float(input('Type a price: R$'))

currency.fnc_resume(_userPrice, 30)

# ----------------------------------------
# LESSON 112:

print('\n\nLesson 112 >> Build a program xxxxxxxxxxxxxx:\n')

_userPrice = data.fnc_moneyRead('Type a price: R$')
currency.fnc_resume(_userPrice, 10)
