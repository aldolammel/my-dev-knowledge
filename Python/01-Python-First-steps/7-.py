# USING MULTIPLE VARIABLES:

# CHALLENGE 005
print('005 >> Build a program where you gimme a number and I\'ll show its previous and next\n',
      'numbers automatically:\n')
_numbInt = int(input('Choose an integer: '))
print(f'You chose {_numbInt} as integer.\nThe previous number of that is {_numbInt - 1} meanwhile\n',
      f'the next one is {_numbInt + 1}.')

# CHALLENGE 006
print('\n\n006 >> Create an algorithm that read a number and show its double, triple\nand square root:\n')
_numbInt2 = int(input('Now, give me another integer, please: '))
_itsDouble = _numbInt2 * 2
_itsTriple = _numbInt2 * 3
_itsSquare = _numbInt2 ** (1/2)
print(f'Cool, your choice was {_numbInt2} and its double is {_itsDouble} and triple, {_itsTriple}, while, finally,\n',
      f'the square root is {_itsSquare:.2f}.')

# CHALLENGE 007
print('\n\n007 >> Develop a program that it read two school grades of\nthe same student, showing their average:\n')
_grade1 = float(input('What\'s their first school grade? '))
_grade2 = float(input('Ok, and what\'s their second one? '))
_gradeAverage = (_grade1 + _grade2) / 2
print(f'The student got {_grade1:.1f} and {_grade2:.1f} as school grades, so their average is {_gradeAverage:.1f}.')

# CHALLENGE 008
print('\n\n008 >> Write a code where a value in meters is converted to\ncentimeters and millimeters:\n')
_numbMts = float(input('Try a number in meters: '))
_numbCm = int(_numbMts * 100)
_numbMm = int(_numbMts * 1000)
print(f'Then {_numbMts:.2f}m is equal to {_numbCm:.2f}cm or, in millimeters,\nequal to {_numbMm:.2f}mm.')

# CHALLENGE 009
print('\n\n009 >> Let\'s code a program that read any integer and present\nautomatically its multiplication table:\n')
_numbForTable = int(input('Type an integer and get ready for magic, pal: '))
print('The multiplication table of', _numbForTable, 'is:')
print(f' {_numbForTable} x 1 = {_numbForTable * 1}\n {_numbForTable} x 2 = {_numbForTable * 2}\n',
      f'{_numbForTable} x 3 = {_numbForTable * 3}\n {_numbForTable} x 4 = {_numbForTable * 4}\n',
      f'{_numbForTable} x 5 = {_numbForTable * 5}\n {_numbForTable} x 6 = {_numbForTable * 6}\n',
      f'{_numbForTable} x 7 = {_numbForTable * 7}\n {_numbForTable} x 8 = {_numbForTable * 8}\n',
      f'{_numbForTable} x 9 = {_numbForTable * 9}\n {_numbForTable} x 10 = {_numbForTable * 10}')

# CHALLENGE 010
print('\n\n010 >> Can you build a program that it read how much cash (in R$) someone gets in wallet and\n',
      'convert it automatically to U$?\n')
_bozoCash = float(input('In Brazilian Real, how much money Bozo gets in his pocket: R$'))
_dCurrencyToday = float(input('But first, about today, with R$1 we can buy how much Dollars? U$'))
_realToDollarToday = int(_bozoCash * _dCurrencyToday)
_realToDollar2017 = int(_bozoCash / 3.27)
print(f'\n Folks, Bozo gets in his pocket U${_realToDollarToday} for his beard-kids visit Disney again.\n',
      f'In 2017, when his baby boys tried Disney for the very first time, with the\n',
      f'same R$ amount, Bozo would have in that time U${_realToDollar2017}\n Can I back in time?')
