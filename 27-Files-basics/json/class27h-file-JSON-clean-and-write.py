"""
WORKING WITH json FILES: HOW TO WRITE ALWAYS A CLEANED FILE

Tips:
> READ = json.load()
> WRITE = json.dump()
> UPDATE = json.update()

Important: doesn't matter what the db file contains, after this,
that will be clearned and written with the new information.

"""

from json import dump

# change the dictionary keys and/or values before to run it:
new_data = {"aldolammel.com": {"email": "aldolammel@gmail.com", "password": "123456"}}

# every thing in the db file, will be deleted and re-write the dictionary content:
with open("class27z-db.json", mode="w") as file:
    dump(new_data, file, indent=4)  # dump(new content, db file, if you want indentation)
