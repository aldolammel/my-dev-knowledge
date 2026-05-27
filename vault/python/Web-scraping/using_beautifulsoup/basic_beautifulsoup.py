"""
WEB SCRAPING:
Web scraping refers to the extraction of data from a website. This information is collected and then exported into
a format that is more useful for the user.

Beautiful soup doc:
https://www.google.com/search?q=python+Beautiful+Soup+Documentation&oq=python+Beautiful+Soup+Documentation&aqs=edge..69i57.3464j0j4&sourceid=chrome&ie=UTF-8

"""

from bs4 import BeautifulSoup

# Getting the whole content of the HTML file:
with open("0_local_html/website.html", encoding="utf8") as file:  # ENCODING super important!
    raw = file.read()

# Saying to BS4 with type of content it will find out (html), and hold that:
html = BeautifulSoup(raw, "html.parser")

# Extracting all html:
print(html)

print("\n-----\n")

# Extracting all html (with indentation):
print(html.prettify())

print("\n-----\n")

# Extracting the whole texts:
print(html.getText())
# print(html.get_text())  # the same!

print("\n-----\n")

# Extracting the title's content:
print(html.title.string)

print("\n-----\n")

# Extracting all links:
for tag in html.find_all("a"):  # <---- One of the most useful method of BS!
    print(tag.get("href"))

print("\n-----\n")

# Extracting a specific amount of a tag:
for tag in html.find_all("a", limit=2):
    print(tag.get("href"))

print("\n-----\n")

# Extracting all tags with these classnames, individually:
for tag in html.find_all(class_=["heading", "custom_example"]):
    print(tag.getText())

print("\n-----\n")

# Extracting all occurrences of an id:
find_id = html.find_all(id="named")
print(find_id)

print("\n-----\n")

# Extracting all tags with these classnames composition:
more_than_one_css_class = html.select(".heading.custom_example")
# Even more specific:
# more_than_one_css_class = html.select("h3.heading.custom_example")
print(more_than_one_css_class)  # it will be a list/array

print("\n-----\n")

# Extracting one specific tag with a specific id:
h1_named = html.find(name="h1", id="named")
print(h1_named.string)

print("\n-----\n")

# Extracting a specific tag among a bunch of the same tag, using its id:
h3_class = html.find(name="h3", class_="heading")
print(h3_class.string)

print("\n-----\n")

# Extracting all tags using a specific css class:
specific_css_class = html.select(".heading")
print(specific_css_class)  # it will be a list/array"""

print("\n-----\n")

# Extracting all tags with this feature (a tag inside other tag):
more_tags_inside = html.select(selector="p a")
print(more_tags_inside)

print("\n-----\n")

# Extracting just one tag with this feature (a html tag inside other html tag):
one_tag_inside = html.select_one(selector="p a")
print(one_tag_inside)

print("\n-----\n")

# Extracting a specific value from a tag:
value_tag = html.find("input")
print(f"The max length of the input tag is: {value_tag.get('maxlength')}")
