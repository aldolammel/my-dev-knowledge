from random import sample

# Management:
is_on_debug = True

# MY COLORS
corT = '\033[1;32m'
corF = '\033[1;31m'
corO = '\033[m'

# CAPITAL NAMES' DATABASE
words_library = ['Kabul', 'Tirana', 'Algiers', 'Andorra la Vella', 'Luanda', 'Buenos Aires', 'Yerevan', 'Canberra',
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
for i in range(len(words_library)):
    words_library[i] = words_library[i].lower().strip()

# GAME RULES
MISTAKES_TOLERANCE = 8


def show_game_title():
    """
    Shows the game title
    :return: print the game title.
    """
    title = '''
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
    return print(title)


def show_word():
    """
    Shows the selected word but its characters hidden from the player until they figure it out
    :return: None.
    """
    print()
    print(f'The world capital is: {corT}', end='')
    for letter in hidden_word:
        print(letter, end='')
    print(f'{corO}\n')
    return None


def hangman_mistakes(mistakes):
    """
    Draw the hangman
    :param mistakes: mistakes made by the player.
    :return: None
    """
    global MISTAKES_TOLERANCE
    hang_states = [
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
    print(f'{corF}')
    if mistakes == MISTAKES_TOLERANCE - 4:
        print(hang_states[0])
    if mistakes == MISTAKES_TOLERANCE - 3:
        print(hang_states[1])
    if mistakes == MISTAKES_TOLERANCE - 2:
        print(hang_states[2])
    if mistakes == MISTAKES_TOLERANCE - 1:
        print(hang_states[3])
    if mistakes == MISTAKES_TOLERANCE:
        print(hang_states[4])
    if mistakes > MISTAKES_TOLERANCE:
        print(hang_states[5])
    print(corO)
    return None


# ----------------------------------------------------------------------------------------------------------------------

while True:
    # Initial values:
    hidden_word = list()
    player_mis = 0
    already_hit = list()
    already_mis = list()

    # Declarations:
    word_selected = sample(words_library, 1)  # selecting randomly just 1 word in the list.
    word_selected = word_selected[0]
    word_length = len(word_selected)

    # Exchanging letter for underscore character:
    for i in range(word_length):  # building the hidden word with the same character numbers.
        if word_selected[i] != ' ':
            hidden_word.append('_')
        else:
            hidden_word.append(' ')
    hits_targeted = word_length - (word_selected.count(' '))  # how many letters has the selected word, less the spaces.
    # Debug:
    if is_on_debug:
        print(word_selected)

    # Starting the game:
    show_game_title()
    show_word()

    # Main loop starts:
    while player_mis <= MISTAKES_TOLERANCE:
        user_try = str(input('Try a letter: ')).strip().lower()
        if not user_try.isalpha():
            print(f'{corF}Only letters, please.{corO}')
            continue  # restart the loop.
        if len(user_try) != 1:
            print(f'{corF}You must type one letter for each try.{corO}')
            continue
        letter_found_times = word_selected.count(user_try)  # looking for how many times the letter shows up in word.

        # you have one or more hits:
        if letter_found_times > 0:
            if user_try not in already_hit:
                already_hit.append(user_try)
                # print('Already hit:', already_hit)                                                     # debug option.
                print(f'{corT}There is the letter "{user_try}"', end=' ')
                if letter_found_times == 1:
                    print(f'once.{corO}')
                elif letter_found_times == 2:
                    print(f'twice.{corO}')
                else:
                    print(f'{letter_found_times} times.{corO}')
                hits_targeted = hits_targeted - letter_found_times
                for i in range(word_length):
                    if word_selected[i] == user_try:
                        hidden_word[i] = user_try
                show_word()
                if hits_targeted == 0:
                    print(f'{corT}YOU WON the hangman game with', end=' ')
                    if player_mis == 0:
                        print(f'no mistakes.{corO}\n')
                    elif player_mis == 1:
                        print(f'{player_mis} mistake.{corO}\n')
                    else:
                        print(f'{player_mis} mistakes.{corO}\n')
                    break
            elif user_try in already_hit:
                # print('Already hit:', _alreadyHit)                                                     # debug option.
                print(f'You already tried this letter! Try another one!')

        # you have no hits:
        else:
            if user_try not in already_mis:
                player_mis += 1
                already_mis.append(user_try)
                # print('Already mistaken:', already_mis)                                                # debug option.
                hangman_mistakes(player_mis)
                print(f'{corF}There is no "{user_try}" in the word.\n'
                      f'You got {player_mis} of {MISTAKES_TOLERANCE} mistakes tolerance.{corO}')
                if player_mis > MISTAKES_TOLERANCE:
                    print(f'{corF}YOU LOOSE!{corO}\n')
                    break
            elif user_try in already_mis:
                # print('Already mistaken:', already_mis)                                                # debug option.
                print(f'You already tried this letter! Try another one!')
            show_word()

    keep_running = str(input('Does keep the game running? [Y/N]: ')).strip().upper()
    if keep_running != 'Y':
        break

print('\nThe game has been finished. Bye.')
