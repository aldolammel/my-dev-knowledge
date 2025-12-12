
"""
    DJANGO > MODEL TYPES: VIRTUAL MODEL

    
"""

# E.g. in models.py
class PagexElementSelector(models.Model):  # Virtual model!
    class Meta:
        managed = False  # table not managed by Django!
        verbose_name = "Adicionar Elemento"
        verbose_name_plural = "Adicionar Elemento"

    def __str__(self):
        return "Adicionar Elemento"



"""
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

MORE ABOUT: CLASS META MANAGED
    ./meta-managed.txt
    
"""


