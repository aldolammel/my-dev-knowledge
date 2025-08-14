"""
    Python module:
    requests : https://pypi.org/project/requests/

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
