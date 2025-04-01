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

# ..................................................................................................

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

# ..................................................................................................

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

# ..................................................................................................

# SETTING THE FIRST LETTER NAME AS A UPPERCASE:
_friends = ['billy', 'bob', 'mike', 'linda', 'stephen']
print([_name.title() for _name in _friends])

print('\n- - - -\n')

# ..................................................................................................

# LIST COMPREHENSION WITH F-STRINGS:

_friendsAges = [20, 32, 19, 24]
print(_friendsAges)

_newListAgeStrings = [f'My friend is {_age} years old.' for _age in _friendsAges]
print(_newListAgeStrings)

print('\n- - - -\n')

# ..................................................................................................
# LESSON

print('\n\nLesson >> Find all of the numbers from 1-1000 that are divisible by 8:\n')

_divisibleByEight = [_num for _num in range(1, 1001) if _num % 8 == 0]
print(_divisibleByEight)

print('\n- - - -\n')

# ..................................................................................................
# LESSON

print('\n\nLesson >> Find all of the numbers from 1-1000 that have a 6 in them:\n')

_nums = [_i for _i in range(1, 1001)]
_numsHaveSixInThem = [_num for _num in _nums if '6' in str(_num)]
print(_numsHaveSixInThem)

print('\n- - - -\n')

# ..................................................................................................
# LESSON

print('\n\nLesson >> Count the number of spaces in a string:\n')

_phrase = 'Practice Problems to Drill List Comprehension in Your Head.'
print(_phrase)
print('Number of phrase spaces: ', len([_char for _char in _phrase if _char == ' ']))


"""

LIST COMPREHENSION with DICTIONARIES / DICTIONARY COMPREHENSION

At first:
WITH LIST OUTPUT: obj = [ comprehension syntax here ]
WITH DICTIONARY OUTPUT: obj = { comprehension syntax here } <-- Curly Brackets

SYNTAX EXAMPLE:
new_dictionary = { new_key: new_value FOR (key, value) IN original_dictionary.items() }

"""
from random import randint

print(">> CREATING A SIMPLE DICTIONARY AND PRINT IT OUT:")
friends = ['Rolf', 'Julie', 'Anton', 'Paul']
time_since_seen = [3, 6, 19, 23]
timer = {friends[i]: time_since_seen[i] for i in range(len(friends))}     # List comprehension with dict.
print(timer)

print('\n- - - -\n')

# ..................................................................................................

print(">> CREATING A DICT OF STUDENTS' SCORE RANDOMLY AND, AFTER, SHOW ONLY THOSE WITH SCORE 6 OR HIGHER:")
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]  # Students
students_scores = {student: randint(1, 10) for student in names}    # Creating randomly the student's scores
print(students_scores)                                              # print it out to review
print('\nPassed students (score 6 or higher):')
passed_students = {student: score for (student, score) in students_scores.items() if score >= 6}
_ = [print(f'{key}: {value}') for (key, value) in passed_students.items()]

print('\n- - - -\n')

# ..................................................................................................

print(">> CREATE A DICT WITH THE NUMBER OF LETTERS FROM EACH WORD PRESENTS IN THE SENTENCE BELOW:")
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
print(sentence)

result = {word: len(word) for word in sentence.split()}
print(result)

print('\n- - - -\n')

# ..................................................................................................

print(">> CREATE A NEW DICT BY CONVERTING CELSIUS TO FAHRENHEIT TEMPERATURES:")
weather_c = {"Mon": 12, "Tue": 14, "Wed": 15, "Thu": 14, "Fri": 21, "Sat": 22, "Sun": 24}

# Traditional way to convert it:
"""weather_f = dict()
for (key, value) in weather_c.items():
    fahrenheit = (value * 9 / 5) + 32
    weather_f[key] = fahrenheit"""

# Dictionary comprehension method:
weather_f = {key: (value * 9 / 5) + 32 for (key, value) in weather_c.items()}

print(weather_f)

print('\n- - - -\n')

# ..................................................................................................
