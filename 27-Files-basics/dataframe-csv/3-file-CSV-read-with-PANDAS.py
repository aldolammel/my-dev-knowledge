"""
PANDAS MODULE: HOW TO OPEN AND CONSULT A CSV FILE
CSV = Comma Separated Values

"""

import pandas

print("Reading CSV file through Pandas module:")
print(pandas.read_csv("db_to_read.csv"))

print("\n- - -\n")

print("Reading a specific column through Pandas module:")
data3 = pandas.read_csv("db_to_read.csv")
print(data3["temp"])

print("\n- - -\n")

print("Converting a specific column from CSV to list through Pandas module:")
data4 = pandas.read_csv("db_to_read.csv")
print(data4["temp"].to_list())

print("\n- - -\n")

print("Converting the whole CSV file in a dictionary through Pandas module:")
data4 = pandas.read_csv("db_to_read.csv")
print(data4.to_dict())

print("\n- - -\n")

print("Reading the average value from a specific column:")
data5 = pandas.read_csv("db_to_read.csv")
print(data5["temp"].mean())

print("\n- - -\n")

print("Reading the maximum value from a specific column:")
data6 = pandas.read_csv("db_to_read.csv")
print(data6["temp"].max())

print("\n- - -\n")

print("Reading only a specific row entries:")
data7 = pandas.read_csv("db_to_read.csv")
print(data7[data7["day"] == "Monday"])

print("\n- - -\n")

print("Find the row with the highest temperature:")
data8 = pandas.read_csv("db_to_read.csv")
print(data8[data8["temp"] == data8["temp"].max()])

print("\n- - -\n")

print("Converting a Pandas value to an integer:")
data9 = pandas.read_csv("db_to_read.csv")
tempe_monday = data9[data9["day"] == "Monday"]
tempe_monday_C = int(tempe_monday["temp"])
tempe_monday_F = tempe_monday_C * 9/5 + 32
print(f"{tempe_monday_C}ºC")
print(f"{tempe_monday_F}ºF")

print("\n- - -\n")

print("\n>> Create a dictionary showing the week day and its temperature:")
data10 = pandas.read_csv("db_to_read.csv")
phonetic_dict = {row["day"]: row["temp"] for (day, row) in data10.iterrows()}
print(phonetic_dict)

print("\n>> Print out only the valid week day typed by the user:")
word = input("Enter the week day: ").strip().title()
output_printing = {print(f"{key} = {value}") for (key, value) in phonetic_dict.items() if word == key}
output_new_dict = {key: value for (key, value) in phonetic_dict.items() if word == key}
print(output_new_dict)  # alternative way to print the new dict.


"""

For more elaborated example to using CSV file to storage information, check the folder: \33-Web-development-introduction\9-flask-wtforms\

"""