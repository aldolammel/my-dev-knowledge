# CONDITIONS / CONDIÇÔES

# Basic imports:
from random import randrange

# My colors:
_corIn = '\033[1;33m'
_corOut = '\033[m'

# Pre-lessons:

_degree1 = float(input('Type the first degree: '))
_degree2 = float(input('Type the second degree: '))
_result = (_degree1 + _degree2) / 2

if _result >= 7.0:
    print(f'Your average degree is {_corIn}{_result:.1f}{_corOut}. Congrats!')
else:
    print(f'What a shame, your average degree is {_corIn}{_result:.1f}{_corOut}.')
print('\nSee you in the next semester.')

# --------------------------------------------------
# LESSON 028

print('\n\nLesson 028 >> Write a program that it picks up a number between 0 and 5 and ask the user to play,'
      'giving a guess. If the user wins, a winning message, otherwise, a losing message:\n')

_guessNumb = int(input('Hey, kid, gimme an integer between 0 and 5: '))
_aiChoice = randrange(5)
if _guessNumb != _aiChoice:
    print(f'\nYOU\'RE SO LOSER! I chose {_corIn}{_aiChoice}{_corOut}, hehe...')
else:
    print('\nHm, good!')

# --------------------------------------------------
# LESSON 029

print('\n\nLesson 029 >> Build a program allowed to identify the car velocity and apply R$7 as fine by each 1km/h'
      'the car has crossed the 80Km/hour threshold:\n')
_carSpeed = int(input('Tell me the car velocity (only integer): '))
_speedLimit = 80
if _carSpeed > _speedLimit:
    _fine = (_carSpeed - _speedLimit) * 7
    print(f'This road has {_speedLimit}Km/h as limit and you\'ve crossed that velocity.\n'
          f'Here\'s the fine: {_corIn}R${float(_fine):.2f}{_corOut}.')
else:
    print('You\'re good, sir. Drive safe!')

# --------------------------------------------------
# LESSON 030

print('\n\nLesson 030 >> Build an app capable to read a integer and shows it up on screen if it is even or odd:\n')
_evenOrOdd = int(input('Type an integer, please: '))
_checkingEven = _evenOrOdd % 2      # even numbers divided by 2 has its module (%) equal zero. Otherwise, if 1, odd.

print(f'\nAs your number module is {_checkingEven}:')

if _checkingEven == 0:
    print(f'Then your number is {_corIn}EVEN{_corOut}!')
else:
    print(f'So your number is {_corIn}ODD{_corOut}! :)')

# --------------------------------------------------
# LESSON 031

print('\n\nLesson 031 >> Develop a program that ask a bus trip distance in Km and, after that,'
      ' calc the ticket price where R$0,50 to each km by 200Km trips, and R$0,45 to longer ones:\n')

_tripDistance = int(input('How long is your bus trip in Km? Please, use only integer. Km: '))
_regularCost = 0.5
_lowCost = 0.45

if _tripDistance <= 200:
    _ticketPrice = _tripDistance * _regularCost
    print('\n')
else:
    _ticketPrice = _tripDistance * _lowCost
    print('\nCongrats! You\'re traveling with discount:')

print(f'You pay {_corIn}R${_ticketPrice:.2f}{_corOut} per ticket.')

# --------------------------------------------------
# LESSON 032

print('\n\nLesson 032 >> Build a software able to read any year and return if it is a leap year:\n')

_year = int(input('Type a year with 4 digits: '))

if _year % 4 == 0 and _year % 100 != 0 or _year % 400 == 0:
    print(f'\nIt {_corIn}IS{_corOut} a leap year!')
else:
    print(f'\nIt is {_corIn}NOT{_corOut} a leap year.')

# --------------------------------------------------
# LESSON 033

print('\n\nLesson 033 >> Build a program that read three different numbers and shows which of them is the greater and'
      'the smaller:\n')

_numb1 = int(input('Type an integer: '))
_numb2 = int(input('Another one: '))
_numb3 = int(input('One more: '))
print('\n')

_array = [_numb1, _numb2, _numb3]
_arraySorted = sorted(_array)

print(f'Greatest number is {_corIn}{_arraySorted[2]}{_corOut}.')
print(f'Smallest number is {_corIn}{_arraySorted[0]}{_corOut}.')

# --------------------------------------------------
# LESSON 034

print('\n\nLesson 034 >> Build a program that calculates the salary increase based on the earns range:\n')
_userEarn = float(input('Type a salary in R$: '))
_range = 1250
_hiEarn = 10
_loEarn = 15

if _userEarn < _range:
    print(f'\nSalary increase {_corIn}{_loEarn}%{_corOut}, from R${_userEarn:.2f} to'
          f' {_corIn}R${_userEarn + ((_userEarn / 100) * _loEarn):.2f}{_corOut}.')
else:
    print(f'\nSalary increase {_corIn}{_hiEarn}%{_corOut}, from R${_userEarn:.2f} to'
          f' {_corIn}R${_userEarn + ((_userEarn / 100) * _hiEarn):.2f}{_corOut}.')

# --------------------------------------------------
# LESSON 035

print('\n\nLesson 035 >> Develop a program able to read three lengths and return if them can build a triangle:\n')
_length1 = float(input('Gimme a length in only with numbers: '))
_length2 = float(input('Another one: '))
_length3 = float(input('And the last one: '))
_triangle = _length1 < _length2 + _length3 and _length2 < _length1 + _length3 and _length3 < _length1 + _length2

if _triangle:
    print(f'Yeah! {_corIn}You got{_corOut} a triangle!')
else:
    print(f'Those number {_corIn}can\'t{_corOut} build a triangle. Try again!')
