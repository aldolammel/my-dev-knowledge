"""
API (Application Programming Interface):

    API is a set of commands, functions, protocols, and objects that programmers can use to create software or interact
    with an external system. API can return various types of data formats, and JSON is a popular choice due to its
    simplicity and ease of use, especially for web-based APIs. Other data formats to return: XML, PlainText, Binary.

    API ENDPOINT: it's the link used to request the data.

    Python module:
    requests : https://pypi.org/project/requests/

    --------------------------------------------------------------------------------------------------------------------

    This example is a file that's reading a simple API: ISS position.



"""
import requests

# Endpoint:
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# HTML error handling:
response.raise_for_status()
# Converting the dictionary (response brought by API) to Json format:
data = response.json()
# Printing out the raw json returned from that endpoint (API):
print(data)
# Working the response data:
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (float(longitude), float(latitude))
# Printing out all data received:
print(f"ISS current position: {iss_position}")
