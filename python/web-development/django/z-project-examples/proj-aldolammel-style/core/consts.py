"""
    CONSTANT MAP:
    
        Recommended be deployed in config-folder (core) as 'consts.py' file.
        
        To call these constants at the same folder:
        
            from . import consts

            Then you call the vars like consts.<var_name>
        
        To call them at other folder:
        
            from core import consts

            Then you call the vars like consts.<var_name>
"""

# To avoid circular-import with lang.py or settings.py, for example, translatable constants and any other constants defined in other places must be defined here manually as well!

# APP ESSENTIAL INFO FOR CMS ONLY - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ADMIN_EMAIL = "xxxxxxxx@xxxxx.com"
BRAND_NAME = "xxxxxxxxxxxxx"
BRAND_EMAIL = "xxxxxxxxxxxxxxxxxxxxx"
BRAND_URL = "https://xxxxxxxxxxxxxxxxx"
DEV_NAME = "xxxxxxxxxxxxxxxx"
DEV_URL = "https://xxxxxxxxxxxxx"

# PAGEX USERS:
# Pagex is not allowed to provide context_processors to Django CMS interface yet, so keep this information above updated too!