# DON'T USE THIS FOR UTILS YOU WANNA USE DIRECTLY IN MODELS.PY. USE UTILS_MODELS.PY INSTEAD!

from django.conf import settings as stgs
from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured

from . import constants as consts
from .models import PagexSettings


def pagex_setup_basic(obj: object):
    """Checks if the Pagex Singleton already has its basic settings.py definitions.
    :Returns: tuple w/ front_base, back_base, and is_urls_relative if success; if fails: None."""
    # Escapes:
    pagex_stgs = PagexSettings.objects.first()
    if pagex_stgs is None:
        raise ImproperlyConfigured(
            f"{consts.TAG_E} Nenhuma configuração PagexSettings foi encontrada. Certifique-se de criar sua configuração PagexSettings antes de qualquer outra ação."
        )
    if not obj:
        raise ImproperlyConfigured(f"{consts.TAG_E} pagex_setup_basic > Erro desconhecido.")
    # Defining URL structure based:
    if not stgs.DEBUG and not stgs.PAGEX_PROD_URL:
        raise ImproperlyConfigured(
            f"{consts.TAG_E} o 'PAGEX_PROD_URL' do projeto ainda não foi definido no settings.py. Caso você ainda não saiba qual será o domínio de produção do produto, defina seu 'DEBUG' como 'True' no settings.py."
        )
    front_base = stgs.PAGEX_PROD_URL
    back_base = stgs.PAGEX_PROD_URL
    # Attention - it's NOT for debug purpose:
    # If debug is true, front-end and back-end can be two servers apart:
    if stgs.DEBUG:
        if not stgs.PAGEX_FRONT_URL or not stgs.PAGEX_BACK_URL:
            raise ImproperlyConfigured(
                f"{consts.TAG_E} como o projeto segue em desenvolvimento (DEBUG = True), certifique-se que você tem seus 'PAGEX_FRONT_URL' e 'PAGEX_BACK_URL' declarados no settings.py."
            )
        front_base = stgs.PAGEX_FRONT_URL
        back_base = stgs.PAGEX_BACK_URL
    return front_base, back_base, pagex_stgs.is_urls_relative  # Packing data in a tuple!


def pagex_front_type_cache(obj: object):
    """It checks, and if needed, caches the Pagex Singleton front_type solution.
    Returns: cached_front_type."""
    # TODO: may be I need to review this because if the front_type changes, in this day I would have
    # to close the Django server to reopen for the new front_type be read apparently over the cache.
    # Check the slug:
    if not hasattr(obj, "slug") or not obj.slug:
        return None
    # Try from cache first:
    cached_front_type = cache.get("pagex_front_type")
    if cached_front_type is None:
        try:
            cached_front_type = PagexSettings.objects.only("front_type").get(pk=1).front_type
            cache.set("pagex_front_type", cached_front_type, consts.VAL_FRONT_TOOL_CACHE)
        except PagexSettings.DoesNotExist:
            raise ImproperlyConfigured(
                f"{consts.TAG_W} O Tipo de Front-end ainda não foi definido. Na interface do Pagex, vá até 'Configurações' e defina o tipo."
            )
    return cached_front_type


def pagex_front_url_setup(front_type, prefix_front, prefix_back, obj, option):
    """Front-end URL setup based on pagex_url_builder request.
    Returns: str URL | None"""
    # Initial values:
    url = None
    # Configuring front URL:
    match front_type:
        case consts.VAL_FRONT_TOOL_DJANGO:
            # Building url:
            if hasattr(obj, "slug"):
                match option:
                    case "page":
                        url = f"{prefix_back}/{obj.slug}"
                        if stgs.DEBUG:
                            print(
                                f"{consts.TAG_D} pagex_front_url_setup > front_type: {front_type} > option: {option} > url: {url}"
                            )
                    case "category":
                        url = f"{prefix_back}/c/{obj.slug}"
                        if stgs.DEBUG:
                            print(
                                f"{consts.TAG_D} pagex_front_url_setup > front_type: {front_type} > option: {option} > url: {url}"
                            )
                    case _:
                        raise ValueError(
                            f"{consts.TAG_E} pagex_front_url_setup > Erro relacionado ao tipo de link de front-end. Provavelmente não está sendo usado 'page' ou 'category' na geração das URLs."
                        )
        case consts.VAL_FRONT_TOOL_VUE:
            # Building url:
            if hasattr(obj, "slug"):
                match option:
                    case "page":
                        url = f"{prefix_front}/{obj.slug}"
                        if stgs.DEBUG:
                            print(
                                f"{consts.TAG_D} pagex_front_url_setup > front_type: {front_type} > option: {option} > url: {url}"
                            )
                    case "category":
                        url = f"{prefix_front}/c/{obj.slug}"
                        if stgs.DEBUG:
                            print(
                                f"{consts.TAG_D} pagex_front_url_setup > front_type: {front_type} > option: {option} > url: {url}"
                            )
        case _:
            raise ValueError(
                f"{consts.TAG_E} pagex_front_url_setup > Erro relacionado ao Tipo de Front-end do projeto. Certifique-se sobre a integridade dos valores de 'CHOICES_FRONTEND' no arquivo 'constants.py' do Pagex."
            )
    return url


def pagex_url_builder(obj: object, builder: int, option: str | None = None):
    """Builds front-end and back-end URLs for front-end-previews or API/JSON-visualizers.
    Args:
        obj: Target object that must have a slug or identifier attribute.
        builder: int, URL builder type:
            1: Front-end CMS page and category preview links;
            2: Front-end menu links;
            3: Back-end Pages API (JSON);
            4: Back-end Menus API (JSON);
        option: Specific builder behavior ('page' or 'category').
    Returns:
        str | None: Built URL or None if invalid parameters.
    """
    # Escape:
    if not hasattr(obj, "slug") and not hasattr(obj, "identifier"):
        return None
    # Initial values:
    prefix_front = ""
    prefix_back = ""
    # Declaring:
    base_urls_data = pagex_setup_basic(obj)
    # Escape:
    if base_urls_data is None:
        return None
    front_base, back_base, is_urls_relative = base_urls_data  # Unpacking
    # Selecting the URL Builder:
    match builder:
        case 1:
            # Declaring:
            front_type = pagex_front_type_cache(obj)
            # If links must be absolute OR if front-end's using Vue:
            if not is_urls_relative or front_type == consts.VAL_FRONT_TOOL_VUE:
                prefix_front = front_base
                prefix_back = back_base
            # Building the URL:
            return pagex_front_url_setup(front_type, prefix_front, prefix_back, obj, option)
        case 2:
            # Declaring:
            front_type = pagex_front_type_cache(obj)
            # If links must be absolute:
            if not is_urls_relative:
                prefix_front = front_base
                prefix_back = back_base
            # Building the URL:
            return pagex_front_url_setup(front_type, prefix_front, prefix_back, obj, option)
        case 3:
            # Building url:
            if hasattr(obj, "slug"):
                url = f"/{consts.PATH_API_PAGES}/{obj.slug}/?format=json"
                if is_urls_relative:
                    return url  # e.g. "/api/pages/home/?format=json"
                return (
                    f"{back_base}{url}"  # e.g. "http://localhost:8000/api/pages/home/?format=json"
                )
        case 4:
            # Building url:
            if hasattr(obj, "identifier"):
                url = f"/{consts.PATH_API_MENUS}/{obj.identifier}/?format=json"
                if is_urls_relative:
                    return url  # e.g. "/api/menus/main_menu/?format=json"
                return f"{back_base}{url}"  # e.g. "http://localhost:8000/api/menus/main_menu/?format=json"
    # If builder fails:
    return None
