# TRAINING TO USE VARIABLE:

_name = str(input('What\'s your name? '))
_lastName = str(input('What\'s your lastname? '))
_age = int(input('How old are you? '))
_gender = bool(input('Are you a woman? '))
_armaMod = str(input('Which Arma mod do you like the most? '))

print(
      'Their fullname is {} {}, {} years old, a {} who love {}, '
      'a mod of Arma 3.'.format(_name, _lastName, _age, _gender, _armaMod)
)

print('Now, let\'s check our variables _armaMod that\'s named as', _armaMod, ':')
print('Which type is _armaMod variable? ', type(_armaMod))
print('Is it numeric? ', _armaMod.isnumeric())
print('Is it alphanumeric? ', _armaMod.isalnum())
print('Is it uppercase? ', _armaMod.isupper())
print('Is it lowercase? ', _armaMod.islower())