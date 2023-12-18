"""
WEB SCRAPING:
Web scraping refers to the extraction of data from a website. This information is collected and then exported into
a format that is more useful for the user.

Beautiful soup doc:
https://www.google.com/search?q=python+Beautiful+Soup+Documentation&oq=python+Beautiful+Soup+Documentation&aqs=edge..69i57.3464j0j4&sourceid=chrome&ie=UTF-8

"""

from bs4 import BeautifulSoup  # ready to work with scraping information from websites
import requests  # ready to work with API
from collections import OrderedDict

# TODO: get All title articles with their links, sorted from highest to lowest vote amount,
#       and show them on python prompt.

try:
    # Extracting from specific website its news:
    site_response = requests.get("https://news.ycombinator.com/")  # Checking the site response. If 200, ok.
    site_response.raise_for_status()  # HTML errors handling.
    html_raw = site_response.text  # Extracting the website content and saving it in an object.
    html = BeautifulSoup(html_raw, "html.parser")  # Analysing the object as HTML content.

except Exception as error:
    print(f"Something wrong/No internet: {error}")

else:
    # Getting all article titles in first page:
    # titles = [i.find(name="a").getText() for i in html.find_all(class_="titleline")]  # BKP
    titles = [i.getText() for i in html.find_all(class_="titleline")]
    # Getting all article links in first page:
    links = [i.find(name="a").get("href") for i in html.find_all(class_="titleline")]
    # Getting all article votes amounts in first page, converting string to integer:
    votes = [int(score.getText().split()[0]) for score in html.find_all(class_="score")]
    # Creating the dictionary:
    results = dict()
    for i in range(len(titles)-1):
        results[votes[i]] = [titles[i], links[i]]
    # Sorting and reversing the dictionary content by key:
    sorted_results = OrderedDict(sorted(results.items(), reverse=True))
    # Print the result out:
    counter = 1
    for key, value in sorted_results.items():
        print(f"{counter}. {value[0]} | {value[1]} | {key} points")
        counter += 1
