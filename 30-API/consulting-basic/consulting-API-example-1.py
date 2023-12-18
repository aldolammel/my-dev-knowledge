"""
API (Application Programming Interface):
An API is a set of commands, functions, protocols, and objects that programmers can use to create software or interact
with an external system.

What is "API endpoint"?
It's the link used to request the data. ISS Postion API endpoint is http://api.open-notify.org/iss-now.json

Important: the "requests" module is the most popular way in python to work with API's
https://pypi.org/project/requests/

"""

import requests

# Taking the ISS basic data:
# Website: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# Endpoint:
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# HTML error handling:
response.raise_for_status()
# Extracting data:
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (float(longitude), float(latitude))
print(iss_position)
