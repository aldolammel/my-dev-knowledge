from django.utils.translation import gettext_lazy as _

# Reminder: gettext_lazy doesn't work with dynamic compositions _(str) % {dict}, so don't in here!

# SECTION NAMES: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# General Sections (S_G_):
S_G_HOME_1_NAME = _('personal')  # NAME = Official section name;
S_G_HOME_1_TTL = _('for you')  # TTL = Text for page title;
S_G_HOME_1_NAV = _('for you')  # NAV = Text for navegation;

S_G_HOME_2_NAME = _('business')
S_G_HOME_2_TTL = _('for business')
S_G_HOME_2_NAV = _('for business')

S_G_REG_NAME = _('create account')
S_G_REG_TTL = _('create free account')
S_G_REG_NAV = _('create account')

S_G_ABOUT_NAME = _('about us')
S_G_ABOUT_TTL = _('about us')
S_G_ABOUT_NAV = _('about')

S_G_HELP_NAME = _('help')
S_G_HELP_TTL = _('let us help you')
S_G_HELP_NAV = _('help')

S_G_PRIVACY_NAME = _('privacy policy')
S_G_PRIVACY_TTL = _('our privacy policy')
S_G_PRIVACY_NAV = _('privacy policy')

# Logged-In Sections (S_I_):
S_I_HOME_1_NAME = _('dashboard')
S_I_HOME_1_TTL = _('dashboard')
S_I_HOME_1_NAV = _('my dash')

S_I_HOME_2_NAME = _('management')
S_I_HOME_2_TTL = _('management')
S_I_HOME_2_NAV = _('my management')

S_I_NEWS_NAME = _('news')
S_I_NEWS_TTL = _('news')
S_I_NEWS_NAV = _('news')
S_I_NEWS_DT_NAME = _('highlight')  # DT = Detail page;
S_I_NEWS_DT_TTL = _('highlight')
S_I_NEWS_DT_NAV = _('highlight')

# LABELS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LB_CREATED_AT = _('Created at')
LB_CREATED_BY = _('Created by')
LB_UPDATED_AT = _('Updated at')
LB_UPDATED_BY = _('Updated by')
LB_STATUS_CONTENT = _('Status')
LB_PHONE_COUNTRY_CODE = _('Country Code')
LB_PHONE_REGION_CODE = _('Region Code')
LB_PHONE_NUMBER = _('Phone Number')
LB_LANG_INTERFACE = _('Interface Language')
LB_USER_PROFILE_TYPE = _('My Goal')
LB_USER_EMAIL = _('E-mail')
LB_USER_NOTIF_BY_EMAIL = _('Is Notified by E-mail')
LB_USER_LANG = _('My Language')
LB_USER_PWD_LAST_UPDATE = _("Password's Last Update")
LB_PROFILES_NOTIF_BY_PHONE = _('Is Notified by Phone')
LB_PROFILE_1_FNAME = _('First Name')
LB_PROFILE_1_LNAME = _('Last Name')
LB_PROFILE_1_SEX = _('Biological Sex')
LB_PROFILE_1_BIRTHDATE = _('Birthdate')
LB_PROFILE_1_BIRTH_YEAR = _('Birth Year')
LB_PROFILE_1_COUNTRY = _('Country I Live')
LB_PROFILE_1_CITY = _('City Where Is My Home')
LB_PROFILE_1_NOMAD = _('I Am An International Nomad')

# FORM BUTTONS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BT_REG_HAVE_ACCOUNT = _('I already have an account')
BT_REG_SUBMIT = _('Create my account')
BT_PROFILE_DEL = _('Delete account')
BT_PROFILE_SUBMIT = _('Update')
BT_STEP_BACK = _('Previous step')
BT_STEP_NEXT = _('Next step')
BT_DRAFT = _('Save to finish later')
BT_DISCARD = _('Discard all')
BT_CANCEL = _('Cancel')
BT_DONE = _('Done')

# FORM FEEDBACKS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_FDBK_XXXX_SUCC = _('Attack note successfully added as a complete note!')
TX_FDBK_XXXX_FAIL = _('Oops. Something wrong with your attack note data...')
TX_FDBK_XXXX_DRAFT = _('Attack note added as a draft!')
TX_FDBK_XXXX_SUCC_NOT_DRAFT = _("Actually your attack note is not a draft! It's complete!")
TX_FDBK_XXXX_DEL = _('Your attack note has been deleted.')
TX_FDBK_PROFILE_SUCC_UPDATED = _('Profile was updated successfully!')
TX_FDBK_PROFILE_FAIL = _("Oops. Something wrong with your profile data...")

# FORM ERRORS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_ERRO_USER_PROFILE_BLNK = _('%(lb)s is required.')
TX_ERRO_USER_EMAIL_BLNK = _('%(lb)s is required.')
TX_ERRO_USER_EMAIL_INVLD = _('Enter a valid e-mail address.')
TX_ERRO_PROFILE_1_FNAME_MAXLNGH = _('%(lb)s cannot exceed %(val)s characters.')
TX_ERRO_PROFILE_1_LNAME_MAXLNGH = _('%(lb)s cannot exceed %(val)s characters.')
TX_ERRO_PROFILE_1_BIRTH_INVLD = _('Invalid date for birthdate.')
TX_ERRO_PROFILE_1_SEX_BLNK = _('%(lb)s is required.')
TX_ERRO_PROFILE_1_COUNTRY_BLNK = _('%(lb)s is required.')

# REGULAR TEXTS WITH OR WITHOUT HYPERLINK: - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_PROFILE_1 = _('Personal')
TX_PROFILE_1_FORM = _('To understand my headaches')

# GENERIC COMPOSITION TEXTS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_FROM = _('from')
TX_BY = _('by')

# FORM HELPERS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_HELP_USER_PROFILE = _(
    "Define which profile type you'll use on the platform (Personal profile is highly recommended)."
)
TX_HELP_USER_SEX = _(
    "For clinical and %(brand)s understanding is crucial to get to know which is your birth sex."
)
TX_HELP_USER_NOTIF_EMAIL = _(
    'Whether you should receive important (non-ad) notifications from your account via e-mail.'
)
TX_HELP_USER_LANG = _('Your favorite language for the %(brand)s interface.')
TX_HELP_PROFILE_1_COUNTRY = _('Country where you live.')
TX_HELP_PROFILE_1_NOMAD = _(
    "If you're moving countries very often, use this for some settings are adapted to your reality."
)
TX_HELP_PROFILE_1_CITY = _('City where is your home.')
TX_HELP_CREATED_BY = _('User who created this record.')
TX_HELP_UPDATED_BY = _('User who made the most recent update to this record.')
TX_HELP_STATUS_CONTENT = _('Whether or not this content should be visible to users.')
TX_HELP_XXXXXXXX_XXXX = _('xxxxxxxxxxxxxxxxxxxxxxx.')
TX_HELP_XXXXXXXX_XXXX = _('xxxxxxxxxxxxxxxxxxxxxxx.')
TX_HELP_XXXXXXXX_XXXX = _('xxxxxxxxxxxxxxxxxxxxxxx.')
TX_HELP_XXXXXXXX_XXXX = _('xxxxxxxxxxxxxxxxxxxxxxx.')

# CMS ONLY: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CMS_MORE_DETAILS = _('More details')
CMS_ERRO_PROFILE = _('ERROR: NO PROFILE!')
