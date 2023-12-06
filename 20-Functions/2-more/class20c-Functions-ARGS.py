"""

FUNCTIONS: *ARGS ARGUMENTS
(Funções: Argumentos não-nomeados):

Unpacking in Python refers to an operation that consists of assigning an iterable of values to a tuple (or list) of
variables in a single assignment statement. As a complement, the term packing can be used when we collect several
values in a single variable using the iterable unpacking operator, *.

By convention, it is called "*args".

The type of args always is a tuple.

"""

from time import sleep
from random import randint

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'

# Pre-lessons:


def fnc_counter(*args):
    print(f'They are {len(args)} numbers and here they go: {args}. The sum of them is {sum(args)}.')


fnc_counter(1, 2, 3, 4)
fnc_counter(23, 25)
fnc_counter(10, 12, 20, 22, 1, 1, 1, 10, 1)

print('\n - - - \n')


def fnc_double(_array):                   # function that duplicate each value into an array/list.
    _pos = 0
    while _pos < len(_array):
        _array[_pos] *= 2
        _pos += 1


_arrayValues = [6, 3, 9, 1, 0, 2]
print(f'Original values.......... = {_arrayValues}')
fnc_double(_arrayValues)
print(f'Duplicate original values = {_arrayValues}')

print('\n - - - \n')


def fnc_another_sum(*args):                      # unpacking method example.
    soma = 0
    for number in args:
        soma += number
    print(f'The sum of {args} = {soma}')


fnc_another_sum(2, 2, 2, 1)
fnc_another_sum(70, 3)

# ----------------------------------------
# LESSON 096:

print('\n\nLesson 096 >> Build a program able to tell a rectangle area when you set its width and length:\n')


def fnc_area(_width, _length):
    _area = _width * _length
    print(f'The rectangle area (width {_width:.2f} X {_length:.2f} length) = {_corT}{_area:.2f}m²{_corOut}.')


print('- - - - - Terrain control - - - - -')
_userWidth = float(input('Terrain\'s width (in meters): '))
_userLength = float(input('Terrain\'s length (in meters): '))

fnc_area(_userWidth, _userLength)

# ----------------------------------------
# LESSON 097:

print('\n\nLesson 097 >> Build a program where you type a phrase and the function creates a line up and down'
      'of your phrase. The lines must fit with the phrase length:\n')


def fnc_headerTitle(_txt):
    _size = len(_txt)
    print('-' * _size)
    print(_txt)
    print('-' * _size)


_userPhrase = str(input('Type any phrase: ')).strip()
fnc_headerTitle(_userPhrase)

# ----------------------------------------
# LESSON 098:

print('\n\nLesson 098 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_counter(_start, _end, _step):
    for i in range(_start, _end + 1, _step):
        print(i, end=' ')
        sleep(0.25)
    print(f'\n{_corT}The counting has been finished!{_corOut}')


_userStarts = int(input('Start integer (e.g. 1): '))
_userEnds = int(input('End integer (e.g. 10): '))
_userSteps = int(input('Step integer (e.g. 1): '))

fnc_counter(_userStarts, _userEnds, _userSteps)

# ----------------------------------------
# LESSON 099:

print('\n\nLesson 099 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_biggest(* _numbers):                  # '* variable' = unpacking parameters.
    _biggest = 0

    print(
        f'Analysing:'
        f'\n{"- " * 30}'
    )

    for _i in _numbers:
        if _i == 0:
            _biggest = _i
        elif _i > _biggest:
            _biggest = _i
        sleep(0.25)
        print(f'{_corT}{_i}{_corOut}', end=' ')

    print(
        f'| Done!'
        f'\nThe biggest number of those is {_corT}{_biggest}{_corOut}.'
        f'\n{"- " * 30}\n'
    )


fnc_biggest(2, 5, 1, 23, 102, 4, 58)
fnc_biggest(5, 1, 0, 8)
fnc_biggest(6)
fnc_biggest()

# ----------------------------------------
# LESSON 100:

print('\n\nLesson 100 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_drawNumbers(_array):
    for _i in range(5):
        _numb = randint(0, 100)
        _array.append(_numb)
    print(f'{_corT}{_array}{_corOut}')


def fnc_sumOnlyEven(_array):
    _evenNumbers = list()
    for _i in _array:
        if _i % 2 == 0:
            _evenNumbers.append(_i)
    _sumOnlyEven = sum(_evenNumbers)
    print(f'Only even numbers from _numbers array: {_corT}{_evenNumbers}{_corOut}')
    print(f'Sum of even numbers: {_corT}{_sumOnlyEven}{_corOut}')


_myNumbers = list()
fnc_drawNumbers(_myNumbers)
fnc_sumOnlyEven(_myNumbers)
