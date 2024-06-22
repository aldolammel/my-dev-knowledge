"""
JSON (JavaScript Object Notation):

    JavaScript Object Notation file is a lightweight data-interchange format that is easy for humans to read and write,
    and easy for machines to parse and generate. JSON is primarily used to transmit data between a server and a
    web application.

    IMPORTANT:
    Json always returns a dictionary.

    Tools:
        Postman > it helps developers design, build, test and manage APIs.
        Insomnia > Postman alternative.

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
