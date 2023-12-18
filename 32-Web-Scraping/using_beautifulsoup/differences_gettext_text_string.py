from bs4 import BeautifulSoup

html_raw = '<title>This is a title</title>Lorem ipsum dolor <strong>end of the text</strong>.'
html = BeautifulSoup(html_raw, 'html.parser')

print(html.get_text())                # This is a titleLorem ipsum dolor end of the text.
print(html.text)                      # This is a titleLorem ipsum dolor end of the text.
print(html.string)                    # None
print(html.find('title').get_text())  # This is a title
print(html.find('title').string)      # This is a title
