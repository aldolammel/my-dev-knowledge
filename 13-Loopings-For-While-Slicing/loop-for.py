"""
-FOR-, A LIMITED LOOPING STRUCTURE:
FOR is a looping structure that it allows us to execute a command over and over again
until it's met a defined number of times.

Syntax:
for _each in _myList:
    <action or condition>

"""

from time import sleep
from datetime import date

# My colors:
_corF = '\033[1;31m'
_corT = '\033[1;32m'
_corOut = '\033[m'

# Counting from 0 to 10:
for _i in range(0, 11):
    print(_i, end=' ')
print('\nEnd\n')

# Counting from 10 to 0:
for _i in range(10, 0, -1):                                                     # this '-1' represents reverse counting.
    print(_i, end=' ')                                # this "end =''" makes the iteration put each object side-by-side.
print('\nEnd\n')

# Counting with no odd numbers:
for _i in range(0, 11, 2):                                   # this '2' represents the frequency of the missing numbers.
    print(_i, end=' ')
print('\nEnd\n')

# Counting with no even numbers:
for _i in range(1, 11, 2):                     # the same of above, '2' represents the frequency of the missing numbers.
    print(_i, end=' ')
print('\nEnd\n')

# Reading by reverse (slicing method):
listToReserve = ["A", "B", "C", "D", "E"]
for i in listToReserve[::-1]:
    print(i, end=" ")
print('\nEnd.\n')

# Counting dynamically:
_start = int(input('Gimme a start integer: '))
_end = int(input('Gimme a number bigger than the last one: '))
_step = int(input('Gimme the number 1 or 2 or 3 for example: '))

for _i in range(_start, _end + 1, _step):
    print(_i, end=' ')
print('\nEnd.\n')

print('\n- - - -\n')

# --------------------------------------------------

"""

BREAK and CONTINUE features:
BREAK stops absolutely the -for- looping.
CONTINUE skip the current repetition, starting the next one in the same -for-.

"""

# BREAK example:
# lets break this -for- before the looping reach the 10th looping time.
for _i in range(10):
    if _i == 5:
        print('Breaking now!')
        break
    print(_i, end=' ')
print('You are out of the -FOR- looping.')

print('\n- - - -\n')

# CONTINUE example:
# with this feature we can skip a repetition to the next one.
for _i in range(10):
    if _i != 5:
        print(_i, end=' ')
    else:
        continue
print('Done, where the number 5 is NOT present \'cause it was skipped with -continue- feature!')

print('\n- - - -\n')

# --------------------------------------------------

"""
ELSE with FOR:
A good way to save lots of code lines.
Important: the -else- only runs the -for- runs completely, with no breaks.  

"""
_cars = ['Ok', 'Ok', 'Ok', 'Ok', 'Ok']           # Try to change a car status to 'Not ok', for example.
for _carStatus in _cars:
    print(f'This car is:', end=' ')
    if _carStatus == 'Ok':
        print(_carStatus)
        print('Shipping the car to customer.\n')
    else:
        print(_carStatus)
        print('Stopping the production line...\n')
        break
else:                                            # using ELSE with FOR can save a lot of code lines ;)
    print('All cars are done.')                  # if one or more cars are 'Not ok', this phrase will never be seen.

print('\n- - - -\n')

_userPrimeNum = int(input('Lets find out the prime numbers by the number (e.g. 30): '))

for _num in range(2, _userPrimeNum + 1):
    for _x in range(2, _num):
        if _num % _x == 0:
            print(f'{_num} equals {_x} * {_num // _x}')
            break
    else:
        print(f'{_num} is a prime number.')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 046:

print('\n\nLesson 046 >> Here our fireworks countdown go:\n')

for _i in range(10, 0, -1):
    print(_i, end=' ')
    sleep(1)
print('\nUhu, fireworks!')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 047:

print('\n\nLesson 047 >> Here\'s all EVEN numbers from 1 to 50:\n')

for _i in range(2, 51, 2):
    print(_i, end=' ')
print('\nEnd.\n')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 048:

print('\nLesson 048 >> Show me the SUM among ALL ODD numbers MULTIPLES OF 3 from 0 to 500:\n')

_sum = 0
_count = 0

for _i in range(1, 501, 2):       # bringing only odd numbers.
    if _i % 3 == 0:               # if the number is divisible by 3 and its module is equal to zero, then...
        _count = _count + 1       # counting how many numbers it is counting.
        _sum = _sum + _i          # summing all the numbers found.

print(f'The sum of {_count} odd numbers multiples of 3 found from 0 to 500 is: {_sum}')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 049:

_tableNumber = int(input('\n\nType an integer to find its multiplication table: '))

for _i in range(1, 11):
    print(f'{_tableNumber} x {_i} = {_tableNumber * _i}')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 050:

print('\n\nLesson 050 >> Ask seven times an integer and sum all of even numbers only:\n')

_sum = 0

for _i in range(1, 7):

    _userChoice = int(input('Type an integer: '))

    if _userChoice % 2 == 0:
        _sum = _sum + _userChoice

print(f'\nThe sum of all entered even numbers is: {_corT}{_sum}{_corOut}.')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 051:

print('\n\nLesson 051 >> Let\'s built an Arithmetic Progression with 10 numbers, '
      'it doesnt matter the integer inputted:\n')

_startAP = int(input('A first term (e.g. 20): '))
_razaoAP = int(input('"razão" number (e.g. 5): '))
_tenTerm = _startAP + (10 - 1) * _razaoAP

for _x in range(_startAP, _tenTerm + _razaoAP, _razaoAP):
    print(_x, end=' >> ')
print('Done!')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 052:

print('\n\nLesson 052 >> A natural number is prime if it has only two distinct positive divisors.',
      ' That is, a natural number is prime if it\'s greater than 1 and divisible (%) only by itself and 1:\n')

_myNumber = int(input('Type an integer: '))

if _myNumber > 0:

    _divisibleTimes = 0
    print(f'\n{_corT}Yellow numbers{_corOut} are those can divide {_myNumber}:')

    for _i in range(1, _myNumber + 1):
        if _myNumber % _i == 0:
            print(f'{_corT}33m', end='')
            _divisibleTimes += 1                                # same of "_obj = _obj + 1"
        else:
            print(f'{_corOut}', end='')
        print(_i, end=' ')

    print(f'\n\n{_corOut}Your choice was divisible {_divisibleTimes} times, then', end=' ')

    if _divisibleTimes == 2:
        print(f'{_corT}{_myNumber} is a prime number!{_corOut}')
    else:
        print(f'{_corF}{_myNumber}',
              f'is NOT a prime number! Prime number is divided twice (by itself and by 1).{_corOut}')

else:
    print(f'\n{_corF}Prime number never is a negative one!{_corOut}')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 053:

print('\n\nLesson 053 >> Tell me if a typed phrase is a palindrome or not:\n')

_isPalindrome = str(input('Type a phrase: ')).strip().upper()

# Palindrome example (en): Now sir a war is won
# Palindrome example (pt): Amor a roma

_arrayWords53 = _isPalindrome.split()
_noSpaces = ''.join(_arrayWords53)

# -SLICING- SOLUTION STARTS:
_reverse = _noSpaces[::-1]
# -SLICING- SOLUTION ENDS.

# -FOR- SOLUTION STARTS:
'''_reverse = ''
for _i in range(len(_noSpaces) - 1, -1, -1):
    _reverse = _reverse + _noSpaces[_i]'''
# -FOR- SOLUTION ENDS.

print(f'\n{_noSpaces}  >>>  {_reverse}')
if _reverse == _noSpaces:
    print(f'{_corT}Your phrase is a palindrome!{_corOut}')
else:
    print(f'{_corF}Your phrase is NOT a palindrome!{_corOut}')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 054:

print('\n\nLesson 054 >> How much people are adults and how much are just kids:\n')

_yearsAdults = 0
_yearsKids = 0

for _i in range(1, 8):
    _yearB = int(input(f'In what year was the number {_i} person born? '))

    if _yearB <= (date.today().year - 18):
        _yearsAdults = _yearsAdults + 1
    else:
        _yearsKids = _yearsKids + 1

print(f'\n{_corT}{_yearsAdults}{_corOut} already reached the majority. / ',
      f'{_corF}{_yearsKids}{_corOut} are kids.\n')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 055 SOLUTION WITH -IF-:

print('\n\nLesson 055 (with IF solution) >> Which person of five is the heaviest and the lightest one. E.g.: 98.4\n')

_heaviestPerson = 0
_lightestPerson = 0

for _i in range(1, 6):

    _weight = float(input(f'Type the weight of the person number {_i} in Kg: '))

    if _i == 1:               # if the first entry in the counting, that weight is the top and bottom in the same time.
        _heaviestPerson = _weight
        _lightestPerson = _weight
    if _weight > _heaviestPerson:
        _heaviestPerson = _weight
    if _weight < _lightestPerson:
        _lightestPerson = _weight

print(f' \nThe heaviest person ever weighs {_corT}{_heaviestPerson:.1f}Kg{_corOut}.',
      f'The lightest person ever weighs {_corT}{_lightestPerson:.1f}Kg{_corOut}.')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 055 SOLUTION WITH ARRAY:

print('\n\nLesson 055 (with ARRAY solution) >> Which person of five is the heaviest and the lightest one. E.g.: 98.4\n')

_weightsArray = []

for _i in range(1, 6):

    _weight = float(input(f'Type the weight of the person number {_i} in Kg: '))

    _weightsArray = _weightsArray + [_weight]

print(f' \nThe heaviest person ever weighs {_corT}{max(_weightsArray):.1f}Kg{_corOut}.',
      f'The lightest person ever weighs {_corT}{min(_weightsArray):.1f}Kg{_corOut}.')

print('\n- - - -\n')

# --------------------------------------------------
# LESSON 056:
# Important: if two (or more) oldest men have the same age, the result will be the first oldest man inserted in the
# program. I am too lazy this morning to fix that :)

print('\n\nLesson 056 >> Show a people analyses with names, ages and genders:\n')

_ageAverage = 0
_oldestMaleAge = 0
_oldestMaleName = ''
_femalesAmount = 0

for _i in range(1, 5):

    print(('-' * 10), 'Person', _i, ('-' * 10))

    _name56 = str(input('Type a name: ')).strip().upper()
    _age56 = int(input('Type an age: '))
    _gender56 = str(input('M for male / F for female: ')).strip().upper()

    # counting the age average:
    _ageAverage = _ageAverage + _age56

    # checking who is the oldest male:
    if _gender56 == 'M':

        if _i == 1:
            _oldestMaleName = _name56
            _oldestMaleAge = _age56

        elif _age56 > _oldestMaleAge:
            _oldestMaleName = _name56
            _oldestMaleAge = _age56

    # checking females' amount:
    elif _age56 < 20:
        _femalesAmount = _femalesAmount + 1

    print('')

print(f'The average age of the group is {_corT}{_ageAverage / 4} years{_corOut}.'
      f'\nThe oldest male has {_corT}{_oldestMaleAge} years{_corOut} and his name is '
      f'{_corT}{_oldestMaleName}{_corOut}.'
      f'\n{_corT}{_femalesAmount}{_corOut} women have less than 20 years old.')
