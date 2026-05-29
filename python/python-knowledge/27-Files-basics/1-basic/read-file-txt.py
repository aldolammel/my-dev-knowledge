"""
HOW TO OPEN/READ A FILE:

Tips:
1) if you try to open a file doesn't exist, the file will be created for you.
2) if you don't declare the opening-mode, it will be read-only.

"""

# Regular way:
# file = open("db.txt", encoding="utf-8")
# contents_1 = file.read()
# print(contents_1)

# Recommended way:
with open("db.txt", mode="r", encoding="utf-8") as file:  # r = read only / w = clear and write / a = append new data in the file
    contents_2 = file.read()
    print(contents_2)
