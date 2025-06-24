import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
response.raise_for_status()

database = response.json()
# print(len(data["results"]))
# print(data["results"])

api_db = database["results"]
