
"""
    DJANGO: SLUG, SLUGIFY STRINGS FOR ENGLISH

    >> Slugify with Django for non-English languages:
        ./slug-slugify-django-other-languages.py
    
    >> Slugify with raw Python for English:
        /Python/python-knowledge/slug-slugify-english.py

    >> Slugify with raw Python for non-English languages:
        /Python/python-knowledge/slug-slugify-other-languages.py
"""

from django.utils.text import slugify

text1 = "Sao Paulo and Porto Alegre got great places with bread and coffee!!!"
text2 = "São Paulo e Porto Alegre têm ótimas opções de LOCAIS com pão e café!!!"

slugify(text1)
# "sao-paulo-and-porto-alegre-got-great-places-with-bread-and-coffee"
slugify(text2)
# (It also handles spaces, removes special characters, and converts to lowercase)
# Output: "sao-paulo-e-porto-alegre-tem-otimas-opcoes-de-locais-com-pao-e-cafe"
slugify(text_br).replace('-', '_')
# Output: "sao_paulo_e_porto_alegre_tem_otimas_opcoes_de_locais_com_pao_e_cafe"