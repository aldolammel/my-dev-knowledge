"""

FUNCTIONS:

Function is a block of code that you can run at any point after it has been defined, and that produces an output
or performs an consulting-with-params.

"""

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'

# Pre-lessons:


def fnc_counter(_start=1, _end=10, _step=1):                # setting default values.

    """                                                     # my first docstring.
    Just a counter that shows the result on screen.
    :param _start: starts the counting.
    :param _end: ends the counting.
    :param _step: rithm of counting.
    :return: nothing.
    """

    _counter = _start
    while _counter <= _end:
        print(f'{_counter} ', end='')
        _counter += _step
    print('DONE!')


fnc_counter(10, 100, 2)                               # using other parameters values, and not the default ones instead.

help(fnc_counter)                                     # showing for what a docstring is awesome.

print('\n- - -\n')


def fnc_sum(_a=0, _b=0, _c=0):
    _sum = _a + _b + _c
    return _sum                                  # Building a function where I'm using 'return' instead of 'print()'.


_return1 = fnc_sum(10, 20, 30)
_return2 = fnc_sum(1, 3)
_return3 = fnc_sum(200)

print(f'My sum are {_return1}; {_return2}; and {_return3}.')


# ----------------------------------------
# LESSON 101:

# print('\n\nLesson 101 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_vote(_birthYear):
    from datetime import date                                  # saving memory 'cause it's loading only for this fnc.

    _currentYear = date.today().year
    _age = _currentYear - _birthYear

    if _age < 16:
        return 'You CANNOT vote yet!'
    elif 16 <= _age < 18 or _age >= 70:
        return 'You CAN vote!'
    else:
        return 'you MUST vote!'


_userBirthYear = int(input('Birth year: '))
print(fnc_vote(_userBirthYear))

# ----------------------------------------
# LESSON 102:

print('\n\nLesson 102 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_factorial(_numb, _show=False):
    """
    Calcs the factorial of a number.
    :param _numb: number to be factored.
    :param _show: (optional) shows or not the calc.
    :return: the value of Factorial of a number.
    """
    _factorial = 1

    for _i in range(_numb, 0, -1):
        if _show:
            if _i == _numb:
                print(f'{_i}', end='')
            else:
                print(f' x {_i}', end='')
            if _i == 1:
                print(' = ', end='')

        _factorial = _factorial * _i

    return _factorial


_userNumb = int(input('Type an integer to be factored (e.g 10): '))

print(f'{_corT}{fnc_factorial(_userNumb, _show=True)}{_corOut}')
help(fnc_factorial)

# ----------------------------------------
# LESSON 103:

print('\n\nLesson 103 >> Build a program that accepts the name and goals of a player, and accepts even when the both\n'
      'fields are empties. It doesnt matter the situation, always at the final it shows a message with who is\n'
      'the player and how many goals they got:\n')


def fnc_playerSheet(_name, _gols):

    if _name == '':
        _name = 'Unknown'
    if not _gols.isdigit():
        _gols = 0

    print(f'{_name} has {_gols} goals in the champion\'s league.')


_playerName = str(input('Name: ')).strip().upper()
_playerGoals = str(input('Goals amount: ')).strip()
fnc_playerSheet(_playerName, _playerGoals)

# ----------------------------------------
# LESSON 104:

print('\n\nLesson 104 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_readInteger(_txt):
    while True:
        _input = str(input(_txt))
        if _input.isnumeric():
            _input = int(_input)
            break
        else:
            print(f'{_corF}It is not an integer.{_corOut}')
    return _input


_number = fnc_readInteger('Type an integer: ')
print(f"Your number is {_corT}{_number}{_corOut}.")

# ----------------------------------------
# LESSON 105:

print('\n\nLesson 105 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_grades(* _grades, _status=False):
    """
    It analyses all grades of a student.
    :param _grades: each (one or further) grade note of a student.
    :param _status: student's average situation.
    :return: dictionary with the analyses of the student.
    """
    _student = dict()
    _student['Amount'] = len(_grades)
    _student['Biggest'] = max(_grades)
    _student['Lowest'] = min(_grades)
    _student['Average'] = sum(_grades) / len(_grades)

    if _status:
        if 0 <= _student['Average'] < 4:
            _student['Status'] = 'Awful'
        if 4 <= _student['Average'] < 6.5:
            _student['Status'] = 'Not good'
        if 6.5 <= _student['Average'] < 8.5:
            _student['Status'] = 'Okay'
        if 8.5 <= _student['Average'] <= 10:
            _student['Status'] = 'Excellent'

    return _student


print(fnc_grades(2.2, 7.5, 9.1, 6.3, _status=True))
help(fnc_grades)

# ----------------------------------------
# LESSON 106:

print('\n\nLesson 106 >> Build a program xxxxxxxxxxxxxx:\n')


def fnc_helper(_fnc):
    from time import sleep
    sleep(0.5)
    print(f'{_corT}', '-' * 20)
    print(f'HELPER: {_fnc.upper()}')
    print('-' * 20, f'{_corOut}')
    help(_fnc)
    print('--- end ---\n')


while True:
    _request = str(input('Type the command or library that you want to help: '))
    if _request.lower() != 'end':
        fnc_helper(_request)
    else:
        print(f'{_corF}The program is closing...{_corOut}', end=' ')
        print(f'{_corT}Done!{_corOut}')
        break
