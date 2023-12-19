"""
API CONSULTING EXAMPLE:

CRITICAL: This example needs to run at first the "creating/1-creating-example.py"

"""

import requests

# Endpoint:
response = requests.get(url="http://127.0.0.1:5000/sales")
# HTML error handling:
response.raise_for_status()
# Converting the dictionary (response brought by API) to Json format:
data = response.json()
# Printing it out:
print(data)
