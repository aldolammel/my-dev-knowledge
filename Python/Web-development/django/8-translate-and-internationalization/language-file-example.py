from django.utils.translation import gettext_lazy as _

# Reminder: gettext_lazy doesn't work with dynamic compositions _(str) % {dict}, so don't in here!

# SECTION NAMES & NAV GROUPERS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''Summary:
    _NAME = Official section name callable in the content;
    _TTL = Exclusive text for page title;
    _NAV = Exclusive text for navegation;
    _DT = Detail page;    
'''
# General Sections (S_G_):
S_G_HOME_1_NAME = _('Personal')
S_G_HOME_1_TTL = _('For You')
S_G_HOME_1_NAV = _('For you')

S_G_HOME_2_NAME = _('Business')
S_G_HOME_2_TTL = _('For Business')
S_G_HOME_2_NAV = _('For business')

S_G_REG_NAME = _('Create Account')
S_G_REG_TTL = _('Create Account')
S_G_REG_NAV = _('Sign up')

S_G_LOGIN_NAME = _('Log In')
S_G_LOGIN_TTL = _('Secure Access')
S_G_LOGIN_NAV = _('Log in')

S_G_LOGIN_RESET_NAME = _('Reset Password')
S_G_LOGIN_RESET_TTL = _('Resetting Password')
S_G_LOGIN_RESET_NAV = _('Reset password')

S_G_LOGIN_RESET_COMPLETE_TTL = _('Password Updated')

S_G_ABOUT_NAME = _('About')
S_G_ABOUT_TTL = _('About Cefalog')
S_G_ABOUT_NAV = _('About')

S_G_HELP_NAME = _('Help Center')
S_G_HELP_TTL = _('Let Us Help You')
S_G_HELP_NAV = _('Help center')

S_G_PRIVACY_NAME = _('Privacy Policy')
S_G_PRIVACY_TTL = _('Our Privacy Policy')
S_G_PRIVACY_NAV = _('Privacy policy')

# Logged-In Sections (S_I_):
S_I_HOME_1_NAME = _('Dashboard')
S_I_HOME_1_TTL = _('Dashboard')
S_I_HOME_1_NAV = _('My dash')

S_I_ATTK_LIST_NAME = _('Attack Notes')
S_I_ATTK_LIST_TTL = _('Attack Notes')
S_I_ATTK_LIST_NAV = _('Attacks')

S_I_ATTK_NOTE_NAME = _('Attack Note')
S_I_ATTK_NOTE_TTL = _('Attack Note')
S_I_ATTK_NOTE_NAV = _('New attack')

S_I_HOME_2_NAME = _('Management')
S_I_HOME_2_TTL = _('Management')
S_I_HOME_2_NAV = _('My management')

S_I_PROFILE_NAME = _('Profile')
S_I_PROFILE_TTL = _('Profile')
S_I_PROFILE_NAV = _('My profile')

S_I_PROFILE_PWD_NAME = _('Change Password')
S_I_PROFILE_PWD_TTL = _('Changing Password')
S_I_PROFILE_PWD_NAV = _('Change password')

S_I_ATTK_NAME = _('Attack Notes')
S_I_ATTK_TTL = _('Attack Notes')
S_I_ATTK_NAV = _('Attack notes')
S_I_ATTK_DT_NAME = _('Attack Note')
S_I_ATTK_DT_TTL = _('Attack Note')
S_I_ATTK_DT_NAV = _('Attack note')

# Nav Groupers (NAV_GPR_):
NAV_GPR_NOTES_NAV = _('My notes')
NAV_GPR_NOTE_NAV = _('Take note')

# LABELS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LB_CREATED_AT = _('Created at')
LB_CREATED_BY = _('Created by')
LB_UPDATED_AT = _('Updated at')
LB_UPDATED_BY = _('Updated by')
LB_STATUS_CONTENT = _('Status')
LB_NAME = _('Name')
LB_DESCRIPT = _('Description')
LB_ICON = _('Icon')
LB_SCALE_NUM = _('Scale Number')
LB_COLOR_CSS = _('Color CSS Classname')
LB_IMG = _('Image')
LB_AREA = _('Area Name')
LB_DRUG = _('Drug Name')
LB_DRUG_DOSE = _('Dose')
LB_DRUG_UNIT = _('Unit')
LB_DRUG_FULL_NAME = _('Full Name')
LB_DRUG_TYPE = _('Medicine Type')
LB_METHOD = _('Method Name')
LB_SYMPTOM = _('Symptom Name')
LB_SENSE = _('Sense Name')
LB_ACTIVITY = _('Activity Name')
LB_PLACE = _('Place Name')
LB_TRIGGER = _('Trigger Name')
LB_ISO_CODE = _('ISO Code')
LB_ABBREV = _('Abbreviation')
LB_PHONE_COUNTRY_CODE = _('Country Code')
LB_PHONE_REGION_CODE = _('Region Code')
LB_PHONE_NUMBER = _('Phone Number')
LB_PHONE_OWNER = _('Owner')
LB_GOAL = _('Goal')
LB_LANG_INTERFACE = _('Interface Language')
LB_PROFILE_TYPE = _('Profile Type')
LB_PROFILE_PWD_1 = _('Password')
LB_PROFILE_PWD_2 = _('Password Confirmation')
LB_USER = _('Username')
LB_USER_PROFILE_LINK = _("You're logged in as")
LB_USER_PROFILE_TYPE = _('My Goal')
LB_USER_EMAIL = _('E-mail')
LB_USER_NOTIF_BY_EMAIL = _('Is Notified by E-mail')
LB_USER_AGE_MIN = _("I'm 13 years old or older")  # TODO
LB_USER_PRIVACY = _("I agree with the Privacy Policy")  # TODO
LB_USER_LANG = _('My Language')
LB_USER_PWD_LAST_UPDATE = _("Password's Last Update")
LB_USER_PWD_OLD = _('Old Password')
LB_USER_PWD_NEW = _('New Password')
LB_USER_PWD_NEW_CONF = _('New Password Confirmation')
LB_PROFILES_USER = _('User')
LB_PROFILES_NOTIF_BY_PHONE = _('Is Notified by Phone')
LB_PROFILE_1_FNAME = _('Name')
# LB_PROFILE_1_LNAME = _('Last Name')  # It's not used anymore!
LB_PROFILE_1_SEX = _('Biological Sex')
LB_PROFILE_1_BIRTHDATE = _('Birthdate')
LB_PROFILE_1_BIRTH_YEAR = _('Birth Year')
LB_PROFILE_1_COUNTRY = _('Country I Live')
LB_PROFILE_1_CITY = _('City Where Is My Home')
LB_PROFILE_1_NOMAD = _('I Am An International Nomad')
LB_PROFILE_1_GOAL_PRI = _('Personal Goal, Primary')
LB_PROFILE_1_GOAL_SEC = _('Personal Goal, Secondary')
LB_PROFILE_2_FNAME = _('Focalpoint, First Name')
LB_PROFILE_2_LNAME = _('Focalpoint, Last Name')
LB_PROFILE_2_BNAME = _('Business Name')
LB_PROFILE_2_LEGAL = _('Legal Business Name')
LB_PROFILE_2_DESC = _('Business Description')
LB_PROFILE_2_EMAIL = _('Business E-mail')
LB_PROFILE_2_COUNTRY = _('Country Of My Business')
LB_PROFILE_2_CITY = _('City Of My Business')
LB_PROFILE_2_URL = _('Business Website')
LB_PROFILE_2_URL_SOCIAL = _('Business Social Media')
LB_PROFILE_2_GOAL_PRI = _('Business Goal, Primary')
LB_PROFILE_2_GOAL_SEC = _('Business Goal, Secondary')
LB_ATTK_CLINIC_VAL = _('Clinical Value')
LB_ATTK_START_D = _('Start Date')
LB_ATTK_START_T = _('Start Time')
LB_ATTK_START_DT = _('Start')
LB_ATTK_START_Y = _('Year')
LB_ATTK_WAS_SLEEP = _('It Was During Sleep')
LB_ATTK_IS_GO = _("It's Ongoing")
LB_ATTK_END_D = _('End Date')
LB_ATTK_END_T = _('End Time')
LB_ATTK_END_DT = _('End')
LB_ATTK_DURATION = _('Length')
# LB_ATTK_WHEN is the LB_ATTK_START_DT
LB_ATTK_WHEN_FORM = _('When')
LB_ATTK_TYPE = _('Attack Type')
LB_ATTK_TYPE_FORM = _('Attack Type')
LB_ATTK_INTENS = _('Intensity')
LB_ATTK_INTENS_FORM = _('Pain Intensity')
LB_ATTK_AREA = _('Affected Areas')
LB_ATTK_AREA_FORM = _('Affected Areas')
LB_ATTK_MEDICINE = _('Medicines')
LB_ATTK_MEDICINE_FORM = _('Medicines')
LB_ATTK_RELIEF = _('Relief Methods')
LB_ATTK_RELIEF_FORM = _('Relief Methods')
LB_ATTK_SYMPTON = _('Symptoms')
LB_ATTK_SYMPTON_FORM = _('Symptoms')
LB_ATTK_SENSE = _('Sense Them')
LB_ATTK_SENSE_FORM = _('Sense Them')
LB_ATTK_ACTIVITY = _('Affected Activities')
LB_ATTK_ACTIVITY_FORM = _('Affected Activities')
LB_ATTK_PLACE = _('I Was')
LB_ATTK_PLACE_FORM = _('I Was')
LB_ATTK_TRIGGER = _('Possible Triggers')
LB_ATTK_TRIGGER_FORM = _('Possible Triggers')
LB_ATTK_NOTE = _('Additional Note')
LB_ATTK_NOTE_FORM = _('Additional Note')

# FORM BUTTONS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BT_REG_SUBMIT = _('Create my account')
BT_REG_NEW_ACCOUNT = _('Create a new account')
BT_PROFILE_LOGOUT = _('Log out')
BT_PROFILE_DEL = _('Close account')
BT_PROFILE_SUBMIT = _('Save changes')
BT_PROFILE_PWD_CHANGE = _('Change password')
BT_PROFILE_PWD_SUBMIT = BT_PROFILE_PWD_CHANGE
BT_LOGIN = _('Log in')
BT_LOGIN_HAVE_ACCOUNT = _('I have an account')
BT_LOGIN_RESET = _('Reset password')
BT_LOGIN_RESET_SUBMIT = _('Send confirmation e-mail')
BT_STEP_BACK = _('Previous step')
BT_STEP_NEXT = _('Next step')
BT_DRAFT = _('Save to finish later')
BT_DISCARD = _('Discard all')
BT_CANCEL = _('Cancel')
BT_BACK = _('Back')
BT_DONE = _('Done')

# FORM FEEDBACKS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_FDBK_ATTK_SUCC = _('Attack note successfully updated!')
TX_FDBK_ATTK_FAIL = _('Oops. Something wrong with your attack note data...')
TX_FDBK_ATTK_DEL = _('Your attack note has been deleted.')
TX_FDBK_LOGIN_RESET = _(
    'If an account exists with the provided e-mail, a password reset link will be sent. Please check your inbox.'
)
TX_FDBK_PROFILE_SUCC_UPDATED = _('Profile was updated successfully!')
TX_FDBK_PROFILE_PWD_UPDATED = _('Your password was changed successfully.')
TX_FDBK_PROFILE_PWD_EQUAL_OLD = _("You tried to use the old password as the new one.")
TX_FDBK_PROFILE_FAIL = _("Oops. Something wrong with your profile data...")
TX_FDBK_PROFILE_1_DEL = _(
    "Done! Your account is now blocked and it'll be completely and automatically deleted within 30 days. Thanks for being with us."
)  # TODO
# TX_FDBK_PROFILE_2_DEL = _("")

# FORM ERRORS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_ERRO_USER_PROFILE_BLNK = _('This field is required.')  # TODO
TX_ERRO_USER_EMAIL_BLNK = _('This field is required.')  # TODO
TX_ERRO_USER_EMAIL_INVLD = _('Enter a valid e-mail address.')
TX_ERRO_USER_AGE_MIN = _('To use our services, you must be 13 years or older.')  # TODO
TX_ERRO_USER_PRIVACY = _(
    'To use our services, you must read and accept our Privacy Policy.'
)  # TODO
TX_ERRO_PROFILES_GOAL_P_NONE = _('Please, at first select a primary goal.')
TX_ERRO_PROFILES_GOAL_SAME = _("Your primary and secondary goals shouldn't be the same.")
TX_ERRO_PROFILE_1_FNAME_MAXLNGH = _('This field cannot exceed %(val)s characters.')  # TODO
TX_ERRO_PROFILE_1_LNAME_MAXLNGH = _('This field cannot exceed %(val)s characters.')  # TODO
TX_ERRO_PROFILE_1_BIRTH_MIN = _(
    'To protect children and prevent their exposure, the minimum age for using our service is 13 years old.'
)  # TODO
TX_ERRO_PROFILE_1_BIRTH_MAX = _('Check the birth year!')
TX_ERRO_PROFILE_1_BIRTH_INVLD = _('Invalid date for birthdate.')
TX_ERRO_PROFILE_1_SEX_BLNK = _('This field is required.')  # TODO
TX_ERRO_PROFILE_1_COUNTRY_BLNK = _('This field is required.')  # TODO
TX_ERRO_PROFILE_2_BNAME_BLNK = _('This field is required.')  # TODO
TX_ERRO_PROFILE_2_BNAME_MAXLNGH = _('This field cannot exceed %(val)s characters.')  # TODO
TX_ERRO_PROFILE_2_LEGAL_BLNK = _('This field is required.')  # TODO
TX_ERRO_PROFILE_2_LEGAL_UNIQ = _(
    "This legal name already exists. It doesn't look good, so please, contact us!"
)
TX_ERRO_PROFILE_2_LEGAL_MAXLNGH = _('This field cannot exceed %(val)s characters.')  # TODO
TX_ERRO_PROFILE_2_CITY_BLNK = _('This field is required.')  # TODO
TX_ERRO_PROFILE_2_CITY_MAXLNGH = _('This field cannot exceed %(val)s characters.')  # TODO
TX_ERRO_PROFILE_2_DESC_BLNK = _('This field is required.')  # TODO
TX_ERRO_PROFILE_2_DESC_MAXLNGH = _('This field cannot exceed %(val)s characters.')  # TODO
TX_ERRO_PROFILE_2_EMAIL_BLNK = _('This field is required.')
TX_ERRO_PROFILE_2_EMAIL_INVLD = TX_ERRO_USER_EMAIL_INVLD


TX_ERRO_ATTK_START_D_BLNK = _('This field is required.')
TX_ERRO_ATTK_START_D_LATE = _("It doesn't make sense for the start date to be after the end date.")
TX_ERRO_ATTK_START_D_INVLD = _(
    'Enter a valid Start Date: mm/dd/yyyy.'
)  # TODO this solution isnt good enough!
TX_ERRO_ATTK_START_D_BACK = _(
    'The limit for retroactive attack note is 180 days from the current date.'
)  # TODO
TX_ERRO_ATTK_START_D_DUPLICAT_A = _(
    "There's another note (which seems still ongoing) in the same period you're trying to record now. You can check that note here."
)
TX_ERRO_ATTK_START_D_DUPLICAT_B = _(
    "You're trying to make a note about another one that covers the same period. You can check that note here."
)
TX_ERRO_ATTK_START_T_BLNK = _('This field is required.')  # TODO
TX_ERRO_ATTK_START_T_INVLD = _(
    'Enter a valid Start Time: hour:minute.'  # TODO
)  # TODO this solution isnt good enough!
TX_ERRO_ATTK_START_DT_FUTURE = _('The start date and time cannot be in the future.')
TX_ERRO_ATTK_ONGO_OLD = _("The note date is not current to still be ongoing.")
TX_ERRO_ATTK_ONGO_NOT_RECENT = _(
    'If the attack is ongoing, it must be your most recent note. Check the attack start time.'
)
TX_ERRO_ATTK_END_NEEDED = _(
    "The end of the attack (date and time) must be provided completely if it's no longer ongoing."
)
TX_ERRO_ATTK_END_INCOMP = _(
    'If the attack is not ongoing anymore, the End Date and End Time are needed.'
)  # TODO
TX_ERRO_ATTK_END_FUTURE = _('You cannot set the attack end for the future.')
TX_ERRO_ATTK_END_T_MIN = _('The end time must be at least 15 minutes after the start time.')  # TODO
TX_ERRO_ATTK_END_D_MAX = _(
    'The attack end cannot have lasted more than 3 days after the attack start.'  # TODO
)
TX_ERRO_ATTK_END_FORBBIDEN = _('You cannot set an attack end if the attack still going.')
TX_ERRO_ATTK_END_D_INVLD = _(
    'Enter a valid End Date: mm/dd/yyyy.'
)  # TODO this solution isnt good enough!
TX_ERRO_ATTK_END_D_NULL = _(
    'End Date cannot be empty if the attack is not ongoing.'
)  # TODO null or blank? Check it and change the var name if needed.
TX_ERRO_ATTK_END_T_INVLD = _(
    'Enter a valid End Time: hour:minute.'
)  # TODO this solution isnt good enough!
TX_ERRO_ATTK_END_T_NULL = _(
    'End Time cannot be empty if the attack is not ongoing.'
)  # TODO null or blank? Check it and change the var name if needed.
TX_ERRO_ATTK_INTENS_BLNK = _('This field is required.')  # TODO
TX_ERRO_ATTK_NOTE_MAXLNGH = _('This field cannot exceed %(val)s characters.')  # TODO

# REGULAR TEXTS WITH OR WITHOUT HYPERLINK: - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_PROFILE_1 = _('Personal')
TX_PROFILE_1_CTA = _('To understand my headaches')
TX_PROFILE_2 = _('Business')
TX_PROFILE_2_CTA = _('To represent a business')

# GENERIC COMPOSITION TEXTS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_FROM = _('from')
TX_BY = _('by')

# TO SPECIAL USAGE TEXTS:
TX_PRIVACY_ALERT = _(
    # Caution: this is used as remider/suffix in other texts. Keep it up-to-date!
    'Your personal data such as full name, e-mail and/or phone number are never shared.'
)

# FORM HELPERS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_HELP_USER_PROFILE = _(
    "Define which profile type you'll use on the platform (Personal profile is highly recommended)."
)
TX_HELP_USER_EMAIL = _('We do NOT share your e-mail under any circumstances.')
TX_HELP_USER_NOTIF_EMAIL = _(
    'Whether you should receive important (non-ad) notifications from your account via e-mail.'
)
TX_HELP_USER_LANG = _('Your favorite language for the Cefalog interface.')  # TODO
TX_HELP_USER_AGE_MIN = TX_ERRO_USER_AGE_MIN
TX_HELP_USER_PRIVACY = TX_ERRO_USER_PRIVACY
# TX_HELP_PROFILE_PWD1 =   # Using the Django solution for this!
TX_HELP_PROFILE_PWD2 = _('Enter the same password as before, for verification.')
TX_HELP_PROFILE_1_NAME = _('A name or nickname that you like.')
TX_HELP_PROFILE_1_BIRTHDATE = _(
    'Your age is valuable to better understand the behavior of headaches over the years.'
)
TX_HELP_PROFILE_1_SEX = _(
    "For clinical and Cefalog understanding is crucial to get to know which is your birth sex."
)  # TODO
TX_HELP_PROFILE_1_COUNTRY = _('Country where you live.')
TX_HELP_PROFILE_1_NOMAD = _(
    "If you're moving countries very often, use this for some settings are adapted to your reality."
)
TX_HELP_PROFILE_1_CITY = _('City where is your home.')
TX_HELP_PROFILE_1_GOAL_PRI = _(
    'Please indicate the goal that best fits your top priority when using our free service.'
)
TX_HELP_PROFILE_1_GOAL_SEC = _('If so, define what your secondary goal with us would be.')
TX_HELP_PROFILE_2_BNAME = _('Comercial name of your business.')
TX_HELP_PROFILE_2_LEGAL = _('Legal name of your business.')
TX_HELP_PROFILE_2_DESC = _(
    'Describe your business in an objective and attractive way for our audience.'
)
TX_HELP_CREATED_BY = _('User who created this record.')
TX_HELP_UPDATED_BY = _('User who made the most recent update to this record.')
TX_HELP_STATUS_CONTENT = _('Whether or not this content should be visible to users.')
TX_HELP_ATTK_CLINIC_VAL = _(
    "Current scientific value of this note. The value changes according to the amount of data entered. The more information added, the greater the value for your doctor and our partner research centers."
)
TX_HELP_ATTK_START_D = _('The date when the attack started.')
TX_HELP_ATTK_START_T = _('The time when the attack started.')
TX_HELP_ATTK_WAS_SLEEP = _('Check if the attack got started during sleep.')
TX_HELP_ATTK_IS_GO = _('Check if the attack still going on.')
TX_HELP_ATTK_END_D = _('The date when the attack finished.')
TX_HELP_ATTK_END_T = _('The time when the attack finished.')
TX_HELP_ATTK_DURATION = _('How long the attack was felt.')
TX_HELP_ATTK_TYPE = _('Type of attack you believe this note is treating.')
TX_HELP_ATTK_INTENS = _('Highest peak of pain the attack reached.')
TX_HELP_ATTK_AREA = _('Area(s) of the body where the attack occurred.')
TX_HELP_ATTK_MEDICINE = _('Medicine(s) used to treat the attack.')
TX_HELP_ATTK_RELIEF = _('Relief method(s) used to ease the attack.')
TX_HELP_ATTK_SYMPTOM = _('Symptom(s) noticed in the attack.')
TX_HELP_ATTK_SENSE = _('What made you realize the attack was coming.')
TX_HELP_ATTK_ACTIVITY = _('Activity or activities affected by the attack.')
TX_HELP_ATTK_PLACE = _('Where you were when the attack began.')
TX_HELP_ATTK_TRIGGER = _('Trigger(s) you believe contributed to the attack.')
TX_HELP_ATTK_NOTE = _('In case you want to add more details of this attack.')
TX_HELP_PAIN_INTENS = _('Name of the pain intensity.')
TX_HELP_DRUG_TYPE = _('Pharmaceutical form of a medicine.')
TX_HELP_DRUG_NAME = _('The active-ingredient or commercial-name of the medicine.')
TX_HELP_DRUG_DOSE = _('Amount of medicine per dose.')
TX_HELP_DRUG_DOSE_UNIT = _('Unit of dose measurement.')
TX_HELP_AREA_NAME = _('Spot on the body where there could be pain or relevant sensations.')
TX_HELP_RELIEF_NAME = _('Name of what helped to alleviate the attack.')
TX_HELP_SYMPTOM_NAME = _('Name the symptom that may be related to headaches.')
TX_HELP_SENSE_NAME = _('Descriptive name for the sensation felt.')
TX_HELP_ACTIVITY_NAME = _('That activity that was affected due to the attack.')
TX_HELP_PLACE_NAME = _('The name of a relevant place type where an attack could begin.')
TX_HELP_TRIGGER_NAME = _('Name for that which may be responsible for triggering an attack.')
TX_HELP_PROFILE_2_COUNTRY = _('Country where the business is physically.')
TX_HELP_PROFILE_2_CITY = _('City where the business is physically.')

# E-MAIL SUBJECTS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#SUBJ_RESET_PWD = _("Cefalog password reset")

# CMS ONLY: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CMS_MORE_DETAILS = _('More details')
CMS_ERRO_PROFILE = _('ERROR: NO PROFILE!')
