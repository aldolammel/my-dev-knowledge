"""

Using pandas to read from public Google Sheets
Pros — Very easy to set up, can be only 3 lines of code to have data from Google Sheets loaded into a dataframe

Cons — Doc has to be public, thus not as secure and not recommended for confidential information

"""

import pandas as pd

# Online solution:
SHEET_ID = "1y8dQ7p6OmOWkaz3HRYaV53bY4jZ7akcvmBXd0Zb64Sg"
SHEET_TAB = "sheet_tab_2"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_TAB}"
sheet_online = pd.read_csv(SHEET_URL)
print(sheet_online.head())

# Local solution:
# Not sure if possible with files as .gsheet
