"""
WORKING WITH json FILES: HOW TO READ ONE

Tips:
> READ = json.load()
> WRITE = json.dump()
> UPDATE = json.update()

Important: if the db file is empty, you'll face an error.

"""

from json import load

with open("class27z-db.json", mode="r") as file:
    print(load(file))
