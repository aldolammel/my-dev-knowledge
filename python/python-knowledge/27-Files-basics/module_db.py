import module_menu

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corO = '\033[m'


def db_exists(_file):                   # checking if the file exists, trying to open and close it.
    try:
        _db = open(_file, 'rt')           # 'rt' = read text
        _db.close()
    except FileNotFoundError:
        return False
    else:
        return True


def db_creation(_file):                  # it creates the database.
    try:
        _db = open(_file, 'wt+')          # 'wt+' = write text (+ = create if it not exist).
        _db.close()
    except:
        print(f'Something ran wrong...')
    else:
        print(f'{_corT}{_file} file has been successfully created!{_corO}')


def db_reader(_file):
    try:
        _db = open(_file, 'rt')
    except:
        print(f'{_corF}Something ran wrong...{_corO}')
    else:
        for _line in _db:
            _data = _line.split(';')
            _data[1] = _data[1].replace('\n', '')
            print(f'{_data[0]:<20}{_data[1]:>10}')
        _db.close()
    finally:
        module_menu.menu()


def new_record(_file):

    try:
        while True:
            _name = str(input('Name: ')).strip().upper()
            if not _name.isnumeric():
                break
            else:
                print(f'{_corF}Name not valid. Try again.{_corO}')

    except (ValueError, TypeError):
        print(f'{_corF}Please, insert a valid name.{_corO}')

    except:
        print(f'{_corF}Something ran  wrong with the name.{_corO}')

    else:
        while True:
            try:
                _year = int(input('Birth year: '))

            except (ValueError, TypeError):
                print(f'{_corF}Please, insert a valid year.{_corO}')

            except:
                print(f'{_corF}Something ran wrong with the year.{_corO}')

            else:
                if len(str(_year)) == 4:
                    break
                else:
                    print(f'{_corF}Birth year must be four digits, e.g. 1984. Try again.{_corO}')

        try:
            _recording = open(_file, 'at')   # preparing to append (include) the new information on file.

        except:
            print(f'{_corF}Something ran wrong in the file opening...{_corO}')

        else:
            try:
                _recording.write(f'{_name};{_year}\n')

            except:
                print(f'{_corF}Apparently, we got an error when it was including in the database.{_corO}')

            else:
                print(f'{_corT}{_name} has been recorded.{_corO}')
                _recording.close()

        finally:
            module_menu.menu()


_db = 'class27z-db.txt'

if db_exists(_db):
    print('Database available!')
else:
    print('Database not available!')
    db_creation(_db)
