# To avoid circular-import with lang.py, translatable constants must stay here!
# from django.utils.translation import gettext_lazy as _


# PATHS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#PATH_API_SOMETGHING = "api/something"  # It's also declared in /frontend/src/stores/global.js
#PATH_JSON_CATS = "c"  # It's also declared in /frontend/src/router/router.js
#PATH_IMG = "something/images/"
#PATH_FILE = "something/to_download/"

# DATA FOR DATABASE (WARNING!) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# If values are changed without maintenance on database, multiple errors will raise up!
#VAL_SOMETHING_A = "a"
#VAL_SOMETHING_B = "b"
#VAL_SOMETHING_C = "c"
#CHOICES_CLASSREFEXAMPLE = (
    #(VAL_SOMETHING_A, 'Example A (default)'),
    #(VAL_SOMETHING_B, 'Example B'),
    #(VAL_SOMETHING_C, 'Example C'),
#)

# OTHERS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# REL_ for 'related_name' on models!
# VAL_ for constant values!
VAL_GENERIC_MIN = 3
VAL_GENERIC_MAX = 40
VAL_GENERIC_DESC_MIN = 20
VAL_GENERIC_DESC_MAX = 140
VAL_SLUG_ADD_LIMIT = 5
VAL_CLASSREFEXAMPLE_ATTREXAMPLE_MIN = VAL_GENERIC_MIN
VAL_CLASSREFEXAMPLE_ATTREXAMPLE_MAX = VAL_GENERIC_MAX


# DEBUG FOR TERMINAL ONLY - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Unlike those debug-tags from 'lang.py' file, these ones accept colors to be displayed on terminal.
COLOR_G = "\033[1;32m"  # green
COLOR_Y = "\033[1;33m"  # yellow
COLOR_R = "\033[1;31m"  # red
COLOR_OFF = "\033[m"
TAG_D = f"{COLOR_G}SUBAPPNAME DEBUG >{COLOR_OFF}"
TAG_W = f"{COLOR_Y}SUBAPPNAME WARNING >{COLOR_OFF}"
TAG_E = f"{COLOR_R}SUBAPPNAME ERROR >{COLOR_OFF}"
