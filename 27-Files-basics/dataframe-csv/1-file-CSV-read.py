"""
CSV MODULE: HOW TO OPEN AND CONSULT A CSV FILE
CSV = Comma Separated Values

"""

import csv

print(">> Reading CSV file with no module:")

with open("../class27z-db.csv", mode="r", encoding="utf-8") as file1:
    data1 = file1.readlines()
    print(data1)

print("\n- - -\n")

print(">> Reading CSV file through CSV module:")

with open("../class27z-db.csv", mode="r", newline="", encoding="utf-8") as file2:
    data2 = csv.reader(file2, delimiter=",")
    for row in data2:
        print(row)


"""

For more elaborated example to using CSV file to storage information, check the folder: \33-Web-development-introduction\9-flask-wtforms\

"""
