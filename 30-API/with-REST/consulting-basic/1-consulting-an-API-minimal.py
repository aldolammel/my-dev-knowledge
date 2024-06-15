"""
API (Application Programming Interface) - MINIMAL:

    API is a set of commands, functions, protocols, and objects that programmers can use to create software or interact
    with an external system. API can return various types of data formats, and JSON is a popular choice due to its
    simplicity and ease of use, especially for web-based APIs. Other data formats to return: XML, PlainText, Binary.

    API ENDPOINT: it's the link used to request the data.

    Python module:
    requests : https://pypi.org/project/requests/

    --------------------------------------------------------------------------------------------------------------------

    This example is a file that's reading a simple API. This API is returning just a number.

    CRITICAL: For this example, you need to run first this folder/example:
        /creating/1-creating-example.py
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
