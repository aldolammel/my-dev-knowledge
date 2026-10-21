# To avoid circular-import with lang.py, translatable constants must stay here!
# from django.utils.translation import gettext_lazy as _


# PATHS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#PATH_API_SOMETGHING = "api/something"  # It's also declared in /frontend/src/stores/global.js
#PATH_JSON_CATS = "c"  # It's also declared in /frontend/src/router/router.js
#PATH_IMG = "something/images/"
#PATH_FILE = "something/to_download/"

# LABELS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# STR_ for string.
STR_SOMETHING_A = "Aldo Lammel"
STR_SOMETHING_B = "Bob Dilan"
STR_SOMETHING_C = "Charlie Brown"

# DATA FOR DATABASE (WARNING!) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# If values are changed without maintenance on database, multiple errors will raise up!
# DIC_ for dictionary.
# INT_ for integer.
# LST_ for list.
# STR_ for string.
# TPL_ for tuple.
#INT_SOMETHING_A = 1
#INT_SOMETHING_B = 2
#INT_SOMETHING_C = 3
#INT_SOMETHING_DEF = INT_SOMETHING_A  # default
#CHOICES_CLASSREFEXAMPLE = (
    #(INT_SOMETHING_A, f'{STR_SOMETHING_A} (default)'),
    #(INT_SOMETHING_B, STR_SOMETHING_B),
    #(INT_SOMETHING_C, STR_SOMETHING_C),
#)

# OTHERS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DIC_ for constant dictionary.
# INT_ for constant integer.
# LST_ for constant list.
# REL_ for 'related_name' on models.
# STR_ for constant string.
# TPL_ for constant tuple.
INT_GENERIC_MIN = 3
INT_GENERIC_MAX = 40
INT_GENERIC_DESC_MIN = 20
INT_GENERIC_DESC_MAX = 140
INT_SLUG_ADD_LIMIT = 5
INT_CLASSREFEXAMPLE_ATTREXAMPLE_MIN = INT_GENERIC_MIN
INT_CLASSREFEXAMPLE_ATTREXAMPLE_MAX = INT_GENERIC_MAX


# DEBUG FOR TERMINAL ONLY - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Unlike those debug-tags from 'lang.py' file, these ones accept colors to be displayed on terminal.
COLOR_G = "\033[1;32m"  # green
COLOR_Y = "\033[1;33m"  # yellow
COLOR_R = "\033[1;31m"  # red
COLOR_OFF = "\033[m"
TAG_D = f"{COLOR_G}SUBAPPNAME DEBUG >{COLOR_OFF}"
TAG_W = f"{COLOR_Y}SUBAPPNAME WARNING >{COLOR_OFF}"
TAG_E = f"{COLOR_R}SUBAPPNAME ERROR >{COLOR_OFF}"
