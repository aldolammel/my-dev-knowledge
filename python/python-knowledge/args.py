

"""
FUNCTIONS: *ARGS ARGUMENTS
(Funções: Argumentos não-nomeados):

Unpacking in Python refers to an operation that consists of assigning an iterable of values to a tuple (or list) of variables in a single assignment statement. As a complement, the term packing can be used when we collect several values in a single variable using the iterable unpacking operator, *.

By convention, it is called "*args".

- args = returns always a TUPLE.
- Kwargs = returns always a DICTIONARY (more about: ./kwargs.py)

MORE IN THIS SECTION OF DRA. ANGELA LEE'S COURSE:
https://www.udemy.com/course/100-days-of-code/learn/lecture/20804136#overview

"""

from time import sleep
from random import randint

# MY COLORS
c_succ = '\033[1;32m'
c_fail = '\033[1;31m'
c_end = '\033[m'

# Pre-lessons:


def fnc_counter(*args):
    print(f'They are {len(args)} numbers and here they go: {args}. The sum of them is {sum(args)}.')


fnc_counter(1, 2, 3, 4)
fnc_counter(23, 25)
fnc_counter(10, 12, 20, 22, 1, 1, 1, 10, 1)

print('\n - - - \n')


def fnc_double(array):                   # function that duplicate each value into an array/list.
    pos = 0
    while pos < len(array):
        array[pos] *= 2
        pos += 1


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
    print(f'The rectangle area (width {_width:.2f} X {_length:.2f} length) = {c_succ}{_area:.2f}m²{c_end}.')


print('- - - - - Terrain control - - - - -')
_userWidth = float(input('Terrain\'s width (in meters): '))
_userLength = float(input('Terrain\'s length (in meters): '))

fnc_area(_userWidth, _userLength)

# ----------------------------------------
# LESSON 097:

print('\n\nLesson 097 >> Build a program where you type a phrase and the function creates a line up and down'
      'of your phrase. The lines must fit with the phrase length:\n')


def fnc_headerTitle(txt):
    size = len(txt)
    print('-' * size)
    print(txt)
    print('-' * size)


user_sentence = str(input('Type any phrase: ')).strip()
fnc_headerTitle(user_sentence)

# ----------------------------------------
# LESSON 098:

print('\n\nLesson 098 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_counter(_start, _end, _step):
    for i in range(_start, _end + 1, _step):
        print(i, end=' ')
        sleep(0.25)
    print(f'\n{c_succ}The counting has been finished!{c_end}')


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
        print(f'{c_succ}{_i}{c_end}', end=' ')

    print(
        f'| Done!'
        f'\nThe biggest number of those is {c_succ}{_biggest}{c_end}.'
        f'\n{"- " * 30}\n'
    )


fnc_biggest(2, 5, 1, 23, 102, 4, 58)
fnc_biggest(5, 1, 0, 8)
fnc_biggest(6)
fnc_biggest()

# ----------------------------------------
# LESSON 100:

print('\n\nLesson 100 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_drawNumbers(array):
    for _i in range(5):
        _numb = randint(0, 100)
        array.append(_numb)
    print(f'{c_succ}{array}{c_end}')


def fnc_sumOnlyEven(array):
    _evenNumbers = list()
    for _i in array:
        if _i % 2 == 0:
            _evenNumbers.append(_i)
    _sumOnlyEven = sum(_evenNumbers)
    print(f'Only even numbers from _numbers array: {c_succ}{_evenNumbers}{c_end}')
    print(f'Sum of even numbers: {c_succ}{_sumOnlyEven}{c_end}')


my_numbers = list()
fnc_drawNumbers(my_numbers)
fnc_sumOnlyEven(my_numbers)
