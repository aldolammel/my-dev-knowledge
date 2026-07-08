# VARIABLE'S BASIC WITH ARRAY/LIST INTRODUCTION

import math
import random


# CHALLENGE 016
print('016 >> Build a program able to read a rational (float) number and convert it to integer:\n')
rational_n = float(input('Type a rational number, for example, 4.94 or 37.0325545: '))
print(f'Your rational number is {rational_n} and it converted to integer is {math.trunc(rational_n)}.')

# CHALLENGE 017
print('\n\n017 >> This program must read the length of the opposite and adjacent sides of a right triangle.\n',
      'Calc it and show the hypotenuse length:\n')
opp_side = float(input('Give us a number for the opposite side: '))
adj_side = float(input('Give us a different number, but now for the adjacent side: '))
print(f'If the opposite side is {opp_side} and the adjacent side is {adj_side},\n',
      f'our hypotenuse length is {math.hypot(opp_side, adj_side)}.')

# CHALLENGE 018
# preguiça...

# CHALLENGE 019
print('\n\n019 >> Make a random select through four option names:\n')
name1 = str(input('Type a name: '))
name2 = str(input('Another one, please: '))
name3 = str(input('A third name: '))
name4 = str(input('And one more: '))
random_choice = [name1, name2, name3, name4]
print(f'The random function chose {random.choice(random_choice)}.')

# CHALLENGE 020
print('\n\n020 >> Give me four names and I will bring them back in another queue for you:\n')
n1 = str(input('First name: '))
n2 = str(input('Second name: '))
n3 = str(input('Third one: '))
n4 = str(input('Fourth name: '))
nomes = [n1, n2, n3, n4]
random.shuffle(nomes)
print('So, I wanna a queue exactly in this order:')    # apparently, if used array, it's not recommended to use format{}
print(nomes)

# Reversing the original list:
# Slicing method:
to_reserve = ["A", "B", "C", "D", "E"]
for i in to_reserve[::-1]:
    print(i, end=" ")
