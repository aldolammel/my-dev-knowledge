from django.conf import settings as stgs
from django.utils import timezone

from . import consts
# from . import lang


# If you want to use {{ MEDIA_URL }} in your templates, add 'django.template.context_processors.media' in the 'context_processors' option of TEMPLATES.


def app_info(request):
    """Information about the app."""
    context = {
        "BRAND_NAME": consts.BRAND_NAME,
        "BRAND_EMAIL": consts.BRAND_EMAIL,
        "BRAND_URL": consts.BRAND_URL,
        "DEV_NAME": consts.DEV_NAME,
        "DEV_URL": consts.DEV_URL,
        "ADMIN_EMAIL": consts.ADMIN_EMAIL,
        "CURRENT_YEAR": timezone.now().year,
    }
    return context


def languages(request):
    """Add LANGUAGES and current LANGUAGE_CODE to the context globally."""
    return {
        "LANGUAGES": stgs.LANGUAGES,  # Available ones!
        "LANGUAGE_CODE": request.LANGUAGE_CODE,  # Currently active one!
    }


def constants_to_template(request):
    """Crucial constant variables to be available to templates."""
    return {
        # "S_G_HOME_1_NAV": lang.S_G_HOME_1_NAV,
        # "S_G_HOME_2_NAV": lang.S_G_HOME_2_NAV,
        # "S_G_REG_NAV": lang.S_G_REG_NAV,
        # "S_G_LOGIN_NAV": lang.S_G_LOGIN_NAV,
        # "S_G_HELP_NAV": lang.S_G_HELP_NAV,
        # "S_G_ABOUT_NAV": lang.S_G_ABOUT_NAV,
        # "S_G_PRIVACY_NAV": lang.S_G_PRIVACY_NAV,
        # "LB_USER_PROFILE_LINK": lang.LB_USER_PROFILE_LINK,
        # "NAV_GPR_NOTES_NAV": lang.NAV_GPR_NOTES_NAV,
        # "NAV_GPR_NOTE_NAV": lang.NAV_GPR_NOTE_NAV,
        # "S_I_ATTK_NOTE_NAV": lang.S_I_ATTK_NOTE_NAV,
        # "S_I_ATTK_LIST_NAV": lang.S_I_ATTK_LIST_NAV,
        # "S_I_HOME_1_NAV": lang.S_I_HOME_1_NAV,
        # "S_I_HOME_2_NAV": lang.S_I_HOME_2_NAV,
        # "S_I_ATTK_NAV": lang.S_I_ATTK_NAV,
        # "S_I_ATTK_DT_NAV": lang.S_I_ATTK_DT_NAV,
        # "BT_PROFILE_LOGOUT": lang.BT_PROFILE_LOGOUT,
    }
