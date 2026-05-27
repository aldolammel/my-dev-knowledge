"""
    POPULAR MODULES TO CONSULTING AN API:
    > requests - https://pypi.org/project/requests/
"""

import requests
from twilio.rest import Client  # Site service PASSWORD = dLpHlprEDuQuq01r


# INITIAL VALUES:
will_rain = False
# CONSTANTS:
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_PARAMS = {
    "lat": -10.154580,
    "lon": -67.736511,
    "appid": "5e2fabfc623c71cedcfa11e8816b25da",
    "exclude": "current,minutely,daily,alerts",
    "units": "metric",
}
ACCOUNT_SID = "xxxxxx"
AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Calling API:
response = requests.get(url=API_ENDPOINT, params=API_PARAMS)
# Error handling:
response.raise_for_status()
# Extracting data:
weather_full_data = response.json()
# Extracting only the next 12 hours forecast:
weather_12h_data = weather_full_data["hourly"][:12]  # python slicing method in replace of "for looping" ;)
# looping to check each available hours forecast:
for hour_data in weather_12h_data:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:  # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
        will_rain = True
        break

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella!",
        from_="+15856393790",
        to="+5551980394586"
    )
    if message.status == "queued":
        print("SMS will be sent soon!")
    else:
        print(message.status)
