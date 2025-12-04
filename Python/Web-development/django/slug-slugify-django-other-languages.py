
"""
    DJANGO: SLUG, SLUGIFY STRINGS FOR OTHER NON-ENGLISH LANGUAGES

    >> Slugify with Django for English:
        ./slug-slugify-django-english.py
    
    >> Slugify with raw Python for English:
        /Python/python-knowledge/slug-slugify-english.py

    >> Slugify with raw Python for non-English languages:
        /Python/python-knowledge/slug-slugify-other-languages.py
"""

# SIMPLEST FOR DJANGO:
# Django can handle basic foreigner languages like Brazilian PT:
# ./slug-slugify-django-english.py


# FOR MORE OPTIONS:
# $ python3 -m pip install python-slugify
# Or $ uv add python-slugify       <---------
from slugify import slugify
text = "Ação, Reação & Emoção!"
# Result: "acao-reacao-and-emocao"
# With custom options:
slug = slugify(text, lowercase=True, separator='-', max_length=50)
# Keep certain characters:
slug = slugify(text, replacements=[['&', 'e']])
# Result: "acao-reacao-e-emocao"