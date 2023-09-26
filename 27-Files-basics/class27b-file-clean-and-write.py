"""
HOW TO WRITE IN A FILE:

Tips:
1) when we use the -with open- command, is not needed to close the opened file.
2) Open the "class27z-db.txt" file after run this code.

"""

# It will CLEAR and write a new data:
with open("class27z-db.txt", mode="w", newline="", encoding="utf-8") as file:
    file.write("It will always be the first unique "
               "line in the file because the mode is W that means 'clear and write'. "
               "And it will support UTF-8 characters like çççççááááõõõ.\n")


