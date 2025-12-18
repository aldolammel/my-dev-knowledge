"""
    DJANGO > UTILS: ALDO'S SOLUTION

    Set this function in your app's utils.py:
"""

from . import constants as consts

def pagex_url_builder(obj: object, builder: int, option: str | None = None):
    """Builds front-end and back-end URLs for front-end-previews or API/JSON-visualizers.
    Args:
        obj: Target object that must have a slug or identifier attribute.
        builder: int, URL builder type:
            1: Front-end CMS page, post and category preview links;
                option: 'page', 'post' or 'category';
            2: Front-end menu links;
            3: Back-end Pages API (JSON);
            4: Back-end Posts API (JSON);
            5: Back-end Structure Content API (JSON);
            6: Back-end Menus API (JSON);
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
            # Building page url:
            if hasattr(obj, "slug"):
                url = f"/{consts.PATH_API_PAGES}/{obj.slug}/?format=json"
                if is_urls_relative:
                    return url  # e.g. "/api/pages/home/?format=json"
                return f"{back_base}{url}"
                # e.g. "http://localhost:8000/api/pages/home/?format=json"
        case 4:
            # Building post url:
            if hasattr(obj, "slug"):
                url = f"/{consts.PATH_API_POSTS}/{obj.slug}/?format=json"
                if is_urls_relative:
                    return url  # e.g. "/api/posts/my-post/?format=json"
                return f"{back_base}{url}"
                # e.g. "http://localhost:8000/api/posts/my-post/?format=json"
        case 5:
            # Building structure content url:
            if hasattr(obj, "identifier"):
                url = f"/{consts.PATH_API_STRUCTS}/{obj.identifier}/?format=json"
                if is_urls_relative:
                    return url  # e.g. "/api/structures/struct_footer/?format=json"
                return f"{back_base}{url}"
                # e.g. "http://localhost:8000/api/menus/struct_footer/?format=json"
        case 6:
            # Building menu url:
            if hasattr(obj, "identifier"):
                url = f"/{consts.PATH_API_MENUS}/{obj.identifier}/?format=json"
                if is_urls_relative:
                    return url  # e.g. "/api/menus/main_menu/?format=json"
                return f"{back_base}{url}"  # e.g. "http://localhost:8000/api/menus/main_menu/?format=json"
    # If builder fails:
    return None