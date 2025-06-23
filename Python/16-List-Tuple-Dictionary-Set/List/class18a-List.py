# ARRAY PART (2/2)

from time import sleep
from random import randint

# MY COLORS
_cor = '\033[1;32m'
_corFail = '\033[1;31m'
_corOut = '\033[m'

# Pre-lessons:

# creating the _arrayP1:
_arrayP1 = list()
_arrayP1.append('Aldo')
_arrayP1.append(38)
print(f'\n_arrayP1 original: {_arrayP1}')

# creating the _arrayP2 wrongly trying to copy from _arrayP1:
_arrayP2 = list()
_arrayP2.append(_arrayP1)
print(f'\n_arrayP2 original: {_arrayP2}')

# lets modified only the _arrayP1:
_arrayP1[0] = 'John'
_arrayP1[1] = 19
print(f'\n_arrayP1 modified: {_arrayP1}')
print(f'_arrayP2 should be the original: {_arrayP2} (but accidentally modified)')

# now lets copy correctly:
_arrayP1 = list()
_arrayP1.append('Aldo')
_arrayP1.append(38)

_arrayP2 = list()
_arrayP2.append(_arrayP1[:])  # right way to copy objects from array.

_arrayP1[0] = 'John'
_arrayP1[1] = 19

print(
    f'\n_arrayP1: {_arrayP1}'
    f'\n_arrayP2: {_arrayP2}'
)

print('\n- - - -\n')

print("USING JOIN():")
_friends = ['Peter', 'Joseph', 'Nick']
_friendsFormatted = ', '.join(_friends)
print(f'Original list: {_friends}')
print(f'My friends are {_friendsFormatted}')

print('\n- - - -\n')

# ----------------------------------------
# LESSON 084:

print('\n\nLesson 084 >> Build a program xxxxxxxxxxxxxxxxx:\n:')

_people = list()
_weights = [['Lightest', 0], ['Heaviest', 0]]
_recording = list()

while True:
    _recording.append(str(input('\nName: ')).strip().upper())
    _recording.append(float(input('Weight: ')))

    if len(_people) == 0:
        _weights[0] = _recording[:]
        _weights[1] = _recording[:]
    else:
        if _recording[1] < _weights[0][1]:                  # checking lightest.
            _weights[0] = _recording[:]

        if _recording[1] > _weights[1][1]:                  # checking heaviest.
            _weights[1] = _recording[:]

    _people.append(_recording[:])                           # copying.
    _recording.clear()                                      # cleaning for next loop.

    _exit = str(input('Do you want to add anyone else? [Y/N]: ')).strip().upper()
    if _exit in 'N':
        break

print(
    f'\n_arrayPeople: {_cor}{_people}{_corOut}'
    f'\nYou got {_cor}{len(_people):.0f}{_corOut} people recorded.'
    f'\nThe heaviest person is {_cor}{_weights[1][0]}{_corOut} with {_cor}{_weights[1][1]:.1f}Kg{_corOut}.'
    f'\nThe lightest person is {_cor}{_weights[0][0]}{_corOut} with {_cor}{_weights[0][1]:.1f}Kg{_corOut}.'
)

# ----------------------------------------
# LESSON 085:

print('\n\nLesson 085 >> Build a program able to receive 7 integers and put them within an array where'
      'others two arrays dwell: one for even numbers and another for odd numbers:\n')

_array = [[], []]

for _pos in range(1, 8):

    _int = int(input(f'Type an integer: '))

    if _int % 2 == 0:
        _array[0].append(_int)
    else:
        _array[1].append(_int)

    print(f'Current: {_cor}{_array}{_corOut}\n')

_array[0].sort()
_array[1].sort()

print(
    f'\nEven numbers only: {_cor}{_array[0]}{_corOut}'
    f'\nOdd numbers only: {_cor}{_array[1]}{_corOut}'
)

# ----------------------------------------
# LESSON 086A - MY TRY

print('\n\nLesson 086 >> Build a 3x3 matrix:\n:')

_row = []
_matrix = []

for _r in range(3):

    for _c in range(3):
        _input = int(input('Type an integer: '))
        _row.append(_input)

    _matrix.append(_row[:])
    _row.clear()

print(
    f'\n[{_matrix[0][0]:^8}] [{_matrix[0][1]:^8}] [{_matrix[0][2]:^8}]'
    f'\n[{_matrix[1][0]:^8}] [{_matrix[1][1]:^8}] [{_matrix[1][2]:^8}]'
    f'\n[{_matrix[2][0]:^8}] [{_matrix[2][1]:^8}] [{_matrix[2][2]:^8}]'
)

# ----------------------------------------
# LESSON 086 - GUANABARA SOLUTION

print('\n\nLesson 086B >> Build a 3x3 matrix:\n:')

_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for _r in range(3):
    for _c in range(3):
        _matrix[_r][_c] = int(input('Type an integer: '))        # interesting solution.

for _r in range(3):
    for _c in range(3):
        print(f'[{_matrix[_r][_c]:^7}]', end='')
    print()

# ----------------------------------------
# LESSON 087:

print('\n\nLesson 087 >> Build a 3x3 matrix but with some final analyses:\n')

_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
_evenNums = 0

for _r in range(3):
    for _c in range(3):
        _matrix[_r][_c] = int(input('Type an integer: '))

        if _matrix[_r][_c] % 2 == 0:
            _evenNums += _matrix[_r][_c]

for _r in range(3):
    for _c in range(3):
        print(f'[{_matrix[_r][_c]:^7}]', end='')
    print()

print(
    f'\nSum of even: {_cor}{_evenNums}{_corOut}'
    f'\nSum in third column: {_cor}{_matrix[0][2] + _matrix[1][2] + _matrix[2][2]}{_corOut}'
    f'\nHighest in second row: {_cor}{max(_matrix[1])}{_corOut}'
)

# ----------------------------------------
# LESSON 088:

print('\n\nLesson 088 >> Build a program allowed to sweepstake six numbers by game where the numbers within never'
      'repeated themselves:\n')

_sweepstake = []
_numChecker = 0

_tries = int(input('How many sweepstakes: '))

for _t in range(1, _tries + 1):                     # tries/sweepstakes available.

    sleep(0.5)

    for _n in range(6):                             # numbers into each try.

        while True:                                 # avoiding repeatable numbers.
            _numChecker = randint(1, 60)
            if _numChecker not in _sweepstake:
                break

        _sweepstake.append(_numChecker)

    print(f'Sweepstake #{_t}: {sorted(_sweepstake)}')
    _sweepstake.clear()

print('\nGood luck!')

# ----------------------------------------
# LESSON 089:

print('\n\nLesson 08X >> Build a program xxxxxxxxxxxxxxxxx:')

_allStudents = []
_newStudent = 'Y'

while _newStudent in 'Y':
    _student = list()
    _student.append(str(input('\nName: ')).strip().upper())
    _student.append(float(input('Grade 1: ')))
    _student.append(float(input('Grade 2: ')))
    _student.append((_student[1] + _student[2]) / 2)                   # grade average.
    _allStudents.append(_student[:])
    _newStudent = str(input('Add another student [Y/N]: ')).strip().upper()

print(f'\n{str("NUM"):<6}{str("NAME"):<20}{str("AVERAGE"):>8}')
for _num, _person in enumerate(_allStudents):
    print(f'{_cor}{_num + 1:<6}{_corOut}{_allStudents[_num][0]:<20}{_allStudents[_num][3]:>8.1f}')

while True:
    _checkGrade = int(input(f'\n0 to exit or student\'s {_cor}SUMMARY NUM{_corOut} to check their grades: '))
    if _checkGrade == 0:
        break
    else:
        for _num in range(len(_allStudents) + 1):
            if _num == _checkGrade:
                print(
                    f'Grades of {_cor}{_allStudents[_num - 1][0]}{_corOut} are: '
                    f'{_cor}{_allStudents[_num - 1][1]:.1f}{_corOut} and {_cor}{_allStudents[_num - 1][2]:.1f}{_corOut}'
                )

print(f'{_corFail}\nThe program has been finished.{_corOut}')

# ----------------------------------------

