"""
INTRODUCTION TO IMPORT FUNCTION


"""

from math import sqrt, ceil, floor                                                    # To be specific, we may use only.

_numb = int(input('Type a number: '))
_mySqrt = sqrt(_numb)
print(f'The square root of {_numb} is {ceil(_mySqrt)} when rounded up.')
print(f'The square root of {_numb} is {floor(_mySqrt)} when rounded down.')
print(f'But the real square root of {_numb} is {_mySqrt:.2f}.')
