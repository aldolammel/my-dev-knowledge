from datetime import datetime
from time import sleep
from random import choice

_corIn = '\033[1;'
_corSucc = '32m'
_corFail = '31m'
_corOut = '\033[m'

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

_housePrice = float(input('What\'s the house price? R$'))
_earn = float(input('How much is your monthly earn? R$'))
_howLong = int(input('How long time do you want to pay (in months): '))

_bill = _housePrice / _howLong

print('\nAnalysing your loan request...\n')
sleep(2)

print(f'Full price: {_housePrice:.2f}\n'
      f'Monthly ({_howLong}x): R${_bill:.2f}\n')
sleep(2)

if _bill < (_earn / 100) * 30:
    print(f'{_corIn}{_corSucc}Loan has been approved! Congrats!{_corOut}')
else:
    print(f'{_corIn}{_corFail}Loan denied!{_corOut}')

# ----------------------------------
# LESSON 037

_numb37 = int(input('\n\nType an integer: '))
print('\nChose one of them down below:',
      '\nB = convert your number to Binary;',
      '\nO = convert your number to Octal;',
      '\nH = convert your number to Hexadecimal;')
_userChoice37 = str(input('Your choice: ')).strip().upper()

if _userChoice37 == 'B':
    print(f'{_numb37} converted to BINARY: {_corIn}{_corSucc}{bin(_numb37)[2:]}{_corOut}')

elif _userChoice37 == 'O':
    print(f'{_numb37} converted to OCTAL: {_corIn}{_corSucc}{oct(_numb37)[2:]}{_corOut}')

elif _userChoice37 == 'H':
    print(f'{_numb37} converted to HEXADECIMAL: {_corIn}{_corSucc}{hex(_numb37)[2:]}{_corOut}')

else:
    print(f'{_corIn}{_corFail}Invalid option. Go again.{_corOut}')

# ----------------------------------
# LESSON 038

_value1 = int(input('\n\nFirst value: '))
_value2 = int(input('Second value: '))

if _value1 > _value2:
    print(f'\n{_corIn}{_corSucc}{_value1}{_corOut} is bigger than {_corIn}{_corFail}{_value2}{_corOut}.')

elif _value1 < _value2:
    print(f'\n{_corIn}{_corSucc}{_value2}{_corOut} is bigger than {_corIn}{_corFail}{_value1}{_corOut}.')

else:
    print('\nThe numbers are the same!')

# ----------------------------------
# LESSON 039

_birthYear = int(input('\n\nYour birth year (e.g. 1984): '))
_enlistYear = _birthYear + 18
_currentYear = datetime.today().year

if _enlistYear > _currentYear:
    print(f'\nYou need to report for army service only in {_corIn}{_corFail}{_enlistYear - _currentYear}'
          f' year(s){_corOut}.')
elif _enlistYear == _currentYear:
    print(f'\nYou must report for army service {_corIn}{_corFail}this year{_corOut}. Get ready, son!')
else:
    print(f'\nThank you for already reporting to the army service {_corIn}{_corSucc}{_currentYear - _enlistYear}'
          f' year(s) ago{_corOut}.')
    
# ----------------------------------
# LESSON 040

_grade1 = float(input('\n\nGimme a school degree: '))
_grade2 = float(input('Gimme a second school degree: '))
_average = (_grade1 + _grade2) / 2

print(f'\nYour final grade: \033[1m{_average:.1f}\033[m')
if 5 <= _average < 7:
    print(f'{_corIn}{_corFail}You must do a new exam to improve your grade.{_corOut}')
elif _average < 5:
    print(f'{_corIn}{_corFail}You failed your school exams.{_corOut}')
else:
    print(f'{_corIn}{_corSucc}Congratulations! You are in a new level up.{_corOut}')

# ----------------------------------
# LESSON 041

_yourAge = int(input('\n\nHow old are you: '))

if _yourAge > 25:
    print(f'You are {_corIn}{_corSucc}master level{_corOut}, up than 25 yo.')
elif 19 < _yourAge <= 25:
    print(f'You are {_corIn}{_corSucc}senior level{_corOut}, from 19 to 25 yo.')
elif 14 < _yourAge <= 19:
    print(f'You are {_corIn}{_corSucc}junior level{_corOut}, from 14 to 19 yo.')
elif 9 < _yourAge <= 14:
    print(f'You are {_corIn}{_corSucc}children level{_corOut}, from 14 to 19 yo.')
else:
    print(f'You are {_corIn}{_corSucc}kinder level{_corOut}, from 0 to 9 yo.')


# ----------------------------------
# LESSON 042

_length1 = float(input('\n\nGimme a length only with numbers: '))
_length2 = float(input('Another one: '))
_length3 = float(input('And the last one: '))
_triangle = _length1 < _length2 + _length3 and _length2 < _length1 + _length3 and _length3 < _length1 + _length2

if _triangle:
    print(f'\nYeah! {_corIn}{_corSucc}You got{_corOut} a triangle!')

    if _length1 == _length2 == _length3:
        print(f'This is a triangle: {_corIn}{_corSucc}Equilátero{_corOut}, all sides have the same length.')

    elif _length1 != _length2 != _length3 != _length1:
        print(f'This is a triangle: {_corIn}{_corSucc}Escaleno{_corOut}, all sides have different lengths.')

    else:
        print(f'This is a triangle: {_corIn}{_corSucc}Isósceles{_corOut}, two sides have the same length.')

else:
    print(f'\nThose numbers {_corIn}{_corFail}can\'t{_corOut} build a triangle. Try again!')

# ----------------------------------
# LESSON 043

_height = float(input('\n\nYour height (e.g. 1.80): '))
_weight = float(input('Your weight (e.g. 80) Kg: '))
_imc = _weight / (_height ** 2)
print(f'\n\nYour IMC is \033[1m{_imc:.1f}\033[m:')

if _imc > 40:
    print(f'{_corIn}{_corFail}You\'re huge, man! Oh my gosh! Stop the tacos and soda, dude!{_corOut}')

elif 40 >= _imc > 30:
    print(f'{_corIn}{_corFail}You are obese!{_corOut}')

elif 30 >= _imc > 25:
    print(f'{_corIn}{_corFail}You are fat.{_corOut}')

elif 25 >= _imc >= 18.5:
    print(f'{_corIn}{_corSucc}Your IMC is okay!{_corOut}')

elif _imc < 18.5:
    print(f'{_corIn}{_corFail}You must to get weight!{_corOut}')

# ----------------------------------
# LESSON 044

_price = float(input('\n\nType the price: R$'))

_method1 = 'Cash (10% off)'
_method2 = 'Bank check (10% off)'
_method3 = 'Credit card 1x (5% off)'
_method4 = 'Credit card 2x'
_method5 = 'Credit card 3x or more (20% plus)'

print(f'\n{"-" * 60}',
      f'\n1 = {_method1}',
      f'\n2 = {_method2}',
      f'\n3 = {_method3}',
      f'\n4 = {_method4}',
      f'\n5 = {_method5}',
      f'\n{"-" * 60}')

_methodPay = int(input('\nWhich payment method above do you want: '))

if _methodPay == 1 or _methodPay == 2:
    print(f'Chosen method: {_method1} or {_method2}')
    print(f'Total payable: R${_price - ((_price / 100) * 10):.2f} {_corIn}{_corSucc}(10% OFF applied){_corOut}')

elif _methodPay == 3:
    print(f'Chosen method: {_method3}')
    print(f'Total payable: R${_price - ((_price / 100) * 5):.2f} {_corIn}{_corSucc}(5% OFF applied){_corOut}')

elif _methodPay == 4:
    print(f'Chosen method: {_method4}')
    print(f'Total payable: R${_price:.2f}')

elif _methodPay == 5:
    print(f'Chosen method: {_method5}')
    print(f'Total payable: R${_price + ((_price / 100) * 20):.2f} {_corIn}{_corFail}(20% surcharge){_corOut}')

else:
    print('Invalid choice! Please, try again.')

# ----------------------------------
# LESSON 045

_rock = "Rock"
_paper = "Paper"
_scissors = "Scissors"
_options = [_rock, _paper, _scissors]

print(f'\n\n{"-" * 20}',
      f'\n1 = {_rock}',
      f'\n2 = {_paper}',
      f'\n3 = {_scissors}',
      f'\n{"-" * 20}')

_userChoice = int(input('\nMake a call: '))

if _userChoice == 1:
    _userChoice = _rock
elif _userChoice == 2:
    _userChoice = _paper
else:
    _userChoice = _scissors

_aiChoice = choice(_options)

if _userChoice == _aiChoice:
    print('\nTied! Try again!')

elif (_userChoice == _rock and _aiChoice == _scissors) or (_userChoice == _scissors and _aiChoice == _rock):
    print(f'\n{_rock} wins {_scissors}!')

elif (_userChoice == _paper and _aiChoice == _rock) or (_userChoice == _rock and _aiChoice == _paper):
    print(f'\n{_paper} wins {_rock}!')

elif (_userChoice == _scissors and _aiChoice == _paper) or (_userChoice == _paper and _aiChoice == _scissors):
    print(f'\n{_scissors} wins {_paper}!')

print(f'\nYou chose the {_corIn}{_corSucc}{_userChoice}{_corOut}.')
print(f'AI chose the {_corIn}{_corFail}{_aiChoice}{_corOut}.')
