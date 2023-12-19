"""
API CONSULTING EXAMPLE:

Taking the ISS basic data:
Website: http://open-notify.org/Open-Notify-API/ISS-Location-Now/

"""

import requests

# Endpoint:
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# HTML error handling:
response.raise_for_status()
# Converting the dictionary (response brought by API) to Json format:
data = response.json()

# Printing out all data received:
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (float(longitude), float(latitude))
print(iss_position)
