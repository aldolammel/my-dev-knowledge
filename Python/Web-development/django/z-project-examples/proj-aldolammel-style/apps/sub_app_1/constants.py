# To avoid circular-import with language.py, translatable constants must stay here!
# from django.utils.translation import gettext_lazy as _

# PATHS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PATH_API_XXXXX = "api/xxxxxx"
PATH_IMG = "xxxxx/images/"

# DATA FOR DATABASE (WARNING!): - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# If values are changed without maintenance on database, multiple errors will raise up!
VAL_AAAAAA = "aaaa"
VAL_BBBBBB = "bbbbbbb"
VAL_XXX_DEFAULT = VAL_AAAAAA
CHOICES_XXXXXX = (
    (VAL_AAAAAA, "Options Blabla (default)"),
    (VAL_BBBBBB, "Options X"),
)
CHOICES_XXXXX_TYPE = [
    ("valueA", "AA AAA AAA"),
    ("valueB", "BB BBBB BB"),
    ("valueC", "CCCCC CC"),
]

# OTHERS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# REL_ for 'related_name' on models!
# VAL_ for constant values!
VAL_FRONT_TOOL_CACHE = 3600  # 3600 = 1h cache!
VAL_TITLE_MIN = 3
VAL_TITLE_MAX = 35
VAL_SEO_TITLE_MIN = VAL_TITLE_MIN
VAL_SEO_TITLE_MAX = 60  # Google recommends 60 characters!
VAL_SEO_DESC_MIN = 30
VAL_SEO_DESC_MAX = 160  # Google recommends 160 characters!
VAL_CAT_MIN = VAL_TITLE_MIN
VAL_CAT_MAX = VAL_TITLE_MAX
VAL_KEYWORD_MIN = VAL_CAT_MIN
VAL_KEYWORD_MAX = VAL_CAT_MAX
VAL_MENU_MIN = VAL_CAT_MIN
VAL_MENU_MAX = VAL_CAT_MAX
VAL_FRONT_TITLE_MAX = 10
VAL_LINK_TYPE_MAX = 20

# DEBUG: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
COLOR_STARTS_GREEN = "\033[1;32m"
COLOR_STARTS_YELLOW = "\033[1;33m"
COLOR_STARTS_RED = "\033[1;31m"
COLOR_ENDS = "\033[m"
TAG_D = f"{COLOR_STARTS_GREEN}APPNAME DEBUG >{COLOR_ENDS}"
TAG_W = f"{COLOR_STARTS_YELLOW}APPNAME WARNING >{COLOR_ENDS}"
TAG_E = f"{COLOR_STARTS_RED}APPNAME ERROR >{COLOR_ENDS}"
