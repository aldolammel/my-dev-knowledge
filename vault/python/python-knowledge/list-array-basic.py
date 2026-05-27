# VARIABLE'S BASIC WITH ARRAY/LIST INTRODUCTION

import math
import random

# CHALLENGE 016
print('016 >> Build a program able to read a rational (float) number and convert it to integer:\n')
_rationalNumb = float(input('Type a rational number, for example, 4.94 or 37.0325545: '))
print(f'Your rational number is {_rationalNumb} and it converted to integer is {math.trunc(_rationalNumb)}.')

# CHALLENGE 017
print('\n\n017 >> This program must read the length of the opposite and adjacent sides of a right triangle.\n',
      'Calc it and show the hypotenuse length:\n')
_oppSide = float(input('Give us a number for the opposite side: '))
_adjSide = float(input('Give us a different number, but now for the adjacent side: '))
print(f'If the opposite side is {_oppSide} and the adjacent side is {_adjSide},\n',
      f'our hypotenuse length is {math.hypot(_oppSide, _adjSide)}.')

# CHALLENGE 018
# preguiça...

# CHALLENGE 019
print('\n\n019 >> Make a random select through four option names:\n')
_name1 = str(input('Type a name: '))
_name2 = str(input('Another one, please: '))
_name3 = str(input('A third name: '))
_name4 = str(input('And one more: '))
_randomChose = [_name1, _name2, _name3, _name4]
print(f'The random function chose {random.choice(_randomChose)}.')

# CHALLENGE 020
print('\n\n020 >> Give me four names and I will bring them back in another queue for you:\n')
_nome1 = str(input('First name: '))
_nome2 = str(input('Second name: '))
_nome3 = str(input('Third one: '))
_nome4 = str(input('Fourth name: '))
_arrayNames = [_nome1, _nome2, _nome3, _nome4]
random.shuffle(_arrayNames)
print('So, I wanna a queue exactly in this order:')    # apparently, if used array, it's not recommended to use format{}
print(_arrayNames)

# Reversing the original list:
# Slicing method:
listToReserve = ["A", "B", "C", "D", "E"]
for i in listToReserve[::-1]:
    print(i, end=" ")
