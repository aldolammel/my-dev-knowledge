# USING MULTIPLE VARIABLES:

# CHALLENGE 005
print('005 >> Build a program where you gimme a number and I\'ll show its previous and next\n',
      'numbers automatically:\n')
nInt = int(input('Choose an integer: '))
print(f'You chose {nInt} as integer.\nThe previous number of that is {nInt - 1} meanwhile\n',
      f'the next one is {nInt + 1}.')

# CHALLENGE 006
print('\n\n006 >> Create an algorithm that read a number and show its double, triple\nand square root:\n')
nInt2 = int(input('Now, give me another integer, please: '))
itsDouble = nInt2 * 2
itsTriple = nInt2 * 3
itsSquare = nInt2 ** (1/2)
print(f'Cool, your choice was {nInt2} and its double is {itsDouble} and triple, {itsTriple}, while, finally,\n',
      f'the square root is {itsSquare:.2f}.')

# CHALLENGE 007
print('\n\n007 >> Develop a program that it read two school grades of\nthe same student, showing their average:\n')
grade1 = float(input('What\'s their first school grade? '))
grade2 = float(input('Ok, and what\'s their second one? '))
gradeAverage = (grade1 + grade2) / 2
print(f'The student got {grade1:.1f} and {grade2:.1f} as school grades, so their average is {gradeAverage:.1f}.')

# CHALLENGE 008
print('\n\n008 >> Write a code where a value in meters is converted to\ncentimeters and millimeters:\n')
nMts = float(input('Try a number in meters: '))
nCm = int(nMts * 100)
nMm = int(nMts * 1000)
print(f'Then {nMts:.2f}m is equal to {nCm:.2f}cm or, in millimeters,\nequal to {nMm:.2f}mm.')

# CHALLENGE 009
print('\n\n009 >> Let\'s code a program that read any integer and present\nautomatically its multiplication table:\n')
nTable = int(input('Type an integer and get ready for magic, pal: '))
print('The multiplication table of', nTable, 'is:')
print(f' {nTable} x 1 = {nTable * 1}\n {nTable} x 2 = {nTable * 2}\n',
      f'{nTable} x 3 = {nTable * 3}\n {nTable} x 4 = {nTable * 4}\n',
      f'{nTable} x 5 = {nTable * 5}\n {nTable} x 6 = {nTable * 6}\n',
      f'{nTable} x 7 = {nTable * 7}\n {nTable} x 8 = {nTable * 8}\n',
      f'{nTable} x 9 = {nTable * 9}\n {nTable} x 10 = {nTable * 10}')

# CHALLENGE 010
print('\n\n010 >> Can you build a program that it read how much cash (in R$) someone gets in wallet and\n',
      'convert it automatically to U$?\n')
bozoCash = float(input('In Brazilian Real, how much money Bozo gets in his pocket: R$'))
dCurrencyToday = float(input('But first, about today, with R$1 we can buy how much Dollars? U$'))
realToDollarToday = int(bozoCash * dCurrencyToday)
realToDollar2017 = int(bozoCash / 3.27)
print(f'\n Folks, Bozo gets in his pocket U${realToDollarToday} for his beard-kids visit Disney again.\n',
      f'In 2017, when his baby boys tried Disney for the very first time, with the\n',
      f'same R$ amount, Bozo would have in that time U${realToDollar2017}\n Can I back in time?')
