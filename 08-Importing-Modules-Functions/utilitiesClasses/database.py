from utilitiesClasses import menu

# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'


def fnc_dbExist(_file):                   # checking if the file exists, trying to open and close it.
    try:
        _db = open(_file, 'rt')           # 'rt' = read text
        _db.close()
    except FileNotFoundError:
        return False
    else:
        return True


def fnc_dbCreate(_file):                  # it creates the database.
    try:
        _db = open(_file, 'wt+')          # 'wt+' = write text (+ = create if it not exist).
        _db.close()
    except:
        print(f'Something ran wrong...')
    else:
        print(f'{_corT}{_file} file has been successfully created!{_corOut}')


def fnc_dbReader(_file):
    try:
        _db = open(_file, 'rt')
    except:
        print(f'{_corF}Something ran wrong...{_corOut}')
    else:
        for _line in _db:
            _data = _line.split(';')
            _data[1] = _data[1].replace('\n', '')
            print(f'{_data[0]:<20}{_data[1]:>10}')
        _db.close()
    finally:
        menu.fnc_menu()


def fnc_newRecord(_file):

    try:
        while True:
            _name = str(input('Name: ')).strip().upper()
            if not _name.isnumeric():
                break
            else:
                print(f'{_corF}Name not valid. Try again.{_corOut}')

    except (ValueError, TypeError):
        print(f'{_corF}Please, insert a valid name.{_corOut}')

    except:
        print(f'{_corF}Something ran  wrong with the name.{_corOut}')

    else:
        while True:
            try:
                _year = int(input('Birth year: '))

            except (ValueError, TypeError):
                print(f'{_corF}Please, insert a valid year.{_corOut}')

            except:
                print(f'{_corF}Something ran wrong with the year.{_corOut}')

            else:
                if len(str(_year)) == 4:
                    break
                else:
                    print(f'{_corF}Birth year must be four digits, e.g. 1984. Try again.{_corOut}')

        try:
            _recording = open(_file, 'at')   # preparing to append (include) the new information on file.

        except:
            print(f'{_corF}Something ran wrong in the file opening...{_corOut}')

        else:
            try:
                _recording.write(f'{_name};{_year}\n')

            except:
                print(f'{_corF}Apparently, we got an error when it was including in the database.{_corOut}')

            else:
                print(f'{_corT}{_name} has been recorded.{_corOut}')
                _recording.close()

        finally:
            menu.fnc_menu()


_db = 'class27z-db.txt'

if fnc_dbExist(_db):
    print('Database available!')
else:
    print('Database not available!')
    fnc_dbCreate(_db)
