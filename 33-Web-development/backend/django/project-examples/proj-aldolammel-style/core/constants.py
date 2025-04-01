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
# EMAIL_HOST_USER = defined in .env file!
BRAND_NAME = 'My Brand Name'
BRAND_DESCRIPT = 'Soon...'  # TODO How do I translate this?
BRAND_EMAIL = 'xxxxxx@gmail.com'
BRAND_URL = 'https://xxxxxxxxx.com'
DEV_NAME = 'ABCOO'
DEV_URL = 'https://abcoo.com.br'
BRAND_KEYWORDS = "Soon..."  # TODO How do I translate this?

# SUB-APP PATTERNNAMES: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
NAMESPACE_0 = "admin"
NAMESPACE_1 = "general"
NAMESPACE_2 = "in"
NAMESPACE_3 = "accounts"
NAMESPACE_4 = "sub_app_name"
# Pattern names from NAMESPACE_1:
PATTERN_1_1 = 'home_view'
PATTERN_1_2 = 'xxxxxx_view'
PATTERN_1_3 = 'xxxxxx_view'
PATTERN_1_4 = 'xxxxxx_view'
PATTERN_1_5 = 'privacy_view'
PATTERN_1_6 = 'logout_view'
# Pattern names from NAMESPACE_2:
PATTERN_2_1 = 'home_view'
PATTERN_2_2 = 'xxxx_view'
PATTERN_2_3 = 'xxxx_view'
PATTERN_2_4 = 'xxxx_view'
# Pattern names from NAMESPACE_3:
PATTERN_3_1 = "register_view"
PATTERN_3_2 = "profile_view"
PATTERN_3_3 = "login"
PATTERN_3_4 = "password_change_view"
PATTERN_3_5 = "password_reset"
PATTERN_3_6 = "password_reset_done"
PATTERN_3_7 = "password_reset_confirm"
PATTERN_3_8 = "password_reset_complete"
PATTERN_3_9 = "logout"
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
PATH_NAMESPACE_0_USERS = "/" + NAMESPACE_0 + "/" + NAMESPACE_3 + "/user/"  # '/admin/auth/user/'
#PATH_XXXXX_XXXXX_XXXX = 'icons/events/attack/'

# DATA FOR DATABASE (WARNING!): - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# If values are changed without maintenance on database, multiple errors will raise up!
CHOICES_PROFILE_TYPE = (
    ("1", "Personal"),  # ("1", _("Personal")),
    ("2", "Business"),  # ("2", _("Business")),
)
CHOICES_SEX = (
    ('f', 'Female'),  # ('f', _('Female')),
    ('m', 'Male'),  # ('m', _('Male')),
    ('i', 'Intersex'),  # ('i', _('Intersex')),
)
CHOICES_STATUS_CONTENT = (
    ('on', 'Active'),  # _('Active')
    ('off', 'Archived'),  # _('Archived')
)

# OTHERS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# REL_ for 'related_name' on models!
# VAL_ for constant values!

# VAL_RETROACTIVE_ADDING_LIMIT = 180  # in days (Retroactive Adding Limit)!
# VAL_HEADACHE_LIFE_TIME_MAX = 3  # in days, based in Headache Life Time Maximum.
# VAL_HEADACHE_LIFE_TIME_MIN = 15  # in minutes, based in Headache Life Time Minimum.
# VAL_EVT_ATTK_NOTE_MAXLNGH = 600
VAL_PROFILE_1_BIRTH_MIN = 13  # in years old. Legal matter in Brazil!
VAL_PROFILE_1_BIRTH_MAX = 85  # in years old. Migraine over than 70 is rare!
VAL_PROFILE_1_NAME_MAXLNGH = 12
VAL_PROFILE_1_DEL_SCHEDULE = 30  # in days!
# VAL_PROFILE_2_DEL_SCHEDULE = VAL_PROFILE_1_DEL_SCHEDULE  # in days!
# VAL_PROFILE_2_BNAME_MAXLNGH = 50
# VAL_PROFILE_2_LEGAL_MAXLNGH = 100
# VAL_PROFILE_2_CITY_MAXLNGH = 40
# VAL_PROFILE_2_DESC_MAXLNGH = 400
REL_PROFILE_1 = "profile_1"
# REL_PROFILE_2 = "profile_2"


"""
    WHERE TO USE THE NAMESPACES:
    
        /33-Web-development/backend/django/3-1-backend-models-database/namespaces-where-to-use.txt


"""
