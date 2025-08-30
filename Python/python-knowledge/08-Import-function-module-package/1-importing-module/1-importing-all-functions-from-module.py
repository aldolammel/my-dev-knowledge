"""
INTRODUCTION TO IMPORT FUNCTION


"""

import math  # like this, we'll import all math library.

n = int(input('Type a number: '))
sqrt = math.sqrt(n)
print(f'The square root of {n} is {math.ceil(sqrt)} when rounded up.')
print(f'The square root of {n} is {math.floor(sqrt)} when rounded down.')
print(f'But the real square root of {n} is {sqrt:.2f}.')
