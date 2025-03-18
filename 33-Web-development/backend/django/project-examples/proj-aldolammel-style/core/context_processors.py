from django.conf import settings as stg
from django.utils import timezone
from core.constants import (
    BRAND_NAME,
    BRAND_EMAIL,
    BRAND_URL,
    DEV_NAME,
    DEV_URL,
    ADMIN_EMAIL,
)
from core import language as lng


def app_info(request):
    """Information about the app."""
    return {
        "BRAND_NAME": BRAND_NAME,
        "BRAND_EMAIL": BRAND_EMAIL,
        "BRAND_URL": BRAND_URL,
        "DEV_NAME": DEV_NAME,
        "DEV_URL": DEV_URL,
        "ADMIN_EMAIL": ADMIN_EMAIL,
        "CURRENT_YEAR": timezone.now().year,
    }


def languages(request):
    """Add LANGUAGES and current LANGUAGE_CODE to the context globally."""
    return {
        "LANGUAGES": stg.LANGUAGES,  # Available ones!
        "LANGUAGE_CODE": request.LANGUAGE_CODE,  # Currently active one!
    }


def constants_to_template(request):
    """Crucial constant variables to be available to templates."""
    return {
        # "S_G_HOME_1_NAV": lng.S_G_HOME_1_NAV,
        # "S_G_HOME_2_NAV": lng.S_G_HOME_2_NAV,
        # "S_G_REG_NAV": lng.S_G_REG_NAV,
        # "S_G_LOGIN_NAV": lng.S_G_LOGIN_NAV,
        # "S_G_HELP_NAV": lng.S_G_HELP_NAV,
        # "S_G_ABOUT_NAV": lng.S_G_ABOUT_NAV,
        # "S_G_PRIVACY_NAV": lng.S_G_PRIVACY_NAV,
        # "LB_USER_PROFILE_LINK": lng.LB_USER_PROFILE_LINK,
        # "NAV_GPR_NOTES_NAV": lng.NAV_GPR_NOTES_NAV,
        # "NAV_GPR_NOTE_NAV": lng.NAV_GPR_NOTE_NAV,
        # "S_I_ATTK_NOTE_NAV": lng.S_I_ATTK_NOTE_NAV,
        # "S_I_ATTK_LIST_NAV": lng.S_I_ATTK_LIST_NAV,
        # "S_I_HOME_1_NAV": lng.S_I_HOME_1_NAV,
        # "S_I_HOME_2_NAV": lng.S_I_HOME_2_NAV,
        # "S_I_ATTK_NAV": lng.S_I_ATTK_NAV,
        # "S_I_ATTK_DT_NAV": lng.S_I_ATTK_DT_NAV,
        # "BT_PROFILE_LOGOUT": lng.BT_PROFILE_LOGOUT,
    }
