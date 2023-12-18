"""
API (Application Programming Interface):

This example needs to run at first "creating/creating_API.py"

"""

import requests

# Endpoint:
response = requests.get(url="http://127.0.0.1:5000/sales")
# HTML error handling:
response.raise_for_status()
# Extracting data:
data = response.json()
# Printing it out:
print(data)
