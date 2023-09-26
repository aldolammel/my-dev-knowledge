from random import sample


# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corOut = '\033[m'


# CAPITAL NAMES' DATABASE
_words_library = ['Kabul', 'Tirana', 'Algiers', 'Andorra la Vella', 'Luanda', 'Buenos Aires', 'Yerevan', 'Canberra',
                  'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 'Belmopan',
                  'Porto Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasilia', 'Bandar Seri Begawan', 'Sofia',
                  'Ouagadougou', 'Gitega', 'Phnom Penh', 'Yaounde', 'Ottawa', 'Praia', 'Bangui', 'Santiago', 'Beijing',
                  'Bogota', 'Moroni', 'Kinshasa', 'Brazzaville', 'San Jose', 'Yamoussoukro', 'Zagreb', 'Havana',
                  'Nicosia', 'Prague', 'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo', 'Dili', 'Quito', 'Cairo',
                  'San Salvador', 'London', 'Malabo', 'Asmara', 'Tallinn', 'Mbabana', 'Addis Ababa', 'Palikir', 'Suva',
                  'Helsinki', 'Paris', 'Libreville', 'Banjul', 'Tbilisi', 'Berlin', 'Accra', 'Athens', 'Guatemala City',
                  'Conakry', 'Bissau', 'Georgetown', 'Port au Prince', 'Tegucigalpa', 'Budapest', 'Reykjavik',
                  'New Delhi', 'Jakarta', 'Tehran', 'Baghdad', 'Dublin', 'Jerusalem', 'Rome', 'Kingston', 'Tokyo',
                  'Amman', 'Nairobi', 'Tarawa Atoll', 'Pristina', 'Kuwait City', 'Bishkek', 'Vientiane', 'Riga',
                  'Beirut', 'Maseru', 'Monrovia', 'Tripoli', 'Vaduz', 'Vilnius', 'Luxembourg', 'Antananarivo',
                  'Lilongwe', 'Kuala Lumpur', 'Male', 'Bamako', 'Valletta', 'Majuro', 'Nouakchott', 'Port Louis',
                  'Mexico City', 'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica', 'Rabat', 'Maputo', 'Nay Pyi Taw',
                  'Windhoek', 'Kathmandu', 'Amsterdam', 'Wellington', 'Managua', 'Niamey', 'Abuja', 'Pyongyang',
                  'Skopje', 'Belfast', 'Oslo', 'Muscat', 'Islamabad', 'Melekeok', 'Panama City', 'Port Moresby',
                  'Asuncion', 'Lima', 'Manila', 'Warsaw', 'Lisbon', 'Doha', 'Bucharest', 'Moscow', 'Kigali',
                  'Basseterre', 'Castries', 'Kingstown', 'Apia', 'San Marino', 'Sao Tome', 'Riyadh', 'Edinburgh',
                  'Dakar', 'Belgrade', 'Victoria', 'Freetown', 'Singapore', 'Bratislava', 'Ljubljana', 'Honiara',
                  'Mogadishu', 'Pretoria', 'Seoul', 'Juba', 'Madrid', 'Sri Jayawardenapura Kotte', 'Khartoum',
                  'Paramaribo', 'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma', 'Bangkok', 'Lome',
                  'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala', 'Kyiv', 'Abu Dhabi',
                  'London', 'Washington', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City', 'Caracas', 'Hanoi',
                  'Cardiff', 'Lusaka', 'Harare']

# DATABASE CONFORMITY
for i in range(len(_words_library)):
    _words_library[i] = _words_library[i].lower().strip()

# GAME RULES
mistakesTolerance = 8


def fnc_show_game_title():
    """
    Shows the game title
    :return: print the game title.
    """
    _title = '''
         ██╗       ██╗ █████╗ ██████╗ ██╗     ██████╗        █████╗  █████╗ ██████╗ ██╗████████╗ █████╗ ██╗      ██████╗
         ██║  ██╗  ██║██╔══██╗██╔══██╗██║     ██╔══██╗      ██╔══██╗██╔══██╗██╔══██╗██║╚══██╔══╝██╔══██╗██║     ██╔════╝
         ╚██╗████╗██╔╝██║  ██║██████╔╝██║     ██║  ██║      ██║  ╚═╝███████║██████╔╝██║   ██║   ███████║██║     ╚█████╗
          ████╔═████║ ██║  ██║██╔══██╗██║     ██║  ██║      ██║  ██╗██╔══██║██╔═══╝ ██║   ██║   ██╔══██║██║      ╚═══██╗
          ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║███████╗██████╔╝      ╚█████╔╝██║  ██║██║     ██║   ██║   ██║  ██║███████╗██████╔╝
           ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚══════╝╚═════╝        ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝
        
        ██╗  ██╗ █████╗ ███╗  ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗  ██╗       ██████╗  █████╗ ███╗   ███╗███████╗
        ██║  ██║██╔══██╗████╗ ██║██╔════╝ ████╗ ████║██╔══██╗████╗ ██║      ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
        ███████║███████║██╔██╗██║██║  ██╗ ██╔████╔██║███████║██╔██╗██║      ██║  ██╗ ███████║██╔████╔██║█████╗
        ██╔══██║██╔══██║██║╚████║██║  ╚██╗██║╚██╔╝██║██╔══██║██║╚████║      ██║  ╚██╗██╔══██║██║╚██╔╝██║██╔══╝
        ██║  ██║██║  ██║██║ ╚███║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚███║      ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝       ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
        '''
    return print(_title)


def fnc_show_word():
    """
    Shows the selected word but its characters hidden from the player until they figure it out
    :return: None.
    """
    print()
    print(f'The world capital is: {_corT}', end='')
    for _l in _hiddenWord:
        print(_l, end='')
    print(f'{_corOut}\n')
    return None


def fnc_hangman_mistakes(_mistakes):
    """
    Draw the hangman
    :param _mistakes: mistakes made by the player.
    :return: None
    """
    global mistakesTolerance
    _hang_states = [
        '''
        _ _ | _ _
        ''',
        '''
            |
            |
            |
            |
            | 
        _ _ | _ _
        ''',
        '''
            ._ _ _ _ _.
            |
            |
            |
            |
            | 
        _ _ | _ _
        ''',
        '''
            ._ _ _ _ _.
            |         |
            |         O
            |
            |
            | 
        _ _ | _ _
        ''',
        '''
            ._ _ _ _ _.
            |         |
            |         O
            |        /||
            |
            | 
        _ _ | _ _
        ''',
        '''
            ._ _ _ _ _.
            |         |
            |         O
            |        /||
            |         ||
            | 
        _ _ | _ _
        '''
    ]
    print(f'{_corF}')
    if _mistakes == mistakesTolerance - 4:
        print(_hang_states[0])
    if _mistakes == mistakesTolerance - 3:
        print(_hang_states[1])
    if _mistakes == mistakesTolerance - 2:
        print(_hang_states[2])
    if _mistakes == mistakesTolerance - 1:
        print(_hang_states[3])
    if _mistakes == mistakesTolerance:
        print(_hang_states[4])
    if _mistakes > mistakesTolerance:
        print(_hang_states[5])
    print(f'{_corOut}')
    return None


while True:
    _wordSelected = sample(_words_library, 1)                              # selecting randomly just 1 word in the list.
    _wordSelected = _wordSelected[0]
    _wordLength = len(_wordSelected)
    _hiddenWord = list()
    for i in range(_wordLength):                             # building the hidden word with the same character numbers.
        if _wordSelected[i] != ' ':
            _hiddenWord.append('_')
        else:
            _hiddenWord.append(' ')
    _hitsTargeted = _wordLength - (_wordSelected.count(' '))  # how many letters has the selected word, less the spaces.
    _mistakes = 0
    _alreadyHit = list()
    _alreadyMis = list()
    # print(_wordSelected)                                                                               # debug option.
    fnc_show_game_title()
    fnc_show_word()

    # Main loop starts:
    while _mistakes <= mistakesTolerance:
        _userTry = str(input('Try a letter: ')).strip().lower()
        if not _userTry.isalpha():
            print(f'{_corF}Only letters, please.{_corOut}')
            continue                                                                     # stop the loop and restart it.
        if len(_userTry) != 1:
            print(f'{_corF}You must type one letter for each try.{_corOut}')
            continue
        _letterFoundTimes = _wordSelected.count(_userTry)  # looking for how many times the letter shows up in the word.

        # you have one or more hits:
        if _letterFoundTimes > 0:
            if _userTry not in _alreadyHit:
                _alreadyHit.append(_userTry)
                # print('Already hit:', _alreadyHit)                                                     # debug option.
                print(f'{_corT}There is the letter "{_userTry}"', end=' ')
                if _letterFoundTimes == 1:
                    print(f'once.{_corOut}')
                elif _letterFoundTimes == 2:
                    print(f'twice.{_corOut}')
                else:
                    print(f'{_letterFoundTimes} times.{_corOut}')
                _hitsTargeted = _hitsTargeted - _letterFoundTimes
                for i in range(_wordLength):
                    if _wordSelected[i] == _userTry:
                        _hiddenWord[i] = _userTry
                fnc_show_word()
                if _hitsTargeted == 0:
                    print(f'{_corT}YOU WON the hangman game with', end=' ')
                    if _mistakes == 0:
                        print(f'no mistakes.{_corOut}\n')
                    elif _mistakes == 1:
                        print(f'{_mistakes} mistake.{_corOut}\n')
                    else:
                        print(f'{_mistakes} mistakes.{_corOut}\n')
                    break
            elif _userTry in _alreadyHit:
                # print('Already hit:', _alreadyHit)                                                     # debug option.
                print(f'You already tried this letter! Try another one!')

        # you have no hits:
        else:
            if _userTry not in _alreadyMis:
                _mistakes += 1
                _alreadyMis.append(_userTry)
                # print('Already mistaken:', _alreadyMis)                                                # debug option.
                fnc_hangman_mistakes(_mistakes)
                print(f'{_corF}There is no "{_userTry}" in the word.\n'
                      f'You got {_mistakes} of {mistakesTolerance} mistakes tolerance.{_corOut}')
                if _mistakes > mistakesTolerance:
                    print(f'{_corF}YOU LOOSE!{_corOut}\n')
                    break
            elif _userTry in _alreadyMis:
                # print('Already mistaken:', _alreadyMis)                                                # debug option.
                print(f'You already tried this letter! Try another one!')
            fnc_show_word()

    _keepRunning = str(input('Does keep the game running? [Y/N]: ')).strip().upper()
    if _keepRunning != 'Y':
        break

print('\nThe game has been finished. Bye.')
