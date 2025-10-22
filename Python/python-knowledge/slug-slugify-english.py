
"""
    PYTHON: SLUG, SLUGIFY STRINGS FOR ENGLISH

    >> Slugify with raw Python for non-English languages:
        ./slug-slugify-other-languages.py

    >> Slugify with Django for English:
        /Python/Web-development/django/slug-slugify-django-english.py

    >> Slugify with Django for non-English languages:
        /Python/Web-development/django/slug-slugify-django-other-languages.py
"""

import re
import unicodedata

def slugify(txt):
    # Normalize unicode characters
    txt = unicodedata.normalize('NFKD', txt).encode('ascii', 'ignore').decode('ascii')
    # Convert to lowercase and remove special characters
    txt = re.sub(r'[^\w\s-]', '', txt.lower())
    # Replace spaces and hyphens with single hyphens
    txt = re.sub(r'[-\s]+', '-', txt).strip('-')
    return txt

slugify("Hello World! This is a Test")
# hello-world-this-is-a-test

