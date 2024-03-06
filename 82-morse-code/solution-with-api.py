import requests

to_translate = input(str("What to translate: ")).strip().upper()
# CONSTANT VALUES:
API_ENDPOINT = "https://api.funtranslations.com/translate/morse.json"
API_PARAMS = {
    "text": to_translate
}

# Calling API:
response = requests.get(url=API_ENDPOINT, params=API_PARAMS)
# Error handling:
response.raise_for_status()
# Receiving the translation:
translated = response.json()
# Print the result out:
print(f"Simple text translation:\n{translated['contents']['translated']}")
# Print the json for debug purposes:
print(f"\nJson response debug:\n{translated}")
