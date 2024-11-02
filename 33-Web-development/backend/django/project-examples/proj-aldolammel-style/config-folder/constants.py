# To avoid circular-import with translation.py, translatable constants must stay here!
from django.utils.translation import gettext_lazy as _


# APP ESSENTIAL INFO: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ADMIN_EMAIL = 'cefalogmaster@gmail.com'
BRAND_NAME = 'Cefalog'
BRAND_DESCRIPT = 'Soon...'  # TODO How do I translate this?
BRAND_EMAIL = 'cefalogmaster@gmail.com'
BRAND_URL = 'https://cefalog.com'
DEV_NAME = 'ABCOO'
DEV_URL = 'https://abcoo.com.br'
BRAND_KEYWORDS = 'Soon...'  # TODO How do I translate this?

# SUB-APP PATTERNNAMES: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Critical: do not use sub-app names as a constant. Django demands it as explicity, unfortunately!
NAMESPACE_1 = 'general'
NAMESPACE_2 = 'in'
NAMESPACE_3 = 'accounts'
NAMESPACE_4 = 'event_attacks'
# Pattern names from NAMESPACE_1:
PATTERN_1_1 = 'home_one_view'
PATTERN_1_2 = 'home_two_view'
PATTERN_1_3 = 'help_view'
PATTERN_1_4 = 'privacy_view'
PATTERN_1_5 = 'about_view'
# Pattern names from NAMESPACE_2:
PATTERN_2_1 = 'home_view'
PATTERN_2_2 = 'home_one_view'
PATTERN_2_3 = 'home_two_view'
# Pattern names from NAMESPACE_3:
PATTERN_3_1 = 'register_view'
PATTERN_3_2 = 'profile_view'
# Pattern names from NAMESPACE_4:
PATTERN_4_1 = 'list_view'
PATTERN_4_2 = 'step_when_view'
PATTERN_4_3 = 'step_type_view'
PATTERN_4_4 = 'step_intensity_view'
PATTERN_4_5 = 'step_areas_view'
PATTERN_4_6 = 'step_medicines_view'
PATTERN_4_7 = 'step_reliefs_view'
PATTERN_4_8 = 'step_symptoms_view'
PATTERN_4_9 = 'step_senses_view'
PATTERN_4_10 = 'step_activities_view'
PATTERN_4_11 = 'step_place_view'
PATTERN_4_12 = 'step_triggers_view'
PATTERN_4_13 = 'step_note_view'

# PATHS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PATH_CMS_USERS = '/admin/auth/user/'
PATH_EVT_ATTK_ICO = 'icons/events/attack/'
PATH_EVT_ATTK_IMG = 'imgs/events/attack/'

# DATA FOR DATABASE (WARNING!): - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# If values are changed without maintenance on database, multiple errors will raise up!
CHOICES_PROFILE_TYPE = (
    ('1', _('Personal')),
    ('2', _('Business')),
)
CHOICES_SEX = (
    ('f', _('Female')),
    ('m', _('Male')),
    ('i', _('Intersex')),
)
CHOICES_STATUS_CONTENT = (
    ('on', _('Active')),
    ('off', _('Archived')),
)
CHOICES_ATTK_CLINIC_VAL = (
    ('0', _('None')),
    ('1', _('Low')),
    ('2', _('Medium')),
    ('3', _('High')),
    ('4', _('Very high')),
)
CHOICES_PHONE_CODE = (
    # FIX: Important to include all phone codes because the phone shouldn't depends user nationality!
    ('244', 'Angola (+244)'),
    ('54', 'Argentina (+54)'),
    ('591', 'Bolivia (+591)'),
)

# OTHERS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
VAL_RETROACTIVE_ADDING_LIMIT = 180  # in days (Retroactive Adding Limit)!
VAL_HEADACHE_LIFE_TIME_MAX = 3  # in days, based in Headache Life Time Maximum.
VAL_HEADACHE_LIFE_TIME_MIN = 15  # in minutes, based in Headache Life Time Minimum.
VAL_EVT_ATTK_NOTE_MAXLNGH = 600
VAL_PROFILE_1_BIRTH_MIN = 13  # in years old. Legal matter in Brazil!
VAL_PROFILE_1_BIRTH_MAX = 85  # in years old. Migraine over than 70 is rare!
VAL_PROFILE_1_NAME_MAXLNGH = 12
VAL_PROFILE_1_DEL_SCHEDULE = 30  # in days!
VAL_PROFILE_2_DEL_SCHEDULE = VAL_PROFILE_1_DEL_SCHEDULE  # in days!
VAL_PROFILE_2_BNAME_MAXLNGH = 50
VAL_PROFILE_2_LEGAL_MAXLNGH = 100
VAL_PROFILE_2_CITY_MAXLNGH = 40
VAL_PROFILE_2_DESC_MAXLNGH = 400
REL_PROFILE_1 = 'profile_1'
REL_PROFILE_2 = 'profile_2'
