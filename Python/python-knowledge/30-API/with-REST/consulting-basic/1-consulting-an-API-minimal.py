"""
    Python module:
    requests : https://pypi.org/project/requests/

    This example is a file that's reading a simple API. This API is returning just a number.

    CRITICAL: For this example, you need to run first this folder/example:
        /Python/python-knowledge/30-API/with-REST/creating/1-creating-example.py
"""
import requests

# Endpoint:
response = requests.get(url="http://127.0.0.1:5000/sales")  # This endpoint returns a number.
# HTML error handling:
response.raise_for_status()
# Converting the dictionary (response brought by API) to Json format:
data = response.json()
# Printing out the json with the endpoint's return:
print(data)
