
"""
    ERRORS: CATCHING EXCEPTIONS
    
        The way to fail more gracefully and prepare the app to fail without a catastrophic scenario.

        Syntax structure to dealing with exceptions:
        > try: .................. something that might cause an exception;
        > except + "cause": ..... do this if there WAS an exception. You can have more than 1 exception side by side;
        > else: ................. do this if there were NO exceptions;
        > finally: .............. do this no matter what happens.

        Very important: if you can use the IF/ELSE structure easilly to across some issue, do it. Use TRY-EXCEPTION structure
        when IF/ELSE is not so easy to deal, example, when you need to check if a file exists.

        MORE IN DRA. ANGELA LEE's COURSE:
        https://www.udemy.com/course/100-days-of-code/learn/lecture/20963160#overview

"""


# EXAMPLE 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("\nEXAMPLE 1 >>")
try:
    file = open("class26z-file.txt")
    print("abc" + 5)

except FileNotFoundError:
    file = open("class26z-file.txt", mode="w")  # "w" mode will force to create the file if that not exists.
    file.write("Try to delete this file manually to check the exception conditions.")
    print("The file 'class26z-file.txt' has been created...")

except TypeError as error_message:
    print(f">> ERROR >> Check your PRINT command inside the TRY: {error_message}")

else:
    print("There are NO errors/exceptions in the app.")

finally:
    file.close()
    print("The app is done.")


# EXAMPLE 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

dictionary = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
              'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
              'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor',
              'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}

print("\nEXAMPLE 2 >> Create a list of the phonetic code words from a word that the user inputs:")
while True:
    word = input("Enter a letter or word: ").strip().upper()

    try:
        output = [dictionary[letter] for letter in word]

    except KeyError:
        print("Please, only letters or words.\n")

    else:
        print(output)
        break
