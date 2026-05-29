"""
ERRORS: EXAMPLE OF RAISING ERROR:
This type of error handling is useful for devs who will maintain a system and need they own custom error messages.

Note that if the user_choice is a negative integer, it will raise a custom error message:

"""


def int_checker(n):
    if n < 0:
        raise ValueError(f'The integer {n} is a negative one. Only type positive integer.')
    for i in range(n + 1):
        print(i, end=' ')
    print('Done!')


user_choice = int(input('An integer number (type a negative one to raise an custom error): '))
int_checker(user_choice)
