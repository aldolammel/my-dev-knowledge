
"""
    PYTHON: SLUG, SLUGIFY STRINGS FOR NON-ENGLISH LANGUAGES

    >> Slugify with raw Python for English:
        ./slug-slugify-english.py
        
    >> Slugify with Django for English:
        /Python/Web-development/django/slug-slugify-django-english.py

    >> Slugify with Django for non-English languages:
        /Python/Web-development/django/slug-slugify-django-other-languages.py
"""

import re
import unicodedata

def slugify(txt):
    # First, normalize and convert accented chars to their base form:
    txt = unicodedata.normalize('NFKD', txt)
    
    # Create a mapping for common Portuguese chars:
    char_map = {
        'ç': 'c',
        'Ç': 'C',
        'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
        'Á': 'A', 'À': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
        'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'ñ': 'n',
        'Ñ': 'N',
    }
    
    # Replace accented characters:
    for accented, base in char_map.items():
        txt = txt.replace(accented, base)
    
    # Now remove any remaining non-ASCII chars and process:
    txt = txt.encode('ascii', 'ignore').decode('ascii')
    txt = re.sub(r'[^\w\s-]', '', txt.lower())
    txt = re.sub(r'[-\s]+', '-', txt).strip('-')
    return txt

txt = "Aldo e sua canção de mochilão gaúcho em português br!"
slugify_pt(txt)
# aldo-e-sua-cancao-de-mochilao-gaucho-em-portugues-br
slugify_pt(txt).replace('-', '_')
# aldo_e_sua_cancao_de_mochilao_gaucho_em_portugues_br
