"""
WEB SCRAPING:
Web scraping refers to the extraction of data from a website. This information is collected and then exported into
a format that is more useful for the user.

Beautiful soup doc:
https://www.google.com/search?q=python+Beautiful+Soup+Documentation&oq=python+Beautiful+Soup+Documentation&aqs=edge..69i57.3464j0j4&sourceid=chrome&ie=UTF-8

"""

from bs4 import BeautifulSoup
# Declarations:
movies_file = "db_movies_list.txt"
# Reading the local html file:
with open("website.html", mode="r") as file:
    content = file.read()
# Analysing the object as HTML content:
html = BeautifulSoup(content, "html.parser")
# Extracting all movie titles:
h3_class = html.find_all(name="h3", class_="jsx-4245974604")
# Adding each movie title in the movies_list (list comprehension method):
movies_list = [i.string for i in h3_class]
# db recording:
try:
    # creating the db file if it doesn't exist, and/or clean the db file:
    with open(movies_file, mode="w") as file:
        file.write("")
    # recording movie titles line by line in db file:
    with open(movies_file, mode="a") as file:
        for movie in movies_list[::-1]:
            file.write(f"{movie}\n")
finally:
    print(f"\nCheck the file: {movies_file}")
