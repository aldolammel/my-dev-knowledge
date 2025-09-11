# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'


# Logotype
def fnc_show_logo():
    _logo = '''
     e88~-_       e      888      e88~-_        ,d88~~\ 888      e    e      888~-_   888     888~~  Y88b    / 
    d888   \     d8b     888     d888   \       8888    888     d8b  d8b     888   \  888     888___  Y88b  /  
    8888        /Y88b    888     8888           `Y88b   888    d888bdY88b    888    | 888     888      Y88b/   
    8888       /  Y88b   888     8888            `Y88b, 888   / Y88Y Y888b   888   /  888     888      /Y88b   
    Y888   /  /____Y88b  888     Y888   /          8888 888  /   YY   Y888b  888_-~   888     888     /  Y88b  
     "88_-~  /      Y88b 888____  "88_-~        \__88P' 888 /          Y888b 888      888____ 888___ /    Y88b 
    '''
    return print(_logo)


# summation
def fnc_calc_sum(_nums):
    return sum(_nums)


# subtraction
def fnc_calc_sub(_nums):
    _result = _nums[0]
    for _num in range(1, len(_nums)):
        _result -= _nums[_num]
    return _result


# Division
def fnc_calc_div(_nums):
    _result = _nums[0]
    for _num in range(1, len(_nums)):
        _result /= _nums[_num]
    return _result


# Multiplication
def fnc_calc_mlt(_nums):
    _result = _nums[0]
    for _num in range(1, len(_nums)):
        _result *= _nums[_num]
    return _result


# Show the calc
def fnc_show_calc(_op, _nums):
    _counter = 0
    print('\nYour calc:', end=' ')
    for _num in _nums:
        _counter += 1
        print(f'{_corT}{_num}{_corOut}', end=' ')
        if _counter != len(_nums):
            print(f'{_corF}{_op}{_corOut}', end=' ')
    print('=', end=' ')
    return None


# Caller of operation selected by user
def fnc_op(_op, _nums):
    fnc_show_calc(_op, _nums)
    fnc_op_to_use = _operators[_op]
    return fnc_op_to_use(_nums)


# Operators dictionary
_operators = {
    '+': fnc_calc_sum,
    '-': fnc_calc_sub,
    '/': fnc_calc_div,
    '*': fnc_calc_mlt
}

fnc_show_logo()

while True:
    _userNumsList = list()
    _userOp = str(input('\nOperator [+ - / *]: ')).strip()

    while True:
        _userNum = float(input('Number: '))
        _userNumsList.append(_userNum)

        if len(_userNumsList) >= 2:
            _keepingCalc = str(input('Add more numbers? [y/n]: ')).lower().strip()
            if _keepingCalc == 'n':
                break

    print(f'{_corT}{fnc_op(_userOp, _userNumsList)}{_corOut}')
    _keepRunning = str(input('\nAnother calc? [y/n]: ')).lower().strip()
    if _keepRunning == 'n':
        print(f'{_corF}The program has been terminated.{_corOut}')
        break

