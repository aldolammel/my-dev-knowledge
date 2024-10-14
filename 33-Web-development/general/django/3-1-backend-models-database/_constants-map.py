
"""
    CONSTANT MAP:
    
        Recommended be deployed in config-folder as 'constants.py' file.
        
        To call these constants at the same folder:
        
            from .constants import <constant_name>, ...
        
        To call them at other folder:
        
            from <config-folder-name>.constants import <constant_name>, ...
            
"""

# To avoid circular-import with language.py, translatable constants must stay here!
# from django.utils.translation import gettext_lazy as _

    
# APP ESSENTIAL INFO: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ADMIN_EMAIL = 'xxxxx@gmail.com'
BRAND_NAME = 'My Brand Name'
BRAND_DESCRIPT = 'Soon...'
BRAND_EMAIL = 'xxxxxx@gmail.com'
BRAND_URL = 'https://xxxxxxxxx.com'
DEV_NAME = 'ABCOO'
DEV_URL = 'https://abcoo.com.br'

# SUB-APP PATTERNNAMES: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Critical: do not use sub-app names as a constant. Django demands it as explicity, unfortunately!
# Pattern names from NAMESPACE_1:
PATTERN_1_1 = 'home_view'
PATTERN_1_2 = 'xxxxxx_view'
PATTERN_1_3 = 'xxxxxx_view'
PATTERN_1_4 = 'xxxxxx_view'
PATTERN_1_5 = 'privacy_view'
# Pattern names from NAMESPACE_2:
PATTERN_2_1 = 'home_view'
PATTERN_2_2 = 'xxxx_view'
PATTERN_2_3 = 'xxxx_view'
PATTERN_2_4 = 'xxxx_view'
# Pattern names from NAMESPACE_3:
PATTERN_3_1 = 'register_view'
PATTERN_3_2 = 'profile_view'
# Pattern names from NAMESPACE_4:
PATTERN_4_1 = 'xxxxxx_view'
PATTERN_4_2 = 'xxxxxx_view'
PATTERN_4_3 = 'xxxxxx_view'
PATTERN_4_4 = 'xxxxxx_view'
PATTERN_4_5 = 'xxxxxx_view'
PATTERN_4_6 = 'xxxxxx_view'
PATTERN_4_7 = 'xxxxxx_view'
PATTERN_4_8 = 'xxxxxx_view'

# PATHS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PATH_XXXXX_XXXXX_XXXX = 'icons/events/attack/'

# DATA FOR DATABASE (WARNING!): - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# If values are changed without maintenance on database, multiple errors will raise up!
CHOICES_SEX = (
    ('f', 'Female'),    # ('f', _('Female')),
    ('m', 'Male'),      # ('m', _('Male')),
    ('i', 'Intersex'),  # ('i', _('Intersex')),
)
CHOICES_STATUS_CONTENT = (
    ('on', 'Active'),     # _('Active')
    ('off', 'Archived'),  # _('Archived')
)

# OTHERS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# REL_ for 'related_name' on models!
# VAL_ for constant values!




"""
    WHERE TO USE THE NAMESPACES:
    
        /33-Web-development/general/django/3-1-backend-models-database/namespaces-where-to-use.txt


"""