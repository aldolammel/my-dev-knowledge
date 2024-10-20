"""
INTRODUCTION TO IMPORT FUNCTION


"""

from math import sqrt, ceil, floor  # To be specific, we may use only.

n = int(input('Type a number: '))
sqrt = sqrt(n)
print(f'The square root of {n} is {ceil(sqrt)} when rounded up.')
print(f'The square root of {n} is {floor(sqrt)} when rounded down.')
print(f'But the real square root of {n} is {sqrt:.2f}.')
