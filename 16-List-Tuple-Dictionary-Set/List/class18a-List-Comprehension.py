"""
LIST COMPREHENSION
Another way to work with -for- (repetition) and lists, using fewer lines.

Syntax with no conditional: _newList = [ <code to create the _newList> for _eachItem in _originalList ]
Systax with conditional:    _newList = [ <code to create the _newList> for _eachItem in _originalList if <conditional> ]

PS: the _newList variable is not needed if your set that into a print, as print([...]), for example.

"""

print("LIST COMPREHENSION (BEGINNER) SOLUTION:")
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

print("LIST COMPREHENSION (SENIOR) SOLUTION:")
numbers = [i for i in range(1, 11)]
print(numbers)

print("LIST COMPREHENSION (BEGINNER) SOLUTION:")
old_numbers1 = [1, 2, 3]
new_numbers1 = list()
for i in old_numbers1:
    new_numbers1.append(i + 1)
print(new_numbers1)

print("LIST COMPREHENSION (SENIOR) SOLUTION:")
old_numbers2 = [1, 2, 3]
new_numbers2 = [i + 1 for i in old_numbers2]
print(new_numbers2)

# ----------------------------------------------------------------------------------------------------------------------

print("DOUBLING VALUES WITH TRADITIONAL LOOPING:")
_originalNumList = [1, 2, 3, 4, 5]
_newNumList = list()
for _eachValue in _originalNumList:
    _newNumList.append(_eachValue * 2)

print(
    f'Traditional looping result:\n'
    f'Original list: {_originalNumList}\n'
    f'New list:      {_newNumList}\n'
)

print("DOUBLING VALUES WITH LIST COMPREHENSION:")
_originalNumbList = [1, 2, 3, 4, 5]
_newNumbList = [_num * 2 for _num in _originalNumbList]

print(
    f'List Comprehension result:\n'
    f'Original list: {_originalNumList}\n'
    f'New list:      {_newNumList}'
)

print('\n- - - -\n')

# --------------------------------------------------

# INPUTTING TAXES IN SOME PRODUCTS WITH TRADITIONAL LOOPING:
_purchases = [1001.00, 2250.00, 1120.00]
_purchasesWithTaxes = list()
for _eachPur in _purchases:
    if _eachPur > 1000:
        _purchasesWithTaxes.append(_eachPur * 0.5 + _eachPur)

print(
    f'Original purchase prices with no taxes:         {_purchases}\n'
    f'Purchase prices with taxes (when more than 1K): {_purchasesWithTaxes}'
)

# INPUTTING TAXES IN SOME PRODUCTS WITH LIST COMPREHENSION:
_purchases = [1001.00, 2250.00, 1120.00]
_purchasesWithTaxes = [_eachPur * 0.5 + _eachPur for _eachPur in _purchases if _eachPur > 1000]

print(
    f'Original purchase prices with no taxes:         {_purchases}\n'
    f'Purchase prices with taxes (when more than 1k): {_purchasesWithTaxes}'
)

print('\n- - - -\n')

# --------------------------------------------------

# SETTING THE FIRST LETTER NAME AS A UPPERCASE:
_friends = ['billy', 'bob', 'mike', 'linda', 'stephen']
print([_name.title() for _name in _friends])

print('\n- - - -\n')

# --------------------------------------------------

# LIST COMPREHENSION WITH F-STRINGS:

_friendsAges = [20, 32, 19, 24]
print(_friendsAges)

_newListAgeStrings = [f'My friend is {_age} years old.' for _age in _friendsAges]
print(_newListAgeStrings)

print('\n- - - -\n')

# --------------------------------------------------
# LESSON

print('\n\nLesson >> Find all of the numbers from 1-1000 that are divisible by 8:\n')

_divisibleByEight = [_num for _num in range(1, 1001) if _num % 8 == 0]
print(_divisibleByEight)

print('\n- - - -\n')

# --------------------------------------------------
# LESSON

print('\n\nLesson >> Find all of the numbers from 1-1000 that have a 6 in them:\n')

_nums = [_i for _i in range(1, 1001)]
_numsHaveSixInThem = [_num for _num in _nums if '6' in str(_num)]
print(_numsHaveSixInThem)

print('\n- - - -\n')

# --------------------------------------------------
# LESSON

print('\n\nLesson >> Count the number of spaces in a string:\n')

_phrase = 'Practice Problems to Drill List Comprehension in Your Head.'
print(_phrase)
print('Number of phrase spaces: ', len([_char for _char in _phrase if _char == ' ']))
