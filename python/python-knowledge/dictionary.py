
"""
    DICTIONARY:
        A set of key-value pairs. All keys must be unique.

        >> Syntax:
            _myDict = { 'Name': 'Aldo', 'Age': 38, 'Location': 'Brazil' }

        >> Dictionary Comprehension:
            ./dict-comprehension.py
"""

from random import randint
from time import sleep
from operator import itemgetter
from datetime import date

# MY COLORS
corT = '\033[1;32m'
corF = '\033[1;31m'
corOut = '\033[m'


# Copy a dictionary:
original = {1: 'one', 2: 'two'}
new = original.copy()
print(f'Original: {original}\nNew: {new}')


# Pre-lessons:

movie = {                          # this is a dictionary.
    'title': 'Star Wars',           # key: value
    'year': 1977,                   # key: value
    'Director': 'George Lucas'      # key: value
}

print(movie.keys())                # shows only keys of the dictionary.
print(movie.values())              # shows only values of the dictionary.
print(movie.items())               # shows each couple of key and value separately by tuples.
print(movie)                       # shows everything from the dictionary.


for key_, value_ in movie.items():
    print(f'The {key_} is {value_}.')


person = {'Name': 'Aldo', 'Gender': 'Male', 'Age': 38}
print(person)
print(f'{person["Name"]} is {person["Age"]} years old.')

print('\nShowing all keys from person dictionary: ')
for key_ in person.keys():
    print(key_, end=' ')


print("EDITING dictionaries:")
del person['Gender']                              # removing a key.
person['Weight'] = 82.3                           # adding a key and its value
person['Name'] = 'John'                           # changing a value.
for key_, value_ in person.items():               # for dictionaries, we don't use the ENUMERATE, but the ITEMS().
    print(f'{key_} = {value_}')


print("CREATING dictionaries into an array:")
europe = []
country1 = {
    'Name': 'Czech Republic',
    'Currency': 'Koruna'
}
country2 = {
    'Name': 'Spain',
    'Currency': 'Euro'
}
europe.append(country1)
europe.append(country2)

print(f'Array "europe": {corT}{europe}{corOut}')
print(f'First dictionary: {europe[0]}')
print(f'Only name of that: {europe[0]["Name"]}')


print("COPYING dictionaries to array:")
city = dict()
state = list()

for i in range(2):
    city['City'] = str(input('Name of the city: ')).strip().upper()
    city['Mayor'] = str(input('Name of the mayor: ')).strip().upper()
    state.append(city.copy())                                # dictionary CANNOT use slicing to make copies.

print(f'\n{state}\n')

for city in state:                     # FOR to array.
    for key_, value_ in city.items():            # FOR to dictionary.
        print(f'{key_}: {value_}')
    print()

# ----------------------------------------
# LESSON 090:

print('\n\nLesson 090 >> Build a program capable to read the name and grade average of one student and, at last,'
      'show those information:\n')

person = dict()                                                    # empty dictionary.

person['Name'] = str(input('Name: ')).strip().upper()              # populating the dict person.
person['Average'] = float(input('Grade average: '))

if person['Average'] >= 7:
    person['Status'] = 'approved'
elif 5 <= person['Average'] < 7:
    person['Status'] = 'new exam is needed'
else:
    person['Status'] = 'rejected'

print(
    '- ' * 20,
    f'\n >> Student: {person["Name"]}'
    f'\n >> Grade average: {person["Average"]}'
    f'\n >> Status: {person["Status"]}'
)

# ----------------------------------------
# LESSON 091:

print('\n\nLesson 091 >> Build a program that automatically rolls the dice for four players and, at last,'
      ' shows the scoreboard with sorted results:\n')

_game = {
    'John': randint(1, 6),
    'Bill': randint(1, 6),
    'Anna': randint(1, 6),
    'Fred': randint(1, 6)
}
_ranking = list()
_higherScore = 0

for key_, value_ in _game.items():
    print(f'{key_} has a {value_}.')
    sleep(0.5)

_ranking = sorted(_game.items(), key=itemgetter(1), reverse=True)              # to sorting a dictionary!

print('\n--- SCOREBOARD ---')
for i, _tuple in enumerate(_ranking):
    print(f'{i + 1}# place: {_tuple[0]} with {corT}{_tuple[1]}{corOut}.')

# ----------------------------------------
# LESSON 092:

print('\n\nLesson 092 >> Build a program xxxxxxxxxxxxxxxxx:\n')

person = dict()

person['Name'] = str(input('Name: ')).strip().upper()
_birth = int(input('Birth year: '))
person['Age'] = date.today().year - _birth
person['WorkNumber'] = int(input('(If not available, type 0) Work number: '))

if person['WorkNumber'] != 0:
    person['Hire'] = int(input('Year of hire: '))
    person['Earnings'] = float(input('Monthly earnings: R$'))
    person['Retirement'] = (person['Hire'] - _birth) + 35

print('---------------')

for key_, value_ in person.items():            # shows each couple of key and value separately by tuples.
    print(f'{key_} is {value_}.')

# ----------------------------------------
# LESSON 093:

print('\n\nLesson 093 >> Build a program that asks for a soccer player and how many goals they have in their carrier.'
      'After that, shows up a basic analyses of each player\'s match:\n')

_soccerPlayer = dict()
_arrayGoals = []

_soccerPlayer['Name'] = str(input('Name: ')).strip().upper()
_matches = int(input(f'How many matches did {_soccerPlayer["Name"]} play: '))

if _matches != 0:
    for i in range(_matches):
        _goals = int(input(f'How many goals in the match#{i + 1}: '))
        _arrayGoals.append(_goals)
        _soccerPlayer['Goals'] = _arrayGoals[:]
        _soccerPlayer['TotalGoals'] = sum(_arrayGoals)                  # NEW: summing all values in _arrayGoals.
    for key_, value_ in _soccerPlayer.items():                          # remember: dict doest use enumarate command.
        print(f'{corT}{key_}{corOut} is {corT}{value_}{corOut}.')

    print(f'\n{_soccerPlayer["Name"]} has played {_matches} matches:')
    for _match, _goals in enumerate(_arrayGoals):
        print(f'  >> In match#{_match + 1}, they did {_goals} goal(s).')
    print(f'Total of goals so far: {corT}{_soccerPlayer["TotalGoals"]}{corOut}')

else:
    print(f'{corF}This player has no soccer carrier yet!{corOut}')

# ----------------------------------------
# LESSON 094:

print('\n\nLesson 094 >> Build a program xxxxxxxxxxxxxxxxx:')

_everybody = list()
_eachPerson = dict()
_ageTotal = 0

while True:
    _eachPerson['Name'] = str(input('\nName: ')).strip().upper()

    _eachPerson['Gender'] = str(input('Gender [M/F]: ')).strip().upper()[0]
    while _eachPerson['Gender'] not in 'MF':
        print(f'{corF}Invalid choice!{corOut}')
        _eachPerson['Gender'] = str(input('Gender [M/F]: ')).strip().upper()[0]

    _eachPerson['Age'] = int(input('Age: '))
    _ageTotal += _eachPerson['Age']
    _everybody.append(_eachPerson.copy())

    while True:
        _keepRecording = str(input('Add someone else [Y/N]: ')).strip().upper()[0]
        if _keepRecording not in 'YN':
            print(f'{corF}Invalid choice!{corOut}')
        else:
            break

    if _keepRecording == 'N':
        break

print('\n', _everybody)
print(f'A) We got {corT}{len(_everybody)}{corOut} people recorded. ')
print(f'B) Age average is {corT}{_ageTotal / len(_everybody):.1f} years{corOut}.')
print(f'C) There are theses females recorded: ', end='')
for _dict in _everybody:
    if _dict['Gender'] == 'F':
        print(f'{corT}{_dict["Name"]}{corOut}', end=', ')

print('\nD) List of people that are over the age average:')
for _dict in _everybody:
    if _dict['Age'] > (_ageTotal / len(_everybody)):
        for key_, value_ in _dict.items():
            print(f'{corT}{key_} = {value_}{corOut}', end=' >> ')
        print()

print('\n\n--- FINISHED ---')

# ----------------------------------------
# LESSON 095:

print('\n\nLesson 095 >> Build a program xxxxxxxxxxxxxxxxx:')

_team = list()
_player = dict()
_goals = list()

while True:
    _player['Name'] = str(input('\nName: ')).strip().upper()
    _player['Matches'] = int(input(f'How many matches {_player["Name"]} did play: '))

    if _player['Matches'] > 0:
        for _match in range(_player['Matches']):
            _goals.append(int(input(f'    >> How many goals in match#{_match + 1}: ')))
    _player['Goals'] = _goals[:]
    _player['TotalGoals'] = sum(_goals)
    _team.append(_player.copy())
    _goals.clear()
    _player.clear()

    while True:
        _keepRecording = str(input('Add someone else [Y/N]: ')).strip().upper()[0]
        if _keepRecording in 'YN':
            break
        else:
            print(f'{corF}Invalid answer! Try again!{corOut}\n')
    if _keepRecording == 'N':
        break

print(
    f'\n------------------ DEBUG INFO ---------------------'
    f'\n_team = {_team}'
    f'\n_player = {_player}'
    f'\n_goals = {_goals}'
    f'\n---------------------------------------------------\n'
)

print(f'{str("COD"):<4}{str("NAME"):<15}{str("MATCHES"):<15}{str("GOALS"):<15}{str("TOTAL"):<6}')
for key_, _val in enumerate(_team):
    print(f'{key_:>3} ', end='')
    for _data in _val.values():
        print(f'{str(_data):<15}', end='')
    print()

while True:
    _summaryNum = int(input('\n[-1 to exit] What player\'s (summary CODE) do you want to analyse: '))

    if _summaryNum <= -1:
        break
    elif _summaryNum >= len(_team):
        print(f'{corF}Invalid summary code! Try again:{corOut}')
    else:
        print(f'\nAnalysing {corT}{_team[_summaryNum]["Name"]}{corOut}:')
        if len(_team[_summaryNum]['Goals']) == 0:
            print(f'{corF}This player has no matches in their carrier!{corOut}')
        else:
            for _match, _goal in enumerate(_team[_summaryNum]['Goals']):
                print(f'    >> In match#{_match + 1}, they got {corT}{_goal}{corOut} goal(s).')
        print('- - - -')

print('\nPROGRAM HAS BEEN FINISHED!')
