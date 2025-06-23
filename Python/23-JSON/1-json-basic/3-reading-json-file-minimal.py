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

"""
import json

with open("file.json", mode="r") as file:
    print(json.load(file))
