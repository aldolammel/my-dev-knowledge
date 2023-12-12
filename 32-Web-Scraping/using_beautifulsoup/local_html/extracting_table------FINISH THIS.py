from bs4 import BeautifulSoup


# Getting the whole content of the HTML file:
with open("table.html", encoding="utf8") as file:  # ENCODING super important!
    html_raw = file.read()

html = BeautifulSoup(html_raw, "html.parser")  # Analysing the object as HTML content.

# Get all column names:
col_names = [i.getText() for i in html.find_all("th")]

# body_content = [i.getText() for i in html.find_all(class_="data-table__value")]
body_content = [i.getText() for i in html.find_all(class_="data-table__value")]

table_content = list()
row = list()

ctr = 1
for i in range(25):
    if ctr <= len(col_names):
        row.append(body_content[i])
        ctr += 1
    else:
        table_content.append(row)
        row = list()
        ctr = 1

for i in range(len(table_content)):
    print(f"{i + 1}: {table_content[i]}")
