"""
WORKING WITH json FILES: HOW TO APPEND NEW INFORMATION, PRESERVING THE OLD ONE

Tips:
> READ = json.load()
> WRITE = json.dump()
> UPDATE = json.update()

Important: if the db file is empty, you'll face an error.
Change this dictionary content, run it and check manually the db file.

"""

import json

# new data:
new_data_dict = {"zaz.com.br": {"email": "zeca@gmail.com", "password": "11111"}}

# reading:
with open("class27z-db.json", mode="r") as file:
    # reading the old data from db file and setting the content in a container:
    current_content = json.load(file)
    # updating/appending the old data with the new one at the same container:
    current_content.update(new_data_dict)

# writing:
with open("class27z-db.json", mode="w") as file:
    # writing the updated container in the db file:
    json.dump(current_content, file, indent=4)
