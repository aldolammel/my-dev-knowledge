"""
WEB SCRAPING:
Web scraping refers to the extraction of data from a website. This information is collected and then exported into
a format that is more useful for the user.

Beautiful soup doc:
https://www.google.com/search?q=python+Beautiful+Soup+Documentation&oq=python+Beautiful+Soup+Documentation&aqs=edge..69i57.3464j0j4&sourceid=chrome&ie=UTF-8

"""

from bs4 import BeautifulSoup

# Getting the whole content of the HTML file:
with open("website.html", encoding="utf8") as file:  # ENCODING super important!!!!!!!!!!
    contents = file.read()

# Saying to BS4 with type of content it will find out (html), and hold that:
html_extracted = BeautifulSoup(contents, "html.parser")

print("\nExtracting all html:")
print(html_extracted)

print("\n\nExtracting all html (with indentation):")
print(html_extracted.prettify())

print("\n\nExtracting the whole texts (.get_text()):")
print(html_extracted.get_text())

print("\n\nExtracting the whole texts (.getText()):")
print(html_extracted.getText())  # <---- this is better right?

print("\n\nExtracting the title's content:")
print(html_extracted.title.string)

print("\n\nExtracting all links:")
for tag in html_extracted.find_all("a"):  # <---- One of the most useful method of BS!
    print(tag.get("href"))

print("\n\nExtracting a specific tag among a bunch of the same tag, using its id:")
h1_named = html_extracted.find(name="h1", id="named")
print(h1_named.string)

print("\n\nExtracting a specific tag among a bunch of the same tag, using its id:")
h3_class = html_extracted.find(name="h3", class_="heading")
print(h3_class.string)

print("\n\nExtracting all tags using specific css class:")
specific_css_class = html_extracted.select(".heading")
print(specific_css_class)  # it will be a list/array

print("\n\nExtracting multiples specific tag inside other tags:")
more_tags_inside = html_extracted.select(selector="p a")
print(more_tags_inside)

print("\n\nExtracting one specific tag inside other tags:")
one_tag_inside = html_extracted.select_one(selector="p a")
print(one_tag_inside)

print("\n\nExtracting a specific value from a tag:")
value_tag = html_extracted.find("input")
result = value_tag.get("maxlength")
print(result)
