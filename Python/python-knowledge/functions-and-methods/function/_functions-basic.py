"""

FUNCTIONS /  METHODS:

Function is a block of code that you can run at any point after it has been defined, and that produces an output
or performs a consulting-with-params.

"""

# MY COLORS
cT = '\033[1;32m'
cF = '\033[1;31m'
cOut = '\033[m'

# Pre-lessons:


def counter(start=1, end=10, step=1):                # setting default values.

    """                                                     # my first docstring.
    Just a counter that shows the result on screen.
    :param start: starts the counting.
    :param end: ends the counting.
    :param step: rithm of counting.
    :return: nothing.
    """

    ctrl = start
    while ctrl <= end:
        print(f'{ctrl} ', end='')
        ctrl += step
    print('DONE!')


counter(10, 100, 2)                               # using other parameters values, and not the default ones instead.

help(counter)                                     # showing for what a docstring is awesome.

print('\n- - -\n')


def summation(a=0, b=0, c=0):
    s = a + b + c
    return s                                  # Building a function where I'm using 'return' instead of 'print()'.


return1 = summation(10, 20, 30)
return2 = summation(1, 3)
return3 = summation(200)

print(f'My sum are {return1}; {return2}; and {return3}.')


# ----------------------------------------
# LESSON 101:

# print('\n\nLesson 101 >> Build a program xxxxxxxxxxxxxx:\n')


def vote(birth_year):
    from datetime import date                                  # saving memory 'cause it's loading only for this fnc.

    currentYear = date.today().year
    age = currentYear - birth_year

    if age < 16:
        return 'You CANNOT vote yet!'
    elif 16 <= age < 18 or age >= 70:
        return 'You CAN vote!'
    else:
        return 'you MUST vote!'


user_birth_year = int(input('Birth year: '))
print(vote(user_birth_year))

# ----------------------------------------
# LESSON 102:

print('\n\nLesson 102 >> Build a program xxxxxxxxxxxxxx:\n')


def factorial(n, show=False):
    """
    Calcs the factorial of a number.
    :param n: number to be factored.
    :param show: (optional) shows or not the calc.
    :return: the value of Factorial of a number.
    """
    factorial = 1

    for i in range(n, 0, -1):
        if show:
            if i == n:
                print(f'{i}', end='')
            else:
                print(f' x {i}', end='')
            if i == 1:
                print(' = ', end='')

        factorial = factorial * i

    return factorial


userNum = int(input('Type an integer to be factored (e.g 10): '))

print(f'{cT}{factorial(userNum, show=True)}{cOut}')
help(factorial)

# ----------------------------------------
# LESSON 103:

print('\n\nLesson 103 >> Build a program that accepts the name and goals of a player, and accepts even when the both\n'
      'fields are empties. It doesnt matter the situation, always at the final it shows a message with who is\n'
      'the player and how many goals they got:\n')


def player_sheet(name, gols):

    if name == '':
        name = 'Unknown'
    if not gols.isdigit():
        gols = 0

    print(f'{name} has {gols} goals in the champion\'s league.')


playerName = str(input('Name: ')).strip().upper()
playerGoals = str(input('Goals amount: ')).strip()
player_sheet(playerName, playerGoals)

# ----------------------------------------
# LESSON 104:

print('\n\nLesson 104 >> Build a program xxxxxxxxxxxxxx:\n')


def read_integer(_txt):
    while True:
        inpt = str(input(_txt))
        if inpt.isnumeric():
            inpt = int(inpt)
            break
        else:
            print(f'{cF}It is not an integer.{cOut}')
    return inpt


num = read_integer('Type an integer: ')
print(f"Your number is {cT}{num}{cOut}.")

# ----------------------------------------
# LESSON 105:

print('\n\nLesson 105 >> Build a program xxxxxxxxxxxxxx:\n')


def grades(* grades, status=False):
    """
    It analyses all grades of a student.
    :param grades: each (one or further) grade note of a student.
    :param status: student's average situation.
    :return: dictionary with the analyses of the student.
    """
    student = dict()
    student['Amount'] = len(grades)
    student['Biggest'] = max(grades)
    student['Lowest'] = min(grades)
    student['Average'] = sum(grades) / len(grades)

    if status:
        if 0 <= student['Average'] < 4:
            student['Status'] = 'Awful'
        if 4 <= student['Average'] < 6.5:
            student['Status'] = 'Not good'
        if 6.5 <= student['Average'] < 8.5:
            student['Status'] = 'Okay'
        if 8.5 <= student['Average'] <= 10:
            student['Status'] = 'Excellent'

    return student


print(grades(2.2, 7.5, 9.1, 6.3, status=True))
help(grades)

# ----------------------------------------
# LESSON 106:

print('\n\nLesson 106 >> Build a program xxxxxxxxxxxxxx:\n')


def helper(fnc):
    from time import sleep
    sleep(0.5)
    print(f'{cT}', '-' * 20)
    print(f'HELPER: {fnc.upper()}')
    print('-' * 20, f'{cOut}')
    help(fnc)
    print('--- end ---\n')


while True:
    userRequest = str(input('Type the command or library that you want to help: '))
    if userRequest.lower() != 'end':
        helper(userRequest)
    else:
        print(f'{cF}The program is closing...{cOut}', end=' ')
        print(f'{cT}Done!{cOut}')
        break
