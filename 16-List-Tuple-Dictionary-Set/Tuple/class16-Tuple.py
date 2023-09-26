"""
TUPLE COLLECTION:
Kind of list but for datas that must not be modified. A tuple is immutable.
After created a tuple, you cannot add elements in that as you easily do with Lists.


Syntax: _citizens = ('Aldo', 'Billy', 'Anna')

Structure example: {dict [list (tuple) ] }

Empty tuple:    _myTuple = tuple()

Converting to tuple:       _myTuple = tuple(_myList)


"""

from random import randint

# MY COLORS
_corInSucc = '\033[1;32m'
_corInFail = '\033[1;31m'
_corOut = '\033[m'

# PRE-LESSONS

# tuple with strings:
_snacks = ('Hamburger', 'Juice', 'Pizza', 'Milk pie', 'French fries')

print('\nExample of tuple with strings:')
print(f'The original tuple: {_snacks}')
print(f'The sorted tuple:  {sorted(_snacks)}')         # it'll transform from tuple to list 'cause tuple is changeless.

print('\n---\n')

"""

ADDING / MERGING:

"""
print("adding (merging) value in a tuple (you will create a 'new tuple' because tuple is changeless):")
_tupleAdding = (10, 11)
print(f'Original _tupleAdding: {_tupleAdding}')
_tupleAdding = _tupleAdding + (12,)                    # 'adding' the value.
print(f'_tupleAdding after adding: {_tupleAdding}')      # actually, _tupleAdding replaced the original _tupleAdding.

print('\n---\n')

print('adding (merging) tuples into tuples:')
_tupleA = (1, 2, 3)
_tupleB = (5, 3, 1, 6, 3)
_tupleC = _tupleA + _tupleB     # tuples being merged.

print('print the tuple with numbers:')
print(f'Original:   {_tupleC}')              # original merge order, with _tupleA numbers first than _tupleB.
print(f'Sorted:     {sorted(_tupleC)}')      # sorting the content (will always be a list when sorted).
print(f'How much 3: {_tupleC.count(3)}')     # counting how many times the number 3 appears in that tuple.
print(f'Position of the first number 3: {_tupleC.index(3, 3)}')  # asking for the index of the first 3.

print('\n---\n')

print('adding (merging) values in a specific index:')
_tupIndex = (1, 2, 3, 4, 5, 6, 7, 8)
_tupIndex = _tupIndex[:3] + (99, 99, 99) + _tupIndex[6:]
print(_tupIndex)

print('\n---\n')

"""
FOR LOOP WITH TUPLE:

"""

print('-For- and tuple, the simplest way:')
for _i in _snacks:
    print(f'I wanna a {_i}!')

print('\n---\n')

print('-For- and tuple, variable with reference:')
for _i in range(0, len(_snacks)):
    print(f'Position {_i} from _snacks tuple: {_snacks[_i]}!')

print('\n---\n')

print('-For- and tuple, enumerate:')
for _pos, _snack in enumerate(_snacks, start=1):                      # forcing to start de counting from 1.
    print(f'Position {_pos} from _snacks tuple: {_snack}!')

print('\n---\n')

print('tuple with composition:')
_person = ('Aldo', 38, 1.75, 80.2, 'Prague, Czech Republic')
print(f'Name: {_person[0]}\n'
      f'Age: {_person[1]}\n'
      f'Height: {_person[2]}M\n'
      f'Weight: {_person[3]:.1f}Kg\n'
      f'Location: {_person[4]}')

print('\n---\n')

"""
TUPLE CONDITION:

"""

print('tuple: how to make a tuple condition without -if- and -else-:')
_myTuple = {
    'BRA': 'Brazil',
    'RUS': 'Russia'
}

_country = _myTuple.get('XPT', 'Country not found.')        # Using the -GET-: 'Key', 'Message if the key is not found.'
print(f'Result: {_country}')

print('\n---\n')

# --------------------------------------------------
# LESSON 072

print('\n\nLesson 072 >> Build a program that writes the entered number value in full:\n')

_numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    _user72Num = int(input('Type an integer between 0 and 20 (or 99 to exit): '))
    if 0 <= _user72Num <= 20:
        print(f'You have typed {_corInSucc}{_numbers[_user72Num]}{_corOut}.\n\n')
    elif _user72Num == 99:
        print(f'{_corInFail}You left the program.{_corOut}')
        break
    else:
        print(f'{_corInFail}Your number is NOT valid!{_corOut}\n\n')

# --------------------------------------------------
# LESSON 073

print('\n\nLesson 073 >> Show me some soccer team lists, using tuple structure:\n')

_brazilianSoccerTeams = ('Grêmio', 'Internacional', 'Juventude', 'Brasil de Pelotas', 'Clube Capim Soccer')

print(f'Southern Brazilian Soccer teams: {_corInSucc}{_brazilianSoccerTeams}{_corOut}.')
print(f'Only the first three:            {_corInSucc}{_brazilianSoccerTeams[:3]}{_corOut}.')
print(f'Only the last three:             {_corInSucc}{_brazilianSoccerTeams[-3:]}{_corOut}.')
print(f'{_corInSucc}Juventude{_corOut} is in the position {_corInSucc}{_brazilianSoccerTeams.index("Juventude") + 1}',
      f'{_corOut}into the _brazilianSoccerTeams tuple.')
print(f'Teams by alphabetic sort: {_corInSucc}{sorted(_brazilianSoccerTeams)}{_corOut}.')

# --------------------------------------------------
# LESSON 074 - INTUITIVE SOLUTION

print('\n\nLesson 074 INTUITIVE SOLUTION >> '
      'Draw 5 numbers and tell me which of them is the biggest and the smallest:\n')

_numbers74 = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
_sorted74 = sorted(_numbers74)

print(f' The numbers drawn were: {_corInSucc}{_numbers74}{_corOut}\n',
      f'The biggest is: {_corInSucc}{_sorted74[-1]}{_corOut}\n',
      f'The smallest is: {_corInSucc}{_sorted74[0]}{_corOut}')


# SMARTER SOLUTION: MIN & MAX METHOD

print('\n\nLesson 074 BUT WITH MIN & MAX METHOD >> Draw 5 numbers and tell which is the biggest and smallest:\n')

_numbers74b = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f' The numbers drawn were: {_corInSucc}{_numbers74b}{_corOut}\n',
      f'The biggest is: {_corInSucc}{max(_numbers74b)}{_corOut}\n',
      f'The smallest is: {_corInSucc}{min(_numbers74b)}{_corOut}')

# --------------------------------------------------
# LESSON 075

print('\n\nLesson 075 >> Ask for four integers and analyse them: which of them are eve, how many times the 9 was typed',
      'and how position is the number 3 if the 3 exists:\n')

_tupleNumbers = ((int(input(f'Type an integer: '))),
                 (int(input(f'Type an integer: '))),
                 (int(input(f'Type an integer: '))),
                 (int(input(f'Type an integer: '))))

print(f'\nYou have typed the following numbers: {_corInSucc}{_tupleNumbers}{_corOut}')
print(f'The number 9 showed up {_corInSucc}{_tupleNumbers.count(9)} times{_corOut}.')

if 3 in _tupleNumbers:
    print(f'The number 3 showed up in the position {_corInSucc}{_tupleNumbers.index(3)}{_corOut}.')
else:
    print(f'{_corInFail}There is NO number 3 in the tuple.{_corOut}')

print(f'The eve numbers typed were: ', end='')
for _i in _tupleNumbers:
    if _i % 2 == 0:
        print(f'{_corInSucc}{_i}{_corOut}', end=' ')

# --------------------------------------------------
# LESSON 076

print('\n\n\nLesson 076 >> Build a product prices table:\n')

_products = (
    'Pencil', 0.50,
    'Pen', 0.99,
    'Notebook 250 pages', 9.99,
    'College bag', 19.90,
    'Eraser', 0.50
)

print('- ' * 7, 'AVAILABLE PRODUCTS', ' -' * 7)

for _i in range(0, len(_products)):
    if _i % 2 == 0:                   # finding what obj is eve. If it is eve, it is a product and not a price.
        print(f'{_products[_i]:.<35}', end='')
    else:
        print(f'R$ {_products[_i]:>7}')

print('- - ' * 12)

# --------------------------------------------------
# LESSON 077

print('\n\nLesson 077 >> Show me twelve words and present which vowels belong to each word:')

_tupleWords = (
    'To learn',
    'To program',
    'Language',
    'Python',
    'Course',
    'Free',
    'To study',
    'To work',
    'Market',
    'Developer',
    'Future'
)

for _i in _tupleWords:

    print(f'\n{_i}: ', end='')

    for _letter in _i:

        if _letter.lower() in 'aeiou':

            print(f'{_corInSucc}{_letter.lower()}{_corOut}', end=' ')
