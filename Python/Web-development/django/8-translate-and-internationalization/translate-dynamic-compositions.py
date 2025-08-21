"""

    TRANSLATE WITH DYNAMIC COMPOSITION:


        >> You can build smart translations for all types of sensence through any language using 
            dynamic compositions with Parler module.
            

"""

# E.g. in /config-folder/constants.py:
# More about: /Python/Web-development/django/3-1-backend-models-database/_constants-map.py
VAL_PROFILE_NAME_MAXLNGH = 20


# E.g. in /config-folder/language.py:
# More about: /Python/Web-development/django/8-translate-and-internationalization/language-file-example.py
LB_PROFILE_NAME = _('Profile Name')
TX_ERRO_PROFILE_NAME_MAXLNGH = _('%(txt)s cannot exceed %(val)s characters.')


# E.g. in /accounts/models.py:

from myconfigfolder.language as lng
from myconfigfolder.constants import VAL_PROFILE_NAME_MAXLNGH

class Profile(models.ModelForm):
    name = models.CharField(
        max_length=VAL_PROFILE_NAME_MAXLNGH,
        verbose_name = lng.LB_PROFILE_NAME,
        error_messages={
            'max_length': lng.TX_ERRO_PROFILE_NAME_MAXLNGH % {
                'txt': lng.LB_PROFILE_NAME,
                'val': VAL_PROFILE_NAME_MAXLNGH,
            },
        },
    )


"""
    WARNING:
    
    Unfortunately, you cannot make all translations directly on the 'language.py' file.
    If you use at same time a translatable variable that will feed another translatable variable
    (dynamic composition), Parler badly tries to translate everything at the same time, bringing
    weird behaviors, some times translating to a wrong language, even making the 'makemigrations'
    command performs unwanted changes.
    
    Never do this (directly using gettext_lazy aside):
    
        TX_ERRO_PROFILE_NAME_MAXLNGH = _('%(txt)s cannot exceed %(val)s characters.') % {
            'txt': lng.LB_PROFILE_NAME,
            'val': VAL_PROFILE_NAME_MAXLNGH,
        },


"""