# INTRODUCTION TO IMPORT FUNCTION:

# import math                                   # like this, we'll import all math library.

# or, to be specific, we may use only:
from math import ceil, floor

_numb = int(input('Type a number: '))
_mySqrt = math.sqrt(_numb)
print(f'The square root of {_numb} is {ceil(_mySqrt)} when rounded up.')
print(f'The square root of {_numb} is {floor(_mySqrt)} when rounded down.')
print(f'But the real square root of {_numb} is {_mySqrt:.2f}.')
