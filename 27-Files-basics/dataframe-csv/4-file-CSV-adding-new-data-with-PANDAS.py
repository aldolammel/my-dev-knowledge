"""
PANDAS: ADDING NEW DATA IN A DATAFRAME (Excel, CSV) FILE

"""

import pandas

print("Converting a dictionary to a Data Frame:")
dictionary = {
    "students": ["John", "Anna", "Billy"],
    "scores": [76, 57, 65]
}
print(f"Original dictionary: {dictionary}")
dataframe = pandas.DataFrame(dictionary)
print(f"After conversion:\n{dataframe}")

print("\n- - -\n")

print("Creating a CSV file from a data frame built by Pandas:")
dataframe.to_csv("class27z-db-created.csv")
print("The CSV file has been created!")



"""

For more elaborated example to using CSV file to storage information, check the folder: \33-Web-development-introduction\9-flask-wtforms\

"""