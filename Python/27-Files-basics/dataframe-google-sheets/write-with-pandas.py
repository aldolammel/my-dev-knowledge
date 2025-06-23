"""

Using gspread + service account from Google Cloud Developer Console to read and write to accessible Google Sheets
Pros — More control & APIs to interact with the doc — including writing to the doc

Cons — Slightly more hassle in setting up credentials, require google cloud account

"""

import gspread as gs
import pandas as pd

# Google setup:
# https://console.cloud.google.com/apis/credentials?project=python-384118
SHEET_ID = "1xFAp9BdHq7Ucjzzlr09GC7TgCTe0dwuQ40auB3JCkTU"
SHEET_TAB = "sheet_tab_2"

# Reading the Google Spreadsheet:
google_console = gs.service_account("file_private_credentials.json")
sheet_file = google_console.open_by_key(SHEET_ID)
sheet_tab = sheet_file.worksheet(SHEET_TAB)
rows_v1 = sheet_tab.get_all_records()
print(
    f"Visualizing without PANDAS:\n"
    f"{rows_v1[:3]}\n"
    f"\n- - -\n"
)
df_v1 = pd.DataFrame(rows_v1)
print(
    f"Visualizing with PANDAS:\n"
    f"{df_v1.head()}"
)

# Updating the Google Spreadsheet:
nums_chosen = list()
for i in range(5):
    user_choice = float(input(f"\n>> {i+1}/5 >> Type a float or integer number: ").strip())
    nums_chosen.append(user_choice)

sheet_tab.update("B2:B6", [[nums_chosen[0]], [nums_chosen[1]], [nums_chosen[2]], [nums_chosen[3]], [nums_chosen[4]]])

print("\n\nLook the result at 'Open' column: \n\n")

rows_v2 = sheet_tab.get_all_records()
df_v2 = pd.DataFrame(rows_v2)
print(df_v2.head())
