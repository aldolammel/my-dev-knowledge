#### Python > Commands
# `append()`

---

Unpacks an iterable and adds each element individually at the end of the list.

```python
my_list = [1, 2]
my_list.append([3, 4])
# Output: [1, 2, [3, 4]] (nested list)
```

To add multiple values at the same time in a list, use [extend()](/python/python-knowledge/extend.md).

---
## Examples using `append()`:

Creating a list:
```python
arrayP1 = list() # declaring list.
arrayP1.append('Aldo')
arrayP1.append(38)

# arrayP1 output: ['Aldo', 38]
```

Creating the `arrayP2` wrongly trying to copy from `arrayP1`:
```python
arrayP2 = list()
arrayP2.append(arrayP1)

# arrayP2 output: same result as arrayP1.
```

Lets modified only the `arrayP1`:
```python
arrayP1[0] = 'John'
arrayP1[1] = 19
# Output of arrayP1 modified: ['John', 19]
# Output of arrayP2 (should be the original): ['John', 19] (but accidentally modified because you tied the arrayP1 to the arrayP2 using the append!
```

Now lets copy correctly:
```python
arrayP1 = list()
arrayP1.append('Aldo')
arrayP1.append(38)

arrayP2 = list()
arrayP2.append(arrayP1[:])  # right way to copy objects from a list/array.

arrayP1[0] = 'John'
arrayP1[1] = 19

# arrayP1 output: ['John', 19]
# arrayP2 output: ['Aldo', 38]
```

Build a program to list of fat people hehe:
```python
people = list()
weights = [['Lightest', 0], ['Heaviest', 0]]
recording = list()

while True:
    recording.append(str(input('\nName: ')).strip().upper())
    recording.append(float(input('Weight: ')))

    if len(people) == 0:
        weights[0] = recording[:]
        weights[1] = recording[:]
    else:
        if recording[1] < weights[0][1]:  # checking lightest.
            weights[0] = recording[:]

        if recording[1] > weights[1][1]:  # checking heaviest.
            weights[1] = recording[:]

    people.append(recording[:])  # copying.
    recording.clear()  # cleaning for next loop.

    exit_ = str(input('Do you want to add anyone else? [Y/N]: ')).strip().upper()
    if exit_ in 'N':
        break

print(
    f'\people: {people}'
    f'\nYou got {len(people):.0f} people recorded.'
    f'\nThe heaviest person is {weights[1][0]} with {weights[1][1]:.1f}Kg.'
    f'\nThe lightest person is {weights[0][0]} with {weights[0][1]:.1f}Kg.'
)
```

Build a program able to receive 7 integers and put them within an array where others two arrays dwell: one for even numbers and another for odd numbers:
```python
array_ = [[], []]

for _ in range(1, 8):
    int_ = int(input(f'Type an integer: '))
    if int_ % 2 == 0:
        array_[0].append(int_)
    else:
        array_[1].append(int_)
    print(f'Current: {array_}\n')

array_[0].sort()
array_[1].sort()

print(
    f'\nEven numbers only: {array_[0]}'
    f'\nOdd numbers only: {array_[1]}'
)
```

Build a 3x3 matrix:
```python
row_ = []
matrix = []

for _ in range(3):
    for _ in range(3):
        input_ = int(input('Type an integer: '))
        row_.append(input_)

    matrix.append(row_[:])
    row_.clear()

print(
    f'\n[{matrix[0][0]:^8}] [{matrix[0][1]:^8}] [{matrix[0][2]:^8}]'
    f'\n[{matrix[1][0]:^8}] [{matrix[1][1]:^8}] [{matrix[1][2]:^8}]'
    f'\n[{matrix[2][0]:^8}] [{matrix[2][1]:^8}] [{matrix[2][2]:^8}]'
)
```

xxxxxxxxxxxxxxxxxxxxxxxxxxx
```python

```

xxxxxxxxxxxxxxxx
```python

```


```python
# ARRAY PART (2/2)

from time import sleep
from random import randint




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


```