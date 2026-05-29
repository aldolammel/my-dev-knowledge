# CONDITIONS

# Basic imports:
from random import randrange

# Pre-lessons:
degree1 = float(input('Type the first degree: '))
degree2 = float(input('Type the second degree: '))
result = (degree1 + degree2) / 2

if result >= 7.0:
    print(f'Your average degree is {result:.1f}. Congrats!')
else:
    print(f'What a shame, your average degree is {result:.1f}.')
print('\nSee you in the next semester.')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print('\n\nLesson 028 >> Write a program that it picks up a number between 0 and 5 and ask the user to play,'
      'giving a guess. If the user wins, a winning message, otherwise, a losing message:\n')

guess_n = int(input('Hey, kid, gimme an integer between 0 and 5: '))
ai_choice = randrange(5)
if guess_n != ai_choice:
    print(f'\nYOU\'RE SO LOSER! I chose {ai_choice}, hehe...')
else:
    print('\nHm, good!')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print('\n\nLesson 029 >> Build a program allowed to identify the car velocity and apply R$7 as fine by each 1km/h'
      'the car has crossed the 80Km/hour threshold:\n')
c_speed = int(input('Tell me the car velocity (only integer): '))
speed_limit = 80
if c_speed > speed_limit:
    fine = (c_speed - speed_limit) * 7
    print(f'This road has {speed_limit}Km/h as limit and you\'ve crossed that velocity.\n'
          f'Here\'s the fine: R${float(fine):.2f}.')
else:
    print('You\'re good, sir. Drive safe!')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print('\n\nLesson 030 >> Build an app capable to read a integer and shows it up on screen if it is even or odd:\n')
n = int(input('Type an integer, please: '))
n_checking = n % 2      # even numbers divided by 2 has its module (%) equal zero. Otherwise, if 1, odd.

print(f'\nAs your number module is {n_checking}:')

if n_checking == 0:
    print(f'Then your number is EVEN!')
else:
    print(f'So your number is ODD! :)')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print('\n\nLesson 031 >> Develop a program that ask a bus trip distance in Km and, after that,'
      ' calc the ticket price where R$0,50 to each km by 200Km trips, and R$0,45 to longer ones:\n')

dist = int(input('How long is your bus trip in Km? Please, use only integer. Km: '))
regular_cost = 0.5
low_cost = 0.45

if dist <= 200:
    ticket_price = dist * regular_cost
    print('\n')
else:
    ticket_price = dist * low_cost
    print('\nCongrats! You\'re traveling with discount:')

print(f'You pay R${ticket_price:.2f} per ticket.')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print('\n\nLesson 032 >> Build a software able to read any year and return if it is a leap year:\n')

year = int(input('Type a year with 4 digits: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'\nIt IS a leap year!')
else:
    print(f'\nIt is NOT a leap year.')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print('\n\nLesson 033 >> Build a program that read three different numbers and shows which of them is the greater and'
      'the smaller:\n')

n1 = int(input('Type an integer: '))
n2 = int(input('Another one: '))
n3 = int(input('One more: '))
print('\n')

array = [n1, n2, n3]
array_sorted = sorted(array)

print(f'Greatest number is {array_sorted[2]}.')
print(f'Smallest number is {array_sorted[0]}.')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print('\n\nLesson 034 >> Build a program that calculates the salary increase based on the earns range:\n')
user_e = float(input('Type a salary in R$: '))
e_range = 1250
e_high = 10
e_low = 15

if user_e < e_range:
    print(f'\nSalary increase {e_low}%, from R${user_e:.2f} to'
          f' R${user_e + ((user_e / 100) * e_low):.2f}.')
else:
    print(f'\nSalary increase {e_high}%, from R${user_e:.2f} to'
          f' R${user_e + ((user_e / 100) * e_high):.2f}.')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print('\n\nLesson 035 >> Develop a program able to read three lengths and return if them can build a triangle:\n')
len1 = float(input('Gimme a length in only with numbers: '))
len2 = float(input('Another one: '))
len3 = float(input('And the last one: '))
triangle = len1 < len2 + len3 and len2 < len1 + len3 and len3 < len1 + len2

if triangle:
    print(f'Yeah! You got a triangle!')
else:
    print(f'Those number can\'t build a triangle. Try again!')



""" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    CONDITIONALS: IF VALUE -VS- IF VALUE IS NOT NONE
        ./conditionals_if-value_vs_if-value-is-not-none.py
"""