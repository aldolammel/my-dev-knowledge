"""

LIST (ARRAY):
Most flexible container to carry information.

Syntax: _myList = [['Aldo', 38, 'Brazil], ['Anna', 22, 'Cyprus']]

Empty list: _myList = list()    or    _myList = []

Converting to List = _myList = list(_myTuple)

"""

# MY COLORS
corInSucc = '\033[1;32m'
corInFail = '\033[1;31m'
corOut = '\033[m'

# Pre-lessons:

# Modifying/Replacing the position 0 in _array:
_array = [1, 2, 3, 4]
print('Original list:', _array)
_array[0] = 9
print('Replacing the num in pos 0 (num 1 for 9):', _array)

print('\n---\n')

# adding a number:
_arrayAdding = [1, 2, 3, 4]
print('Original _arrayAdding:', _arrayAdding)
_arrayAdding.append(10)                                             # always for the last position.
print('After adding a new value:', _arrayAdding)

print('\n---\n')

# Finding a position of the value in the list through its index:
_animals = ['cat', 'dog', 'rabbit', 'horse', 'dinosaur', 'bird']
_posDino = _animals.index('dinosaur')
print('The value "dinosaur" in the _animals list is the position:', _posDino)

print('\n---\n')

# Inserting a new position in the list index:
_arrayInserting = [1, 2, 3, 4]
print('Original _arrayInserting:', _arrayInserting)
_arrayInserting.insert(0, 7)                                    # it changes the index of list, opening a new position.
print('Inserting in the pos 0 the num 7:', _arrayInserting)

print('\n---\n')

# sorting the array from back to front:
print('Original list with no sorting: ', _array)
_array.sort(reverse=True)
print('Sorting and reversing the list:', _array)

print('\n---\n')

# deleting always the value in the last position:
_arrayDeleting = [1, 2, 3, 4]
print('Original _arrayDeleting:', _arrayDeleting)
_arrayDeleting.pop()
print('After deleting the last value:', _arrayDeleting)

print('\n---\n')

# deleting the number in a specific position:
_arrayDelPos = [1, 2, 3]
print('Original _arrayDelPos:', _arrayDelPos)
del _arrayDelPos[0]
print('Deleting the num in pos 0:', _arrayDelPos)

print('\n---\n')

# deleting a specific value, doesn't matter the position it is:
_listRemoving = [20, 30, 40, 50]
print('Original _listRemoving:', _listRemoving)
_listRemoving.remove(40)
print('Removing the value "40", doesnt matter its position in _listRemoving index:', _listRemoving)

print('\n---\n')

# creating a new array and detecting which value is in which position:
_newArray = list()     # the same of '_newArray = []'
_newArray.append(4)
_newArray.append(6)
_newArray.append(13)

print(f'\n{_newArray}')

for pos, i in enumerate(_newArray):
    print(f'Position {pos} is value {i}')

print('\n---\n')

# creating a new array with user inputs:
_arrayWithInputs = []

for i in range(0, 5):
    _arrayWithInputs.append(int(input('Type an integer: ')))

print(_arrayWithInputs)

print('\n---\n')

# DUPLICATE/COPY AN ARRAY - NEVER WILL WORK - associating an array with another one (It is NOT a copy in Python):
_arrayAA = [1, 2, 3]
_arrayBB = _arrayAA
print(f'\nArray A: {_arrayAA}')
print(f'Array B: {_arrayBB}')
_arrayBB[0] = 9                 # the association makes the 9 get into the both arrays :(
print(f'Array A after changing: {_arrayAA}')
print(f'Array B after changing: {_arrayBB}')

print('\n---\n')

# DUPLICATE/COPY AN ARRAY - RIGHT WAY TO DO A DUPLICATE:
_arrayCC = [1, 2, 3]
_arrayDD = _arrayCC[:]          # slicing method, here i'm saying to bring all values from an array to the other.
print(f'Array C: {_arrayCC}')
print(f'Array D: {_arrayDD}')
_arrayDD[0] = 9
print(f'\nArray C: {_arrayCC}')
print(f'Array D after changing (works properly): {_arrayDD}')

print('\n---\n')

# Lists inside a list:
_list1 = [1, 2, 3]
_list2 = [4, 5, 6]
_list3 = [_list1, _list2]
print('_list1:', _list1)
print('_list2:', _list2)
print('The _list3 has the _list1 and _list2 within. _list3:', _list3)

# --------------------------------------------------
# LESSON 78

print('\nLesson 078 >> Build a program that receives and saves 5 integers and present the highest and lowest number'
      'in that array with its reference positions in there:\n')

_mainArray = []
_posHighest = []
_posLowest = []

for i in range(0, 5):
    _mainArray.append(int(input(f'Type an integer: ')))

for pos, _val in enumerate(_mainArray):
    if _val == max(_mainArray):
        _posHighest.append(pos)
    if _val == min(_mainArray):
        _posLowest.append(pos)

print(f'\nTyped values: {corInSucc}{_mainArray}{corOut}')
print(f'Highest value: {corInSucc}{max(_mainArray)}{corOut} (positions: {corInSucc}{_posHighest}{corOut})')
print(f'Lowest value: {corInSucc}{min(_mainArray)}{corOut} (positions: {corInSucc}{_posLowest}{corOut})')

# --------------------------------------------------
# LESSON 079

print('\n\nLesson 079 >> Build a program xxxxx:\n')

numbers = list()

while True:

    user_choice = int(input('Type an integer (or 0 to exit): '))

    if user_choice == 0:
        break

    elif user_choice not in numbers:
        numbers.append(user_choice)

print(f'\nYour array: {corInSucc}{sorted(numbers)}{corOut}')

# --------------------------------------------------
# LESSON 080 (EXTREMELY HARD THIS ONE):

print('\n\nLesson 080 >> Build a program that sort 5 numbers without using any sorting function:\n')

no_sort = list()

for i in range(0, 5):
    user_input = int(input('Type an integer: '))

    if i == 0 or user_input > no_sort[-1]:    # this '-1' is equal to last object inside the array.
        no_sort.append(user_input)
        print('Added at last position...')
    else:
        pos = 0
        while pos < len(no_sort):
            if user_input <= no_sort[pos]:
                no_sort.insert(pos, user_input)
                print(f'Added at position {pos}...')
                break
            pos = pos + 1

print(f'\nYour array already sorted without any sorting function: {corInSucc}{no_sort}{corOut}')

# --------------------------------------------------
# LESSON 081

print('\n\nLesson 081 >> Build a program xxxxx:\n')

_array81 = []

while True:

    _input81 = int(input('Type an integer (0 to exit): '))

    if _input81 == 0:
        break
    else:
        _array81.append(_input81)

_array81.sort(reverse=True)

print(
    f'\n{corInSucc}{len(_array81)}{corOut} numbers were typed.'
    f'\nYour array: {corInSucc}{_array81}{corOut}'
)
if 5 in _array81:
    print(f'{corInSucc}The number 5 belongs the _array81!{corOut}')
else:
    print(f'{corInFail}The number 5 does not belong the _array81!{corOut}')

# --------------------------------------------------
# LESSON 082

print('\n\nLesson 082 >> Build a program the user adds numbers in an array and, after that, this program shows up'
      'the eve list and the odd list as arrays as well:\n')

list_all = list()
list_eve = list()
list_odd = list()

while True:

    user_choice = int(input('Type an integer (0 to exit): '))
    list_all.append(user_choice)

    if user_choice == 0:
        break

    elif user_choice % 2 == 0:
        list_eve.append(user_choice)
    else:
        list_odd.append(user_choice)

print(
    f'\nAll numbers: {corInSucc}{list_all}{corOut}\n'
    f'Only eve ones: {corInSucc}{list_eve}{corOut}\n'
    f'Only odd ones: {corInSucc}{list_odd}{corOut}'
)

# --------------------------------------------------
# LESSON 083

print('\n\nLesson 083 >> Build a program xxxxx:\n')

_mathExp = str(input('Type any math expression [e.g. (2+2)*3 ]: ').upper().strip())

if _mathExp.count('(') != _mathExp.count(')'):
    print(f'{corInFail}Expression NOT valid!{corOut}')
else:
    print(f'{corInSucc}Expression ok!{corOut}')
