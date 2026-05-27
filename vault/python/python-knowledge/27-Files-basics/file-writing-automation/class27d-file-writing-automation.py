"""
HOW TO AUTOMATE FILE CREATION:
To test this code, go to "file-writing-automation" folder and delete all files inside "output/readyToSend".

"""

from time import sleep

with open("input/names/invited_names.txt", mode="r") as file:
    names = file.readlines()  # it reads each file line and built a list with them.

with open("input/letters/starting_letter.txt", mode="r") as file:
    letter_original = file.read()
    for name in names:
        stripped_name = name.strip()  # it removes the '\n' at the end from each name in the list.
        new_letter = letter_original.replace("[name]", stripped_name)
        with open(f"file-writing-automation/output/readyToSend/letter_for_{stripped_name.lower()}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
        print(f">> {stripped_name}'s letter has been created.")
        sleep(1)

print("\n---------------------\nAll letters are ready to send.")
