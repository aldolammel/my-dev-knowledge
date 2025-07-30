"""

MORSE CODE TRANSLATOR HARD CODED BY @aldolammel
For translation double check, use this free online service: https://morsecode.world/international/translator.html

"""
from time import sleep

# Constants:
MORSE = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    ".": ".-.-.- ",
    ",": "--..-- ",
    "?": "..--.. ",
    "=": "-...- ",
    " ": "/"
}
# Global declarations:
cooldown = 2
char_limiter = 140
# Running the app:
while True:
    # Internal Initial Values:
    msg_translate = list()
    # User message:
    msg_user = input(str("\n\nType a short line message: ")).strip().upper()
    # Exiting command:
    if msg_user == "EXIT":
        break
    # splitting the user message by letter:
    msg_by_letter = [letter for letter in msg_user]
    # Error handling:
    if len(msg_by_letter) > char_limiter:
        print(f"\nWARNING: don't except the {char_limiter} characters limit!")
        sleep(cooldown)
        continue
    # Building the translation:
    for letter in msg_by_letter:             # for each letter of the original msg...
        for key, value in MORSE.items():     # check each morse letter...
            if letter == key:                # if the checked morse letter's the same of the original msg letter...
                msg_translate.append(value)  # translate it, including to the translation list.
    # Printing the translation out:
    [print(letter, end="") for letter in msg_translate]
    sleep(cooldown)
