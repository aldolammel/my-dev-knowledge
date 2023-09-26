"""

SLICING:
(Fatiamento)


"""

_phrase = 'Who is the Russian dwarf most famous nowadays?'
print('\n\nLets analyse this question: \"', _phrase, '\"\n')

print(f'At first, easy to see the phrase got {len(_phrase)} characters.',
      f'However let\'s go through it deeper:\n')

print('So think: ', _phrase[11:])           # using slicing from 11th to the last phrase letter.
print(_phrase[:24], '?')                    # from the phrase beginning to its 23rd letter.
print('Putin is a', _phrase[11:24], '!')    # from 11th to the 23rd (always one before) phrase letter.
print(_phrase[::3])                         # from the first til the last letter but jumping 3 and 3 letters.
print(_phrase[::-1])                        # from the last til the first (reverse).

_letter = str(input('\nType a single letter: '))
_letterCounter = int(_phrase.upper().count(_letter.upper()))       # converting all letters to uppercase.

print(f'\nThe original question-phrase has {_letterCounter}',      # .upper and .count functions running.
      f'\'{_letter.upper()}\' letter.\n')

_userPhrase = str(input('Now, type our own phrase: '))
_characterCounter = len(_userPhrase)                              # len() is used to count things.
_spaceCounter = _userPhrase.count(' ')                            # .count is used to count characters?
_wordsArray = _userPhrase.split()                                 # .split the string in words.

print(f'Your phrase has {_characterCounter} characters, {_characterCounter - _spaceCounter} letters',
      f'(including punctuation) and {len(_wordsArray)} words.')

# --------------------------------------------------
# LESSON 022

print('''\n\nLesson 022 >> Build a program capable to read a full name in lower and uppercase,
plus its characters amount with no spaces, including how much letters the first name brings.\n''')

_userName = str(input('Insert a full name: ').title().strip())
_userNameArray = _userName.split()

print(f'{_userName} converted to lowercase is \'{_userName.lower()}\' and uppercase is \'{_userName.upper()}\'. \n'
      f'Although the whole name got {len(_userName) - _userName.count(" ")} letters, the first name '
      f'got only {len(_userNameArray[0])}.')

# --------------------------------------------------
# LESSON 023

print('\n\nLesson 023 >> Create an app able to receive an integer between 0 and 9999 and tells us'
      ' what\'s the unity, ten, hundred and the thousand of the chosen number:\n')

_givenNumb = int(input('An integer between 0 to 9999: '))

_unity = _givenNumb // 1 % 10  # número com divisão-inteira (//) por 1 (ele mesmo), divido por 10 (% = resto da divisão)
_ten = _givenNumb // 10 % 10
_hundred = _givenNumb // 100 % 10
_thousand = _givenNumb // 1000 % 10

print(f'Analysing the number {_givenNumb}: \n'
      f'Unity = {_unity}\n'
      f'Ten = {_ten}\n'
      f'Hundred = {_hundred}\n'
      f'Thousand = {_thousand}\n')

# --------------------------------------------------
# LESSON 024

print('\n\nLesson 024 >> Build a program capable to understand if the city\'s name begins with \'Santo\' word:\n ')
_city = str(input('Type a city\'s name: ')).strip().upper()

_comparison = _city[:5] == str('SANTO')   # I'm counting the digits from first until 4th digit in _city string.

print(_comparison)

# LESSON 025
print('\n\nLesson 025 >> Build a program able to recognize if \'Silva\' belongs to the people name:\n')

_passport = str(input('Type a full name: ')).strip().title()
_checkingPass = 'SILVA' in _passport.upper()

print(f'{_passport} is a citizen of Silvaland? {_checkingPass}')

# --------------------------------------------------
# LESSON 026

print('\n\nLesson 026 >> Create a program that reads a phrase and shows how many the letter \'A\' shows up and'
      ' its first and last position in there:\n')

_letterPhrase = str(input('Type any phrase, please: ')).strip().upper()
# Only a perfect phrase to testing: À medida que espero o avião há horas, uma ágil e inesperada ânsia me vem.

_aConverted = _letterPhrase.replace('Â', 'A').replace('Â', 'A').replace('À', 'A').replace('Á', 'A').replace('Ä', 'A')
_aCounted = _aConverted.count('A')

print(f'It finds {_aCounted} letter \'A\' in your phrase. The first \'A\' occurs in the character position number'
      f' {_aConverted.find("A") + 1},'
      f' meanwhile the last one in the position number {_aConverted.rfind("A") + 1}.')

# --------------------------------------------------
# LESSON 027

print('\n\nLesson 027 >> Show me a code capable to understand a full name and shows up that first and '
      'last name apart:\n')

_fullName27 = str(input('Type a full name, please: ')).strip().title()
_arrayNames27 = _fullName27.split()
_firstWord27 = _arrayNames27[0]                           # Zero is the first object/name inside that array.
_lastWord27 = _arrayNames27[len(_arrayNames27)-1]

print(f'The full name \'{_fullName27}\' is composed by the first word \'{_firstWord27}\''
      f' and the last word \'{_lastWord27}\'.')
