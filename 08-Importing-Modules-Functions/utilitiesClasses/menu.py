from utilitiesClasses import database

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'


def fnc_header(_txt):
    print('\n\n')
    print('-' * 40)
    print(f'{_txt.upper():^40}')
    print('-' * 40)


def fnc_menu(_userOption='Select a numeric option: '):
    _options = (
        'See all records',
        'Record a new person',
        'Exit'
    )
    _db = 'class27z-db.txt'
    fnc_header('Main menu')

    for _pos, _val in enumerate(_options):
        _pos += 1
        print(f'{_corT}{_pos}{_corOut}: {_val}')

    print('-' * 40)
    while True:
        try:
            _input = int(input(_userOption))

        except (ValueError, TypeError):
            print(f'{_corF}You must to type one of the menu\'s numbers above.{_corOut}')

        except KeyboardInterrupt:
            print(f'{_corF}The action has been aborted.{_corOut}')

        except Exception as _error:
            print(f'{_corF}Something ran wrong: {_error}{_corOut}')

        else:
            if 0 < _input <= len(_options):    # avoid invalid option if the user type an integer out of the menu range.
                break
            else:
                print(f'{_corF}Option not found! Try again.{_corOut}')

    if _input == 1:
        fnc_header(f'Option: {_options[0]}')
        database.fnc_dbReader(_db)

    if _input == 2:
        fnc_header(f'Option: {_options[1]}')
        database.fnc_newRecord(_db)

    if _input == 3:
        fnc_header(f'Option: {_options[2]}')
        print('See you soon!')
        return 0
