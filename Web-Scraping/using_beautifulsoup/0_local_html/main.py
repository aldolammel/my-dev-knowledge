"""
WEB SCRAPING:
Web scraping refers to the extraction of data from a website. This information is collected and then exported into
a format that is more useful for the user.

Beautiful soup doc:
https://www.google.com/search?q=python+Beautiful+Soup+Documentation&oq=python+Beautiful+Soup+Documentation&aqs=edge..69i57.3464j0j4&sourceid=chrome&ie=UTF-8

"""

from bs4 import BeautifulSoup

# Getting the whole content of the HTML file:
with open("website.html", encoding="utf8") as file:  # ENCODING super important!
    raw = file.read()

# Saying to BS4 with type of content it will find out (html), and hold that:
html = BeautifulSoup(raw, "html.parser")

# Extracting all html (with indentation):
print(html.prettify())
