# To avoid circular-import with lang.py, translatable constants must stay here!
# from django.utils.translation import gettext_lazy as _


# PATHS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#PATH_API_GLOBAL = "api/global"  # It's also declared in /frontend/src/stores/global.js
#PATH_API_PAGES = "api/pages"  # It's also declared in /frontend/src/stores/pages.js
#PATH_JSON_CATS = "c"  # It's also declared in /frontend/src/router/router.js
#PATH_IMG = "pagex/images/"
#PATH_FILE = "pagex/to_download/"

# DATA FOR DATABASE (WARNING!) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# If values are changed without maintenance on database, multiple errors will raise up!
#VAL_FRONT_TOOL_DJANGO = "django"
#VAL_FRONT_TOOL_VUE = "vue"
#CHOICES_FRONTEND = (
    #(VAL_FRONT_TOOL_DJANGO, "Django Templates (default)"),
    #(VAL_FRONT_TOOL_VUE, "Vue.js 3"),
    # (VAL_FRONT_TOOL_REACT, 'React Native'),
    # (VAL_FRONT_TOOL_ANGULAR, 'Angular.js'),
#)

# OTHERS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# REL_ for 'related_name' on models!
# VAL_ for constant values!
#VAL_BRAND_MIN = 1
#VAL_BRAND_MAX = 20
#VAL_BRAND_LONG_MAX = 3 * VAL_BRAND_MAX

# DEBUG FOR TERMINAL ONLY - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Unlike those debug-tags from 'lang.py' file, these ones accept colors to be displayed on terminal.
COLOR_G = "\033[1;32m"  # green
COLOR_Y = "\033[1;33m"  # yellow
COLOR_R = "\033[1;31m"  # red
COLOR_OFF = "\033[m"
TAG_D = f"{COLOR_G}SUBAPPNAME DEBUG >{COLOR_OFF}"
TAG_W = f"{COLOR_Y}SUBAPPNAME WARNING >{COLOR_OFF}"
TAG_E = f"{COLOR_R}SUBAPPNAME ERROR >{COLOR_OFF}"
