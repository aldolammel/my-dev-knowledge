"""

DICTIONARY:
A set of key-value pairs. All keys must be unique.

Syntax: _myDict = { 'Name': 'Aldo', 'Age': 38, 'Location': 'Brazil' }

"""
from random import randint
from time import sleep
from operator import itemgetter
from datetime import date

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'


# Copy a dictionary:
original = {1: 'one', 2: 'two'}
new = original.copy()
print(f'Original: {original}\nNew: {new}')





# Pre-lessons:

_movie = {                          # this is a dictionary.
    'title': 'Star Wars',           # key: value
    'year': 1977,                   # key: value
    'Director': 'George Lucas'      # key: value
}

print(_movie.keys())                # shows only keys of the dictionary.
print(_movie.values())              # shows only values of the dictionary.
print(_movie.items())               # shows each couple of key and value separately by tuples.
print(_movie)                       # shows everything from the dictionary.

print('\n----\n')

for _key, _value in _movie.items():
    print(f'The {_key} is {_value}.')

print('\n----\n')

_people = {'Name': 'Aldo', 'Gender': 'Male', 'Age': 38}
print(_people)
print(f'{_people["Name"]} is {_people["Age"]} years old.')

print('\nShowing all keys from _people dictionary: ')
for _key in _people.keys():
    print(_key, end=' ')

print('\n')

print("EDITING dictionaries:")
del _people['Gender']                              # removing a key.
_people['Weight'] = 82.3                           # adding a key and its value
_people['Name'] = 'John'                           # changing a value.
for _key, _value in _people.items():               # for dictionaries, we don't use the ENUMERATE, but the ITEMS().
    print(f'{_key} = {_value}')

print('\n----\n')

print("CREATING dictionaries into an array:")
_europe = []
_country1 = {
    'Name': 'Czech Republic',
    'Currency': 'Koruna'
}
_country2 = {
    'Name': 'Spain',
    'Currency': 'Euro'
}
_europe.append(_country1)
_europe.append(_country2)

print(f'Array "_europe": {_corT}{_europe}{_corOut}')
print(f'First dictionary: {_europe[0]}')
print(f'Only name of that: {_europe[0]["Name"]}')

print('\n----\n')

print("COPYING dictionaries to array:")
_city = dict()
_rioGrandeDoSul = list()

for _i in range(2):
    _city['City'] = str(input('Name of the city: ')).strip().upper()
    _city['Mayor'] = str(input('Name of the mayor: ')).strip().upper()
    _rioGrandeDoSul.append(_city.copy())                                # dictionary CANNOT use slicing to make copies.

print(f'\n{_rioGrandeDoSul}\n')

for _eachCity in _rioGrandeDoSul:                     # FOR to array.
    for _key, _value in _eachCity.items():            # FOR to dictionary.
        print(f'{_key}: {_value}')
    print()

# ----------------------------------------
# LESSON 090:

print('\n\nLesson 090 >> Build a program capable to read the name and grade average of one student and, at last,'
      'show those information:\n')

_person = dict()                                                    # empty dictionary.

_person['Name'] = str(input('Name: ')).strip().upper()              # populating the dict _person.
_person['Average'] = float(input('Grade average: '))

if _person['Average'] >= 7:
    _person['Status'] = 'approved'
elif 5 <= _person['Average'] < 7:
    _person['Status'] = 'new exam is needed'
else:
    _person['Status'] = 'rejected'

print(
    '- ' * 20,
    f'\n >> Student: {_person["Name"]}'
    f'\n >> Grade average: {_person["Average"]}'
    f'\n >> Status: {_person["Status"]}'
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

for _key, _value in _game.items():
    print(f'{_key} has a {_value}.')
    sleep(0.5)

_ranking = sorted(_game.items(), key=itemgetter(1), reverse=True)              # to sorting a dictionary!

print('\n--- SCOREBOARD ---')
for _i, _tuple in enumerate(_ranking):
    print(f'{_i + 1}# place: {_tuple[0]} with {_corT}{_tuple[1]}{_corOut}.')

# ----------------------------------------
# LESSON 092:

print('\n\nLesson 092 >> Build a program xxxxxxxxxxxxxxxxx:\n')

_people = dict()

_people['Name'] = str(input('Name: ')).strip().upper()
_birth = int(input('Birth year: '))
_people['Age'] = date.today().year - _birth
_people['WorkNumber'] = int(input('(If not available, type 0) Work number: '))

if _people['WorkNumber'] != 0:
    _people['Hire'] = int(input('Year of hire: '))
    _people['Earnings'] = float(input('Monthly earnings: R$'))
    _people['Retirement'] = (_people['Hire'] - _birth) + 35

print('---------------')

for _key, _value in _people.items():            # shows each couple of key and value separately by tuples.
    print(f'{_key} is {_value}.')

# ----------------------------------------
# LESSON 093:

print('\n\nLesson 093 >> Build a program that asks for a soccer player and how many goals they have in their carrier.'
      'After that, shows up a basic analyses of each player\'s match:\n')

_soccerPlayer = dict()
_arrayGoals = []

_soccerPlayer['Name'] = str(input('Name: ')).strip().upper()
_matches = int(input(f'How many matches did {_soccerPlayer["Name"]} play: '))

if _matches != 0:
    for _i in range(_matches):
        _goals = int(input(f'How many goals in the match#{_i + 1}: '))
        _arrayGoals.append(_goals)
        _soccerPlayer['Goals'] = _arrayGoals[:]
        _soccerPlayer['TotalGoals'] = sum(_arrayGoals)                  # NEW: summing all values in _arrayGoals.
    for _key, _value in _soccerPlayer.items():                          # remember: dict doest use enumarate command.
        print(f'{_corT}{_key}{_corOut} is {_corT}{_value}{_corOut}.')

    print(f'\n{_soccerPlayer["Name"]} has played {_matches} matches:')
    for _match, _goals in enumerate(_arrayGoals):
        print(f'  >> In match#{_match + 1}, they did {_goals} goal(s).')
    print(f'Total of goals so far: {_corT}{_soccerPlayer["TotalGoals"]}{_corOut}')

else:
    print(f'{_corF}This player has no soccer carrier yet!{_corOut}')

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
        print(f'{_corF}Invalid choice!{_corOut}')
        _eachPerson['Gender'] = str(input('Gender [M/F]: ')).strip().upper()[0]

    _eachPerson['Age'] = int(input('Age: '))
    _ageTotal += _eachPerson['Age']
    _everybody.append(_eachPerson.copy())

    while True:
        _keepRecording = str(input('Add someone else [Y/N]: ')).strip().upper()[0]
        if _keepRecording not in 'YN':
            print(f'{_corF}Invalid choice!{_corOut}')
        else:
            break

    if _keepRecording == 'N':
        break

print('\n', _everybody)
print(f'A) We got {_corT}{len(_everybody)}{_corOut} people recorded. ')
print(f'B) Age average is {_corT}{_ageTotal / len(_everybody):.1f} years{_corOut}.')
print(f'C) There are theses females recorded: ', end='')
for _dict in _everybody:
    if _dict['Gender'] == 'F':
        print(f'{_corT}{_dict["Name"]}{_corOut}', end=', ')

print('\nD) List of people that are over the age average:')
for _dict in _everybody:
    if _dict['Age'] > (_ageTotal / len(_everybody)):
        for _key, _value in _dict.items():
            print(f'{_corT}{_key} = {_value}{_corOut}', end=' >> ')
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
            print(f'{_corF}Invalid answer! Try again!{_corOut}\n')
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
for _key, _val in enumerate(_team):
    print(f'{_key:>3} ', end='')
    for _data in _val.values():
        print(f'{str(_data):<15}', end='')
    print()

while True:
    _summaryNum = int(input('\n[-1 to exit] What player\'s (summary CODE) do you want to analyse: '))

    if _summaryNum <= -1:
        break
    elif _summaryNum >= len(_team):
        print(f'{_corF}Invalid summary code! Try again:{_corOut}')
    else:
        print(f'\nAnalysing {_corT}{_team[_summaryNum]["Name"]}{_corOut}:')
        if len(_team[_summaryNum]['Goals']) == 0:
            print(f'{_corF}This player has no matches in their carrier!{_corOut}')
        else:
            for _match, _goal in enumerate(_team[_summaryNum]['Goals']):
                print(f'    >> In match#{_match + 1}, they got {_corT}{_goal}{_corOut} goal(s).')
        print('- - - -')

print('\nPROGRAM HAS BEEN FINISHED!')
