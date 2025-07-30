"""
HOW TO READ AND. AFTER THAT. WRITE IN THE SAME FILE:

Tip: run this file and, after that, open manually the "db.txt" file to check the new line added.

"""

with open("db.txt", mode="a", encoding="utf-8") as file:  # a = append
    file.write("new line\n")

print("Now check the db.txt file.")
