from bs4 import BeautifulSoup

# Getting the whole content of the HTML file:
with open("table.html", encoding="utf8") as file:  # ENCODING super important!
    raw = file.read()

html = BeautifulSoup(raw, "html.parser")  # Analysing the object as HTML content.

# Extracting the columns' names:
columns = [i.getText() for i in html.select(selector="th")]
# Extracting the total of <TR> (rows) of the table, excepting the header <TR>:
rows_amount = len([i for i in html.find_all("tr")]) - 1
# Extracting the content as string from each relevant cell:
body_content = [i.getText(" ", strip=True) for i in html.find_all(class_=["s1", "s2"])]  # this " ", strip=True fixes when tags has unwated break as you check at table through the cells "Paraná" and "Pernambuco"..
space = "    "

for col in columns:
    print(col, end=space)

print()

for i in range(rows_amount):
    for col in range(len(columns)):
        if col != (len(columns) - 1):
            print(body_content[0], end=space)
        else:
            print(body_content[0])
        del body_content[0]
