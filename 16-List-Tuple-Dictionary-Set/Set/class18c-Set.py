"""

SET:
As similar as Dictionaries, but with no Keys, loading only single values (no duplicates).
In SET, we haven't control over the values position within. The order of the values is unpredictable.
In SET, we can mix different types of data inside: float, int, str, bool.
The main goal of the SET collections are load values with no duplicates.
As Dict, SET also use braces {}, so careful.

Example of a list = [2, 2, 5, 5, 10, 10]
It converted to set = {2, 5, 10}

Empty set:  _mySet = set()

Converting to set: _mySet = set(_myList)

"""

_listCollection = [2, 5, 23, 3, 3, 0, 122, 3]                   # original collection for test.

_setCollection = set(_listCollection)                           # setting the list collection into a -set- collection.

print('List (array) collection: ', _listCollection)
print('Set collection: ', _setCollection)

print('\n-------\n')

"""

ADDING & REMOVING:
Adding and removing values in a -set-:

"""
_setEmpty = set()                                               # never use '{}' to indicate a -set- empty.
_setEmpty.add(12)
_setEmpty.add(24)
print('_setEmpty now: ', _setEmpty)
_setEmpty.remove(12)
print('_setEmpty now after a value been removed: ', _setEmpty)

# To clean the whole -set-:
_anotherSet = {10, 5, 2}
_anotherSet.clear()
print('_anotherSet after the cleaning: ', _anotherSet)

# The same, but with stringers in the -set- content:
_stringSet = {'Anna', 'Anna', 'Anna', 'Aldo', 'Aldo', 'Aldo'}
_stringSet.add('Zack')
print('_stringSet: ', _stringSet)

# practicing the adding:
_myList = list()
_mySet = set()

for _i in range(11):
    _myList.append(_i)
    _mySet.add(_i)

print('_myList: ', _myList)
print('_mySet:  ', _mySet)

for _i in range(11):
    _myList.append(_i)
    _mySet.add(_i)

print('\nCurrent _myList, after another round adding the same original values: ', _myList)
print('Current _mySet, after another round adding the same original values:  ', _mySet)     # will never be duplicated.
print('Can you see some differences above between _myList and _mySet? ;)')

print('\n-------\n')

"""

COPYING:
Differences between Deep Copy and Shallow Copy:

"""

# Deep copy:
_setFull = {2, 12, 1}
_setCopy = _setFull.copy()
_setCopy.add(0)
print('DEEP COPY (true copy):')
print('Original set:             ', _setFull)
print('Copied set + a new value: ', _setCopy)

# shallow copy:
_setFull2 = {2, 12, 1}
_setCopy2 = _setFull2
_setCopy2.add(0)
print('\nSHALLOW COPY (directly connection between the sets):')
print('Original set:             ', _setFull2, '    (unfortunately, it brings the new value too)')
print('Copied set + a new value: ', _setCopy2)

print('\n-------\n')

# UNION method: taking 2 or more collections and creating a set collection only with unique values:
print('\nUNION METHOD:')
_studentsClass1 = {'John', 'Anne', 'Aldo', 'Billy'}
_studentsClass2 = {'Jack', 'Billy', 'Frank', 'Aldo'}
_studentsNames = _studentsClass1.union(_studentsClass2)      # union syntax.
print('_studentsClass1 = ', _studentsClass1)
print('_studentsClass2 = ', _studentsClass2)
print('_studentsNames = ', _studentsNames)

print('\n-------\n')

# INTERSECTION method: taking 2 or more collection and creating a set collection only with the duplicates cases:
print('\nINTERSECTION METHOD:')
studentsClass3 = {'Carmen', 'Jonathan', 'Bob', 'Kendrick'}
studentsClass4 = {'Carmen', 'Joseph', 'Bob', 'Sarah'}
studentsAtBothClasses = studentsClass3.intersection(studentsClass4)
print(f'studentsClass3 = {studentsClass3}')
print(f'studentsClass4 = {studentsClass4}')
print(f'studentsAtBothClasses = {studentsAtBothClasses}')

print('\n\nLesson >>> Build a program that check with -intersection- if the player got some lottery numbers:\n')

_lotNums = {13, 21, 22, 5, 8}

_plrs = [
    {
        'name': 'Aldo',
        'numbers': {19, 2, 31, 48, 5}
    },
    {
        'name': 'Jack',
        'numbers': {13, 22, 30, 40, 5}
    }
]

print(f'{_plrs[0]["name"]} got {len(_plrs[0]["numbers"].intersection(_lotNums))} number(s) right.')
print(f'{_plrs[1]["name"]} got {len(_plrs[1]["numbers"].intersection(_lotNums))} number(s) right.')

print('\n-------\n')

# DIFFERENCE method: taking 2 or more collection and creating a set collection only those values unique in each case:
print('\nDIFFERENCE METHOD:')
_studentsEnglish = {'Loli', 'Julian', 'Kelly'}
_studentsPortuguese = {'Kelly', 'Kennedy', 'Zoe'}
_studentsOnlyEnglish = _studentsEnglish.difference(_studentsPortuguese)
_studentsOnlyPortuguese = _studentsPortuguese.difference(_studentsEnglish)
print('_studentsEnglish = ', _studentsEnglish)
print('_studentsPortuguese = ', _studentsPortuguese)
print('_studentsOnlyEnglish = ', _studentsOnlyEnglish)
print('_studentsOnlyPortuguese = ', _studentsOnlyPortuguese)

print('\n-------\n')

"""

DIFFERENCES BETWEEN LISTS, TUPLES, DICTS & SETS:

"""

_numbers = 99, 2, 34, 2, 34, 99, 0      # in this way, it'll be a tuple, even with no braces.
print(f'Original data (_numbers = {type(_numbers)}): {_numbers}\n\n')

_lis = list(_numbers)
_tup = tuple(_numbers)
_dic = {}.fromkeys(_numbers, 'Something')
_set = set(_numbers)

print(
    f'Converted to List  | {len(_lis)} numbers: {_lis}\n'  # list accepts duplicated values.
    f'Converted to Tuple | {len(_tup)} numbers: {_tup}\n'  # tuple accepts duplicated values.
    f'Converted to Dict  | {len(_dic)} numbers: {_dic}\n'  # here the numbers are keys and keys can't be duplicated.
    f'Converted to Set   | {len(_set)} numbers: {_set}'    # set will never accept duplicated values.
)

print('\n-------\n')


