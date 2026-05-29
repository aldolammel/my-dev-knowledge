"""
HANDLING EXCEPTIONS (TRATAMENTO DE ERROS):

Exceptions are used to prevent a generic error messages and the software to stop suddenly.

Traceback message = The part of the error message that tells us the lines of code where the error happened and
the functions calls that took place.

MORE IN DRA. ANGELA LEE's COURSE:
https://www.udemy.com/course/100-days-of-code/learn/lecture/20963160#overview

"""

import urllib
import urllib.request

# MY COLORS
corT = '\033[1;32m'
corF = '\033[1;31m'
corOut = '\033[m'


# Pre-lesson:

try:
    a = int(input('Type an integer: '))
    b = float(input('Type a float: '))
    the_result = a / b

except ZeroDivisionError:                               # will be shown only if this error/exception take place.
    print(f'{corF}Impossible to divide a number by zero.{corOut}')

except Exception as erro:                             # will be shown after any error/exception not listed above.
    print(f'Something ran wrong: {corF}{erro}{corOut}')

else:                                                   # will be shown when everything is alright.
    print(f'The result is: {the_result:.1f}')

finally:                                                # after all, this always will take place.
    print('Bye')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# LESSON 113:

print('\n\nLesson 113 >> Built a program that use a handler error:\n')


def fnc_integer_reader(_txt):
    global erro
    while True:
        try:
            num = int(input(_txt))
        except (ValueError, TypeError):
            print(f'Error: {corF}You must type an integer.{corOut}')
        except KeyboardInterrupt:
            print(f'\n{corF}The program was interrupted.{corOut}')
            return 0
        except Exception as erro:
            print(f'Error: {corF}{erro}{corOut}')
        else:
            return num


def fnc_float_reader(_txt):
    while True:
        try:
            num = float(input(_txt))
        except (ValueError, TypeError):
            print(f'{corF}You must type a float.{corOut}')
        except KeyboardInterrupt:
            print(f'\n{corF}The program was interrupted.{corOut}')
            return 0
        except Exception as erro:
            print(f'Error: {corF}{erro}{corOut}')
        else:
            return num


user_int = fnc_integer_reader('Type an integer: ')
user_float = fnc_float_reader('Type a float number: ')
print(f'Your integer is {corT}{user_int}{corOut} and your float is {corT}{user_float}{corOut}.')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# LESSON 114:

print('\n\nLesson 114 >> Built a program that test the connection with any website:\n')

try:
    url = urllib.request.urlopen('https://aldolammel.com')
except urllib.error.URLError:
    print(f'{corF}It looks without internet signal or something like that!{corOut}')

except Exception as erro:
    print(f'Error: {corF}{erro}{corOut}')
else:
    print(f'{corT}The URL seems to work fine!{corOut}')
