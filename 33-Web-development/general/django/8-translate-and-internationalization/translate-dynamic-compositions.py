"""

    TRANSLATE WITH DYNAMIC COMPOSITION:


        >> You can build smarth translations for all types of sensence through any language using 
            dynamic compositions with Parler module.
            

"""

# E.g. in /config-folder/constants.py:
# More about: /33-Web-development/general/django/3-1-backend-models-database/_constants-map.py
VAL_PROFILE_NAME_MAXLNGH = 20


# E.g. in /config-folder/language.py:
# More about: /33-Web-development/general/django/8-translate-and-internationalization/language-file-example.py
LB_PROFILE_NAME = _('Profile Name')
TX_ERRO_PROFILE_NAME_MAXLNGH = _('%(lb)s cannot exceed %(val)s characters.')


# E.g. in /accounts/models.py:

from myconfigfolder.language as lng
from myconfigfolder.constants import VAL_PROFILE_NAME_MAXLNGH

class Profile(models.ModelForm):
    name = models.CharField(
        max_length=VAL_PROFILE_NAME_MAXLNGH,
        verbose_name = lng.LB_PROFILE_NAME,
        error_messages={
            'max_length': lng.TX_ERRO_PROFILE_NAME_MAXLNGH % {
                'lb': lng.LB_PROFILE_NAME,
                'val': VAL_PROFILE_NAME_MAXLNGH,
            },
        },
    )


"""
    WARNING:
    
    Unfortunately, you cannot make all dynamic translations directly on 'language.py' file.
    If you use at same time a translatable variable that will feed another translatable variable, 
    Parler badly will try to translate everything at the same time, bringing weird behaviors, some
    times translating, sometimes bringing a wrong language, even making the 'makemigrations'
    command perform changes that is not needed.
    
    Never do this:
    
        TX_ERRO_PROFILE_NAME_MAXLNGH = _('%(lb)s cannot exceed %(val)s characters.') % {
            'lb': lng.LB_PROFILE_NAME,
            'val': VAL_PROFILE_NAME_MAXLNGH,
        },
        
        

    EXCEPTION:
    
    If you feed a translatable variable with a simple variable (not translatable), it's okay:
    
        TX_ERRO_PROFILE_NAME_MAXLNGH = _('Name cannot exceed %(val)s characters.') % {
            'val': VAL_PROFILE_NAME_MAXLNGH,
        },


"""