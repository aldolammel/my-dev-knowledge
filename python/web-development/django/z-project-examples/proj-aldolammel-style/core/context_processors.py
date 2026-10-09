from django.conf import settings
# from . import consts, lang
from . import consts

# If you want to use {{ MEDIA_URL }} in your templates, add 'django.template.context_processors.media' in the 'context_processors' option of TEMPLATES.

def data_to_cms_template_only(request):
    """Information about the app just for CMS, a layer that Pagex doesn't serve yet. For front-end, Pagex got this data through its PagexSettings model."""
    context = {
        "BRAND_NAME": consts.BRAND_NAME,
        "BRAND_EMAIL": consts.BRAND_EMAIL,
        "BRAND_URL": consts.BRAND_URL,
        "DEV_NAME": consts.DEV_NAME,
        "DEV_URL": consts.DEV_URL,
        "ADMIN_EMAIL": consts.ADMIN_EMAIL,
        # "CURRENT_YEAR": timezone.now().year,
    }
    return context