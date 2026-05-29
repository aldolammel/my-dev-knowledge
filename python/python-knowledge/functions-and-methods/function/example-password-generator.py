listPass = list()


def fnc_show_logo():
    _logo = '''
    ██████   █████  ███████ ███████ ██     ██  ██████  ██████  ██████  
    ██   ██ ██   ██ ██      ██      ██     ██ ██    ██ ██   ██ ██   ██ 
    ██████  ███████ ███████ ███████ ██  █  ██ ██    ██ ██████  ██   ██ 
    ██      ██   ██      ██      ██ ██ ███ ██ ██    ██ ██   ██ ██   ██ 
    ██      ██   ██ ███████ ███████  ███ ███   ██████  ██   ██ ██████  
    GENERATOR:                                                                              
    '''
    return print(_logo)


def fnc_list(_value):
    """
    Just the list where the password characters will be saved
    :param _value: the value/character that other function will select.
    :return: the list/array where the values will be saved.
    """
    global listPass
    listPass.append(_value)
    return listPass


def fnc_num(_range=6):
    """
    Randomly it will select some numbers for the password
    :param _range: how many numbers will be included.
    :return: None.
    """
    from random import randrange
    for num in range(_range):
        fnc_list(randrange(0, 9))                                                                         # from 0 to 9.
    return None


def fnc_alphabet(_range=3):
    """
    Randomly it will select some letters for the password
    :param _range: how many letters will be included.
    :return: None.
    """
    from random import randrange
    _alphabet = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
                 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
                 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    for letter in range(_range):
        fnc_list(_alphabet[randrange(0, 51)])                                      # 52 is the amount of US alphabet x2.
    return None


def fnc_special(_range=3):
    """
    Randomly it will select some special characters for the password
    :param _range: how many special characters will be included.
    :return: None.
    """
    from random import randrange
    _specials = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', '=', '_', '|', '/', '.', ',', ']', '[', '{',
                 '}', '?', ';', ':', '~', '^', '<', '>']
    for special in range(_range):
        fnc_list(_specials[randrange(0, 27)])                   # 28 is the amount of special characters available here.
    return None


def fnc_password_generate(_list, _times=5):
    """
    Defines how many times the program will generate a new password
    :param _list: the list used to save the password generated
    :param _times: how many passwords options you want to show
    :return: None
    """
    for i in range(_times):
        fnc_password_ready(_list)
        _list.clear()
    return None


def fnc_password_ready(_list):
    """
    Present the final result of password generation
    :param _list: the list used to save the password generated.
    :return: None.
    """
    from random import shuffle
    fnc_num()                                                                      # generation of the password numbers.
    fnc_alphabet()                                                                 # generation of the password letters.
    fnc_special()                                                                # generation of the special characters.
    shuffle(_list)                                                       # shuffle the list with the generated password.
    print('    ', end='')
    for i in _list:
        print(i, end='')
    print()
    return None


fnc_show_logo()
fnc_password_generate(listPass, 15)
