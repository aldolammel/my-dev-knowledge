# To avoid circular-import with lang.py, translatable constants must stay here!
# from django.utils.translation import gettext_lazy as _

# PATHS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PATH_API_GLOBAL = "api/global"  # It's also declared in /frontend/src/stores/global.js
PATH_API_PAGES = "api/pages"  # It's also declared in /frontend/src/stores/pages.js
PATH_API_POSTS = "api/posts"  # It's also declared in /frontend/src/stores/posts.js
PATH_API_STRUCTS = "api/structures"  # It's also declared in /frontend/src/stores/structures.js
PATH_API_MENUS = "api/menus"  # It's also declared in /frontend/src/stores/menus.js
PATH_API_CATS = "api/categories"  # It's also declared in /frontend/src/stores/categories.js
PATH_API_TAGS = "api/tags"  # It's also declared in /frontend/src/stores/tags.js
PATH_JSON_CATS = "c"  # It's also declared in /frontend/src/router/router.js
PATH_JSON_TAGS = "t"  # It's also declared in /frontend/src/router/router.js
PATH_IMG = "pagex/images/"
PATH_FILE = "pagex/to_download/"

# DATA FOR DATABASE (WARNING!) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# If values are changed without maintenance on database, multiple errors will raise up!
VAL_FRONT_TOOL_DJANGO = "django"
VAL_FRONT_TOOL_VUE = "vue"
# VAL_FRONT_TOOL_REACT = "react"
# VAL_FRONT_TOOL_ANGULAR = "angular"
VAL_FRONT_TOOL_DEFAULT = VAL_FRONT_TOOL_DJANGO
# VAL_ELEM_TYPE_TXT = "0"
# VAL_ELEM_TYPE_IMG = "1"
# VAL_ELEM_TYPE_FILE = "2"
# VAL_ELEM_TYPE_LINK = "3"
CHOICES_FRONTEND = (
    (VAL_FRONT_TOOL_DJANGO, "Django Templates (default)"),
    (VAL_FRONT_TOOL_VUE, "Vue.js 3"),
    # (VAL_FRONT_TOOL_REACT, 'React Native'),
    # (VAL_FRONT_TOOL_ANGULAR, 'Angular.js'),
)
CHOICES_LINK_TYPE = (
    ("page", "Página"),
    ("category", "Categoria"),
    ("redirection", "Redirecionamento"),
    # ("tag", "Tag"),  # Not used for menu links!
)

# OTHERS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# REL_ for 'related_name' on models!
# VAL_ for constant values!
VAL_BRAND_MIN = 1
VAL_BRAND_MAX = 20
VAL_EMAIL_URL_MIN = 6  # x@x.co or http://x.co
VAL_EMAIL_URL_MAX = 60
VAL_FRONT_TOOL_CACHE = 3600  # 3600 = 1h cache!
VAL_SEO_TITLE_MIN = 3
VAL_SEO_TITLE_MAX = 60  # Google recommends up to 60 characters!
VAL_PAGE_TITLE_MIN = VAL_SEO_TITLE_MIN
VAL_PAGE_TITLE_MAX = 35  # Good number to not destroy Menus layouts through big titles.
VAL_POST_TITLE_MIN = VAL_SEO_TITLE_MIN
VAL_POST_TITLE_MAX = VAL_SEO_TITLE_MAX
VAL_POST_CONTENT_MIN = 140
VAL_POST_CONTENT_MAX = 70000
VAL_SEO_DESC_MIN = 30
VAL_SEO_DESC_MAX = 160  # Google recommends up to 160 characters!
VAL_CAT_MIN = VAL_PAGE_TITLE_MIN
VAL_CAT_MAX = VAL_PAGE_TITLE_MAX
VAL_TAG_MIN = VAL_CAT_MIN
VAL_TAG_MAX = VAL_CAT_MAX
VAL_MENU_MIN = VAL_CAT_MIN
VAL_MENU_MAX = VAL_CAT_MAX
VAL_FRONT_TITLE_MAX = 10
VAL_LINK_TYPE_MAX = 20
VAL_SLUG_NAME_MIN = 8
VAL_SLUG_NAME_MAX = 16
VAL_SLUG_ADD_LIMIT = 5  # It considering the additional separator characters.

# DEBUG - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
COLOR_STARTS_GREEN = "\033[1;32m"
COLOR_STARTS_YELLOW = "\033[1;33m"
COLOR_STARTS_RED = "\033[1;31m"
COLOR_ENDS = "\033[m"
TAG_D = f"{COLOR_STARTS_GREEN}PAGEX DEBUG >{COLOR_ENDS}"
TAG_W = f"{COLOR_STARTS_YELLOW}PAGEX WARNING >{COLOR_ENDS}"
TAG_E = f"{COLOR_STARTS_RED}PAGEX ERROR >{COLOR_ENDS}"
