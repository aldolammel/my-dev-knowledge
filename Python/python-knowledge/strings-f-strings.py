# On Python, "F-Strings" concept is pretty similar to JavaScript "String Interpolation" concept.

# To check string formatting:
# ./string-formatting.py

from datetime import datetime
from time import sleep
from random import choice

c_start = '\033[1;'
c_success = '32m'
c_fail = '31m'
c_end = '\033[m'

# ----------------------------------
# PRE-LESSON

counter_minutes = 1
counter_seconds = 15
is_running = True
while is_running:
    if counter_seconds >= 0:
        print(f"{counter_minutes:02d}:{counter_seconds:02d}")  # this ":02d" force the timer shows two digits.
        counter_seconds -= 1
        sleep(1)
    else:
        is_running = False

# ----------------------------------
# LESSON 036

house_price = float(input('What\'s the house price? R$'))
earn = float(input('How much is your monthly earn? R$'))
how_long = int(input('How long time do you want to pay (in months): '))

bill = house_price / how_long

print('\nAnalysing your loan request...\n')
sleep(2)

print(f'Full price: {house_price:.2f}\n'
      f'Monthly ({how_long}x): R${bill:.2f}\n')
sleep(2)

if bill < (earn / 100) * 30:
    print(f'{c_start}{c_success}Loan has been approved! Congrats!{c_end}')
else:
    print(f'{c_start}{c_fail}Loan denied!{c_end}')

# ----------------------------------
# LESSON 037

n37 = int(input('\n\nType an integer: '))
print('\nChose one of them down below:',
      '\nB = convert your number to Binary;',
      '\nO = convert your number to Octal;',
      '\nH = convert your number to Hexadecimal;')
userChoice37 = str(input('Your choice: ')).strip().upper()

if userChoice37 == 'B':
    print(f'{n37} converted to BINARY: {c_start}{c_success}{bin(n37)[2:]}{c_end}')

elif userChoice37 == 'O':
    print(f'{n37} converted to OCTAL: {c_start}{c_success}{oct(n37)[2:]}{c_end}')

elif userChoice37 == 'H':
    print(f'{n37} converted to HEXADECIMAL: {c_start}{c_success}{hex(n37)[2:]}{c_end}')

else:
    print(f'{c_start}{c_fail}Invalid option. Go again.{c_end}')

# ----------------------------------
# LESSON 038

val1 = int(input('\n\nFirst value: '))
val2 = int(input('Second value: '))

if val1 > val2:
    print(f'\n{c_start}{c_success}{val1}{c_end} is bigger than {c_start}{c_fail}{val2}{c_end}.')

elif val1 < val2:
    print(f'\n{c_start}{c_success}{val2}{c_end} is bigger than {c_start}{c_fail}{val1}{c_end}.')

else:
    print('\nThe numbers are the same!')

# ----------------------------------
# LESSON 039

birth_y = int(input('\n\nYour birth year (e.g. 1984): '))
enlist_y = birth_y + 18
current_y = datetime.today().year

if enlist_y > current_y:
    print(f'\nYou need to report for army service only in {c_start}{c_fail}{enlist_y - current_y}'
          f' year(s){c_end}.')
elif enlist_y == current_y:
    print(f'\nYou must report for army service {c_start}{c_fail}this year{c_end}. Get ready, son!')
else:
    print(f'\nThank you for already reporting to the army service {c_start}{c_success}{current_y - enlist_y}'
          f' year(s) ago{c_end}.')
    
# ----------------------------------
# LESSON 040

_grade1 = float(input('\n\nGimme a school degree: '))
_grade2 = float(input('Gimme a second school degree: '))
_average = (_grade1 + _grade2) / 2

print(f'\nYour final grade: \033[1m{_average:.1f}\033[m')
if 5 <= _average < 7:
    print(f'{c_start}{c_fail}You must do a new exam to improve your grade.{c_end}')
elif _average < 5:
    print(f'{c_start}{c_fail}You failed your school exams.{c_end}')
else:
    print(f'{c_start}{c_success}Congratulations! You are in a new level up.{c_end}')

# ----------------------------------
# LESSON 041

age = int(input('\n\nHow old are you: '))

if age > 25:
    print(f'You are {c_start}{c_success}master level{c_end}, up than 25 yo.')
elif 19 < age <= 25:
    print(f'You are {c_start}{c_success}senior level{c_end}, from 19 to 25 yo.')
elif 14 < age <= 19:
    print(f'You are {c_start}{c_success}junior level{c_end}, from 14 to 19 yo.')
elif 9 < age <= 14:
    print(f'You are {c_start}{c_success}children level{c_end}, from 14 to 19 yo.')
else:
    print(f'You are {c_start}{c_success}kinder level{c_end}, from 0 to 9 yo.')


# ----------------------------------
# LESSON 042

length1 = float(input('\n\nGimme a length only with numbers: '))
length2 = float(input('Another one: '))
length3 = float(input('And the last one: '))
triangle = length1 < length2 + length3 and length2 < length1 + length3 and length3 < length1 + length2

if triangle:
    print(f'\nYeah! {c_start}{c_success}You got{c_end} a triangle!')

    if length1 == length2 == length3:
        print(f'This is a triangle: {c_start}{c_success}Equilátero{c_end}, all sides have the same length.')

    elif length1 != length2 != length3 != length1:
        print(f'This is a triangle: {c_start}{c_success}Escaleno{c_end}, all sides have different lengths.')

    else:
        print(f'This is a triangle: {c_start}{c_success}Isósceles{c_end}, two sides have the same length.')

else:
    print(f'\nThose numbers {c_start}{c_fail}can\'t{c_end} build a triangle. Try again!')

# ----------------------------------
# LESSON 043

height = float(input('\n\nYour height (e.g. 1.80): '))
weight = float(input('Your weight (e.g. 80) Kg: '))
imc = weight / (height ** 2)
print(f'\n\nYour IMC is \033[1m{imc:.1f}\033[m:')

if imc > 40:
    print(f'{c_start}{c_fail}You\'re huge, man! Oh my gosh! Stop the tacos and soda, dude!{c_end}')

elif 40 >= imc > 30:
    print(f'{c_start}{c_fail}You are obese!{c_end}')

elif 30 >= imc > 25:
    print(f'{c_start}{c_fail}You are fat.{c_end}')

elif 25 >= imc >= 18.5:
    print(f'{c_start}{c_success}Your IMC is okay!{c_end}')

elif imc < 18.5:
    print(f'{c_start}{c_fail}You must to get weight!{c_end}')

# ----------------------------------
# LESSON 044

price = float(input('\n\nType the price: R$'))

method1 = 'Cash (10% off)'
method2 = 'Bank check (10% off)'
method3 = 'Credit card 1x (5% off)'
method4 = 'Credit card 2x'
method5 = 'Credit card 3x or more (20% plus)'

print(f'\n{"-" * 60}',
      f'\n1 = {method1}',
      f'\n2 = {method2}',
      f'\n3 = {method3}',
      f'\n4 = {method4}',
      f'\n5 = {method5}',
      f'\n{"-" * 60}')

method_pay = int(input('\nWhich payment method above do you want: '))

if method_pay == 1 or method_pay == 2:
    print(f'Chosen method: {method1} or {method2}')
    print(f'Total payable: R${price - ((price / 100) * 10):.2f} {c_start}{c_success}(10% OFF applied){c_end}')

elif method_pay == 3:
    print(f'Chosen method: {method3}')
    print(f'Total payable: R${price - ((price / 100) * 5):.2f} {c_start}{c_success}(5% OFF applied){c_end}')

elif method_pay == 4:
    print(f'Chosen method: {method4}')
    print(f'Total payable: R${price:.2f}')

elif method_pay == 5:
    print(f'Chosen method: {method5}')
    print(f'Total payable: R${price + ((price / 100) * 20):.2f} {c_start}{c_fail}(20% surcharge){c_end}')

else:
    print('Invalid choice! Please, try again.')

# ----------------------------------
# LESSON 045

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
options = [rock, paper, scissors]

print(f'\n\n{"-" * 20}',
      f'\n1 = {rock}',
      f'\n2 = {paper}',
      f'\n3 = {scissors}',
      f'\n{"-" * 20}')

user_choice = int(input('\nMake a call: '))

if user_choice == 1:
    user_choice = rock
elif user_choice == 2:
    user_choice = paper
else:
    user_choice = scissors

ai_choice = choice(options)

if user_choice == ai_choice:
    print('\nTied! Try again!')

elif (user_choice == rock and ai_choice == scissors) or (user_choice == scissors and ai_choice == rock):
    print(f'\n{rock} wins {scissors}!')

elif (user_choice == paper and ai_choice == rock) or (user_choice == rock and ai_choice == paper):
    print(f'\n{paper} wins {rock}!')

elif (user_choice == scissors and ai_choice == paper) or (user_choice == paper and ai_choice == scissors):
    print(f'\n{scissors} wins {paper}!')

print(f'\nYou chose the {c_start}{c_success}{user_choice}{c_end}.')
print(f'AI chose the {c_start}{c_fail}{ai_choice}{c_end}.')
