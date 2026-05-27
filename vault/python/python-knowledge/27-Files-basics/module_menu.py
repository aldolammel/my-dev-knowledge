import module_db

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corO = '\033[m'


def header(_txt):
    print('\n\n')
    print('-' * 40)
    print(f'{_txt.upper():^40}')
    print('-' * 40)


def menu(_userOpt='Select a numeric option: '):
    _opts = (
        'See all records',
        'Record a new person',
        'Exit'
    )
    _db = 'class27z-db.txt'
    header('Main menu')

    for _pos, _val in enumerate(_opts):
        _pos += 1
        print(f'{_corT}{_pos}{_corO}: {_val}')

    print('-' * 40)
    while True:
        try:
            _input = int(input(_userOpt))

        except (ValueError, TypeError):
            print(f'{_corF}You must to type one of the menu\'s numbers above.{_corO}')

        except KeyboardInterrupt:
            print(f'{_corF}The action has been aborted.{_corO}')

        except Exception as _error:
            print(f'{_corF}Something ran wrong: {_error}{_corO}')

        else:
            if 0 < _input <= len(_opts):       # avoid invalid option if the user type an integer out of the menu range.
                break
            else:
                print(f'{_corF}Option not found! Try again.{_corO}')

    if _input == 1:
        header(f'Option: {_opts[0]}')
        module_db.db_reader(_db)

    if _input == 2:
        header(f'Option: {_opts[1]}')
        module_db.new_record(_db)

    if _input == 3:
        header(f'Option: {_opts[2]}')
        print('See you soon!')
        return 0
