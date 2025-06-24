"""import requests
from tkinter import *"""
from random import choice
from time import sleep

# COLORS
corU = '\033[1;32m'  # color in, user
corD = '\033[1;31m'  # color in, dealer
corY = '\033[1;33m'  # color in, debug info
corO = '\033[m'  # color out

# DEVELOPING OPTIONS:
isDebugging = False
if isDebugging:
    timing = 0.35
else:
    timing = 1


# FUNCTIONS:
def fnc_logo():
    """
    It shows the logo before each new match
    :return: None.
    """
    sleep(0.2)
    print('''

     /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$
    | $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/
    | $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/ 
    | $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/  
    | $$__  $$| $$      | $$__  $$| $$      | $$  $$  
    | $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$ 
    | $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$
    |_______/ |________/|__/  |__/ \______/ |__/  \__/

        /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$          
       |__  $$ /$$__  $$ /$$__  $$| $$  /$$/          
          | $$| $$  \ $$| $$  \__/| $$ /$$/           
          | $$| $$$$$$$$| $$      | $$$$$/            
     /$$  | $$| $$__  $$| $$      | $$  $$            
    | $$  | $$| $$  | $$| $$    $$| $$\  $$           
    |  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$          
     \______/ |__/  |__/ \______/ |__/  \__/          
      by @aldolammel

    ''')
    return None


def fnc_get_card(who, hand, show=True):
    """
    It gives a card to dealer or to the user when called
    :param who: string. Name of the player
    :param hand: list. Hand of who will receive the card
    :param show: bool. Whether the card will be shown to players. Default: True
    :return: string message of a cord was given.
    """
    global isPlaying, deck, result

    sleep(timing)

    if not isDebugging:
        card_received = choice(deck)
    else:
        card_received = int(input(f'\n{corY}[DEBUGGING ON]{corO} Add card to {who}: '))

    hand.append(card_received)

    if isPlaying:
        # checking if the player wants an 11 or 1 card value:
        if sum(hand) > 21:
            if hand.count(11) != 0:
                hand[hand.index(11)] = 1
                if card_received == 11:
                    card_received = 1

        # pre-announcing > adjusting the grammar and colors:
        if who == 'You':
            new_card_msg = f'\n{corU}{who}{corO} get a new card:'
        else:
            new_card_msg = f'\n{corD}{who}{corO} gets a new card:'

        # announcing the new card given:
        if not isDebugging:
            if not show:
                result = f'{new_card_msg} XXXX'
            else:
                result = f'{new_card_msg} {card_received}'
        else:
            result = f'{new_card_msg} {card_received}'

    return print(result)


def fnc_check_winner():
    """
    Checks who are the winner
    :return: result object.
    """
    global isPlaying, isThereWinner, d_hand, u_hand, result

    if not isThereWinner:
        # winning messages:
        u_win_msg = (f'\n{corU}YOU WIN! {u_hand} = {sum(u_hand)}!{corO} '
                     f'\nThe dealer got {d_hand} = {sum(d_hand)}.')
        u_winbj_msg = (f'\n{corU}You got the BLACKJACK hand! '
                       f'\nYou win = {u_hand}{corO} '
                       f'\nDealer looses = {d_hand}')
        d_win_msg = (f'\n{corD}DEALER WINS! {d_hand} = {sum(d_hand)}!{corO} '
                     f'\nYou got {u_hand} = {sum(u_hand)}.')
        d_winbj_msg = (f'\n{corD}The Dealer got the BLACKJACK hand! '
                       f'\nDealer wins = {d_hand}{corO} '
                       f'\nYou loose = {u_hand}')
        sleep(timing)

        # if the game draws:
        if sum(d_hand) == sum(u_hand):
            result = (f'\nDRAW! '
                      f'\nBoth with {(sum(u_hand) + sum(d_hand)) / 2}'
                      f'\nYou = {u_hand}'
                      f'\nDealer = {d_hand}')
        else:

            # if user or dealer reaches the blackjack goal:
            if sum(u_hand) == 21 and sum(d_hand) != 21:
                if len(u_hand) == 2:
                    result = u_winbj_msg
                else:
                    result = u_win_msg
            if sum(d_hand) == 21 and sum(u_hand) != 21:
                if len(d_hand) == 2:
                    result = d_winbj_msg
                else:
                    result = d_win_msg

            # if user or dealer across 21 and the opponent stays below 21, the opponent wins:
            if sum(u_hand) > 21 and sum(d_hand) < 21:
                result = d_win_msg
            if sum(d_hand) > 21 and sum(u_hand) < 21:
                result = u_win_msg

            # if user and dealer both across 21, the game burst:
            if sum(u_hand) > 21 and sum(d_hand) > 21:
                result = (f'\nYOU BOTH BURST! '
                          f'\nYour hand {u_hand}={sum(u_hand)} '
                          f'\nDealer\'s hand {d_hand}={sum(d_hand)}')

            # if nobody across 21 or even reaches it, the winner is who has the closest 21 score:
            if sum(d_hand) < 21 and sum(u_hand) < 21:
                d_checking = 21 - sum(d_hand)
                u_checking = 21 - sum(u_hand)
                if d_checking < u_checking:
                    result = d_win_msg
                else:
                    result = u_win_msg

        # finishing the game:
        isPlaying = False
        isThereWinner = True
    return print(result)


def fnc_round_one():
    """
    Runs the first cards delivery.
    :return: if someone receives a 10 and 11, returns fnc_check_winner. Otherwise, returns fnc_round_two.
    """

    if isDebugging:
        print(f'\n{corY}[DEBUGGING CHECKING]:'
              f'\nDeck cards: {deck}'
              f'\nCurrent user hand: {u_hand}'
              f'\nCurrent dealer hand: {d_hand}')

    # first cards:
    fnc_get_card('You', u_hand)
    fnc_get_card('The Dealer', d_hand, False)  # from deck, the dealer receives a UNREVEALED card.
    fnc_get_card('You', u_hand)
    fnc_get_card('The Dealer', d_hand)

    # checking BlackJack special hand:
    if sum(u_hand) == 21 or sum(d_hand) == 21:
        return fnc_check_winner()
    else:
        return fnc_round_two()


def fnc_round_two():
    """
    Runs the last cards delivery.
    :return: fnc_check_winner.
    """
    global isPlaying, ask_error_msg

    # user last playing:
    while isPlaying:
        u_turn_msg = f'{corU}You{corO} stand, finishing your turn.'
        sleep(timing)
        if sum(u_hand) < 21:
            while True:
                ask_card = str(input(f'\n{corU}Your hand{corO} is {u_hand}! Another card? [y/n]: ')).strip().lower()
                if ask_card == 'y' or ask_card == 'n':
                    break
                else:
                    print(ask_error_msg)
                    sleep(timing)
            if ask_card == 'y':
                sleep(timing)
                fnc_get_card('You', u_hand)
            else:
                print(u_turn_msg)
                break
        else:
            print(u_turn_msg)
            break

    # dealer last playing:
    while isPlaying:
        d_turn_msg = f'{corD}Dealer\'s{corO} turn has been finished.'
        sleep(timing)
        if sum(d_hand) < 21 and sum(u_hand) <= 21:
            if sum(d_hand) < 17:
                fnc_get_card('The Dealer', d_hand)
            else:
                print(d_turn_msg)
                break
        else:
            print(d_turn_msg)
            break

    # finishing the game:
    return fnc_check_winner()


def fnc_play_again():
    """
    Just ask the user if they want to play again
    :return: bool value.
    """
    global isPlaying, isThereWinner, ask_error_msg

    if isDebugging:
        print(f'\n{corY}[DEBUGGING FINAL INFO]:'
              f'\nDeck cards: {deck}'
              f'\nYour final hand = {u_hand} = {sum(u_hand)}'
              f'\nDealer final hand = {d_hand} = {sum(d_hand)}{corO}')

    while True:
        ask_play_again = str(input('\nPlay again? [y/n]: ')).strip().lower()
        if ask_play_again == 'y' or ask_play_again == 'n':
            break
        else:
            print(ask_error_msg)
            sleep(timing)
    if ask_play_again == 'y':
        isThereWinner = False
        isPlaying = True
        return isPlaying
    else:
        print(f'\n{corD}The BLACKJACK game has been terminated. \nby @aldolammel{corO}')
        isPlaying = False
        return isPlaying


# ----------------------------------------------------------------------------------------------------------------------

# GLOBAL SCOPE:
isPlaying = True
isThereWinner = False
result = ''
ask_error_msg = f'\n{corD}Please, use "Y" for YES or "N" for NO.{corO}'

# APP STARTS:
while isPlaying:
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # deck cards available in BlackJack.
    d_hand = list()
    u_hand = list()

    fnc_logo()
    fnc_round_one()
    fnc_play_again()

"""app_window = Tk()  # creating the app window.

app_window.title('Black Jack Game')

# Spaces empties:
col0_row0 = ''
col2_row0 = ''
col3_row0 = ''

# Txts:
txt_about = Label(app_window, text='This is a Black Jack game built with Python by @aldolammel')

# Buttons:
bt_hit = Button(app_window, text='HIT', command=fnc_get_card)
bt_stand = Button(app_window, text='STAND')

# Row 0
col0_row0.grid(column=0, row=0)
col2_row0.grid(column=2, row=0)
col3_row0.grid(column=3, row=0)

# Row 1
txt_about.grid(column=2, row=1)

app_window.mainloop()  # makes the window still opened."""
