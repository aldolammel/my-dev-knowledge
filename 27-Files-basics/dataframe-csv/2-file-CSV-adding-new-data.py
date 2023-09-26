"""

CSV MODULE: HOW TO ADD NEW DATA IN A CSV FILE
CSV = Comma Separated Values

"""

import csv

print(">> Writing in a CSV file through CSV module:")

input_day = input(">> Day like 'Monday': ").strip()
input_temperature = input(">> Temperature like '12': ").strip()
input_weather = input(">> Weather like 'Rain': ").strip()

with open("../class27writing-db.csv", mode="a", encoding="utf-8") as file:
    file.write(f"\n{input_day},{input_temperature},{input_weather}")


"""

For more elaborated example to using CSV file to storage information, check the folder: \33-Web-development-introduction\9-flask-wtforms\

"""
