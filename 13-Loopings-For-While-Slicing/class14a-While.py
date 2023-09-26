from random import randint

# MY COLORS:
_corInSucc = '\033[1;32m'
_corInFail = '\033[1;31m'
_corOut = '\033[m'

# ------------------------------------------------------------------
# LESSON 057

print('\n\nLesson 057 >> Built a program that read the gender of someone but just accept "M" or "F" values. In case'
      'the type disagreed the rule, ask again the gender:\n')

_genderPhrase = 'Which gender? [M/F]: '
_userGender = str(input(_genderPhrase)).strip().upper()[0]    # using slicing/fatiamento

while _userGender not in 'MF':
    _userGender = str(input(f'Invalid gender. {_genderPhrase}')).strip().upper()[0]

print(f'\nYour gender is {_corInSucc}{_userGender}{_corOut}.')

print('Lesson 057 has been finished successfully!')

# ------------------------------------------------------------------
# LESSON 058

print('\n\nLesson 058 >> Make an AI capable to think in an integer between 0 and 10 and print that after the player\n'
      'tries to guess which number the AI thought. As long as the user doesnt guess what the number is, the AI\n'
      'will continue in the game:\n')

_youAreLooser = True

while _youAreLooser:

    _aiChoice = randint(0, 11)
    _userChoice = int(input('From 0 to 10, try to guess what integer number the computer is thinking now: '))

    if _aiChoice != _userChoice:
        print(f'\nAI chose {_corInFail}{_aiChoice}{_corOut}.'
              f'\n{_corInFail}You, humans, are so losers!{_corOut}\n')
    else:
        _youAreLooser = False

print(f'{_corInSucc}Hm, you win! Good!{_corOut}')

# ------------------------------------------------------------------
# LESSON 059

print('\n\nLesson 059 >> Build an app allowed to read two values and shows up them into a screen menu:\n')

while True:

    _value1 = int(input('Give an integer: '))
    _value2 = int(input('Another integer: '))

    print('\nPlease, chose an option down below:\n', '1 = Sum\n', '2 = Multiply\n', '3 = Bigger\n',
          '4 = Choose new integers\n', '5 = Exit\n')

    _userChoice = int(input('Your choice: '))

    if _userChoice == 1 or _userChoice == 2 or _userChoice == 3 or _userChoice == 5:

        if _userChoice == 1:
            print(f'{_value1} plus {_value2} is {_corInSucc}{_value1 + _value2}{_corOut}.\n')

        if _userChoice == 2:
            print(f'{_value1} multiply by {_value2} is {_corInSucc}{_value1 * _value2}{_corOut}.\n')

        if _userChoice == 3:
            if _value1 == _value2:
                print(f'{_corInFail}{_value1} and {_value2} are equal!{_corOut}\n')
            elif _value1 > _value2:
                print(f'{_corInSucc}{_value1}{_corOut} is bigger than {_corInFail}{_value2}{_corOut}.\n')
            else:
                print(f'{_corInSucc}{_value2}{_corOut} is bigger than {_corInFail}{_value1}{_corOut}.\n')

        if _userChoice == 5:
            break
    else:
        if _userChoice == 4:
            print('Ok...\n')
        else:
            print(f'{_corInFail}Option not valid.{_corOut} Let\'s try again:\n')

print('\nThe lesson 059 has been finished!')

# ------------------------------------------------------------------
# LESSON 060 (WITH -FOR- SOLUTION):

print('\n\nLesson 060 >> WITH -FOR- SOLUTION: Show me the factorial of a number:\n')

_userFactA = int(input('Gimme an integer to figure out its factorial: '))
_factA = 1

for _i in range(_userFactA, 0, -1):

    print(f'{_i}', end='')

    if _i > 1:
        print(f' x ', end='')
    else:
        print(f' = ', end='')

    _factA = _factA * _i

print(f'{_corInSucc}{_factA}{_corOut}')

# ------------------------------------------------------------------
# LESSON 060 (WITH -WHILE- SOLUTION):

print('\n\nLesson 060 >> WITH -WHILE- SOLUTION: Show me the factorial of a number:\n')

_userFactB = int(input('Gimme an integer to figure out its factorial: '))
_factB = 1

while _userFactB > 0:

    print(f'{_userFactB}', end='')

    if _userFactB > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')

    _factB = _factB * _userFactB
    _userFactB = _userFactB - 1

print(f'{_corInSucc}{_factB}{_corOut}')

# ------------------------------------------------------------------
# LESSON 061

print('\n\nLesson 061 >> Let\'s built an Arithmetic Progression with 10 numbers, using the -WHILE-, '
      'it doesnt matter the integer inputted:\n')

_startAP = int(input('A first term (e.g. 20): '))
_razaoAP = int(input('"razão" number (e.g. 5): '))

_whileCycles = 1
_ap = _startAP

while _whileCycles <= 10:

    print(f'{_ap} >> ', end='')
    _ap += _razaoAP
    _whileCycles += 1

print(f'{_corInSucc}Done!{_corOut}')

# ------------------------------------------------------------------
# LESSON 062

print('\n\nLesson 062 >> Let\'s built an Arithmetic Progression with 10 numbers,'
      'it doesnt matter the integer inputted. Plus: give to the user the possibility they expand the AP:\n')

_startAP2 = int(input('Type an integer, term (e.g. 20): '))
_razaoAP2 = int(input('Type an integer, razão (e.g. 5): '))

_termCycles = 10
_termsCounter = 0
_whileCyclesAP2 = 0
_ap2 = _startAP2

while _whileCyclesAP2 <= _termCycles:

    print(f'{_ap2} >> ', end='')
    _ap2 = _ap2 + _razaoAP2
    _whileCyclesAP2 = _whileCyclesAP2 + 1

    if _whileCyclesAP2 == _termCycles:
        _addingTerms = int(input(f'{_corInSucc}Type how much terms you wanna add:{_corOut} '))
        _termCycles = _addingTerms
        _whileCyclesAP2 = 0

    _termsCounter = _termsCounter + 1

    if _termCycles <= 0:
        break

print(f'\nDone after {_corInSucc}{_termsCounter} terms{_corOut}.')

# ------------------------------------------------------------------
# LESSON 063

print('\n\nLesson 063 >> Build the Fibonacci sequence:\n')

_fiboLimiter = int(input('How deep you wanna go in Fibonacci sequence: '))

_whileCounter = 3
_fiboNumb1 = 0
_fiboNumb2 = 1

print(f'{_fiboNumb1} >> {_fiboNumb2} >> ', end='')

while _whileCounter <= _fiboLimiter:

    _fiboNumb3 = _fiboNumb1 + _fiboNumb2

    print(f'{_fiboNumb3} >> ', end='')

    _fiboNumb1 = _fiboNumb2
    _fiboNumb2 = _fiboNumb3

    _whileCounter += 1

print(f'Fibonacci until its first {_fiboLimiter} terms, done!')

# ------------------------------------------------------------------
# LESSON 064

print('\n\nLesson 064 >> Build a program that you ask the user to input an integer and repeat that until the user\n'
      'to type 999 to stop it. After that, present the type times and the sum of all times, less the "999 flag":\n')

_flagNumb = 999
_userNumb64 = 0
_fakeSum = 0
_whileCycles64 = -1

while _userNumb64 != _flagNumb:

    _userNumb64 = int(input('Type an integer [999 to stop]: '))

    _fakeSum += _userNumb64
    _whileCycles64 += 1

print(f'\nYou typed {_corInSucc}{_whileCycles64} time(s){_corOut} and the sum is: '
      f'{_corInSucc}{_fakeSum - _flagNumb}{_corOut}')


# ------------------------------------------------------------------
# LESSON 065

print('\n\nLesson 065 >> Read several integers and, if the user wants to finish it, show up the biggest number typed\n'
      ' as well as the smallest one:\n')

_user65choice = 'Y'
_biggest65numb = 0
_smallest65numb = 0
_while65cycles = 0
_sum65 = 0

while _user65choice in 'Y':

    _user65numb = int(input('Gimme an integer: '))

    _sum65 += _user65numb

    if _while65cycles == 0:
        _biggest65numb = _smallest65numb = _user65numb
    else:
        if _biggest65numb < _user65numb:
            _biggest65numb = _user65numb
        if _smallest65numb > _user65numb:
            _smallest65numb = _user65numb

    _while65cycles += 1

    _user65choice = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]  # checking just the first letter.

if _user65choice in 'YN':
    print(f'\n You\'ve typed {_while65cycles} numbers and their average were {_sum65 / _while65cycles:.1f}.\n',
          f'The biggest value was {_biggest65numb} and the smallest one, {_smallest65numb}.')
else:
    print(f'{_corInFail}Invalid choice! The program was terminated.{_corOut}')
