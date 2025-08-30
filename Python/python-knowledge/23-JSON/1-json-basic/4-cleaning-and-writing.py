"""
    This example: doesn't matter what the json file contains, after this,
    that will be cleaned and written with the new information.
"""
import json

# New data for the json:
new_data = {
    "aldolammel.com": {
        "email": "aldolammel@gmail.com",
        "password": "123456"
    }
}
# writing / every data in json will be deleted and re-written by the new data (current_content):
with open("file.json", mode="w") as file:
    json.dump(new_data, file, indent=4)  # json.dump(new content, json file, indentation length)

# Debug purposes only:
print("Open that file.json to check the result.")
