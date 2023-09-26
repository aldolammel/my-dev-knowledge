"""
API (Application Programming Interface) with PARAMETERS

"""

import requests

# CONSTANTS:
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"  # Notice that i'm not using parameters here!
API_PARAMS = {  # so the good practices in Python is to set the parameters like this, in a dictionary:
    "lat": -29.955090,
    "lon": -51.625332,
    "appid": "5e2fabfc623c71cedcfa11e8816b25da",
    "exclude": "current,minutely,hourly,alerts",
    "units": "metric",
}

# Calling API:
response = requests.get(url=API_ENDPOINT, params=API_PARAMS)  # and after that, configure the parameters like this.
# Error handling:
response.raise_for_status()
# Extracting data:
data = response.json()
print(data)
