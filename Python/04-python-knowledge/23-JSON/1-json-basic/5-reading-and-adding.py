"""
    This example: if the json file is empty, you'll face an error.
    Change this dictionary content, run it and check manually the json file.
"""
import json

# New data for the json:
new_data = {
    "abcoo.com.br": {
        "email": "abcoo.ideias@gmail.com",
        "password": "654321"
    }
}
# reading:
with open("file.json", mode="r") as file:
    # reading the old data from db file and setting the content in a container:
    current_content = json.load(file)
    # updating/appending the old data with the new one at the same container:
    current_content.update(new_data)

# writing / every data in json will be deleted and re-written by the updated data (current_content):
with open("file.json", mode="w") as file:
    json.dump(current_content, file, indent=4)

# Debug purposes only:
print("Open that file.json to check the result.")
