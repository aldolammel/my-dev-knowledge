"""
HANDLING EXCEPTIONS (TRATAMENTO DE ERROS):

Exceptions are used to prevent a generic error messages and the software to stop suddenly.

Traceback message = The part of the error message that tells us the lines of code where the error happened and
the functions calls that took place.

"""

import urllib
import urllib.request

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'


# Pre-lesson:

try:
    _a = int(input('Type an integer: '))
    _b = float(input('Type a float: '))
    _result = _a / _b

except ZeroDivisionError:                               # will be shown only if this error/exception take place.
    print(f'{_corF}Impossible to divide a number by zero.{_corOut}')

except Exception as _error:                             # will be shown after any error/exception not listed above.
    print(f'Something ran wrong: {_corF}{_error}{_corOut}')

else:                                                   # will be shown when everything is alright.
    print(f'The result is: {_result:.1f}')

finally:                                                # after all, this always will take place.
    print('Bye')


# -------------------------------------------------------------------------
# LESSON 113:

print('\n\nLesson 113 >> Built a program that use a handler error:\n')


def fnc_integer_reader(_txt):
    global _error
    while True:
        try:
            _num = int(input(_txt))
        except (ValueError, TypeError):
            print(f'Error: {_corF}You must type an integer.{_corOut}')
        except KeyboardInterrupt:
            print(f'\n{_corF}The program was interrupted.{_corOut}')
            return 0
        except Exception as _error:
            print(f'Error: {_corF}{_error}{_corOut}')
        else:
            return _num


def fnc_float_reader(_txt):
    while True:
        try:
            _num = float(input(_txt))
        except (ValueError, TypeError):
            print(f'{_corF}You must type a float.{_corOut}')
        except KeyboardInterrupt:
            print(f'\n{_corF}The program was interrupted.{_corOut}')
            return 0
        except Exception as _error:
            print(f'Error: {_corF}{_error}{_corOut}')
        else:
            return _num


_userInteger = fnc_integer_reader('Type an integer: ')
_userFloat = fnc_float_reader('Type a float number: ')
print(f'Your integer is {_corT}{_userInteger}{_corOut} and your float is {_corT}{_userFloat}{_corOut}.')

# -------------------------------------------------------------------------
# LESSON 114:

print('\n\nLesson 114 >> Built a program that test the connection with any website:\n')

try:
    _url = urllib.request.urlopen('https://aldolammel.com')
except urllib.error.URLError:
    print(f'{_corF}It looks without internet signal or something like that!{_corOut}')

except Exception as _error:
    print(f'Error: {_corF}{_error}{_corOut}')
else:
    print(f'{_corT}The URL seems to work fine!{_corOut}')
