"""
    DJANGO > UTILS: ALDO'S SOLUTION

    Set this function in your app's utils.py:
"""

from django.conf import settings as stgs
from . import consts

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
                    case "post":
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
                    case "post":
                        url = f"{prefix_front}/posts/{obj.slug}"
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
                f"{consts.TAG_E} pagex_front_url_setup > Erro relacionado ao Tipo de Front-end do projeto. Certifique-se sobre a integridade dos valores de 'CHOICES_FRONTEND' no arquivo 'consts.py' do Pagex."
            )
    return url