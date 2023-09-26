"""
HOW TO OPEN A FILE:

Tips:
1) if you try to open a file doesn't exist, the file will be created for you.
2) if you don't declare the opening-mode, it will be read-only.

"""

# Regular way:
# file = open("class27z-db.txt")
# contents_1 = file.read()
# print(contents_1)

# Recommended way:
with open("class27z-db.txt", mode="r") as file:  # r = read only / w = clear and write / a = append new data in the file
    contents_2 = file.read()
    print(contents_2)
