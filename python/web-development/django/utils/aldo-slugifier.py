"""
    DJANGO > UTILS: ALDO'S SOLUTION

    Set this function in your app's utils_models.py:
"""

# TO AVOID CIRCULAR IMPORT ERRORS, THIS FILE DOESN'T IMPORT ANY FROM MODELS.PY, AND ITS UTILS ARE APPLIED ONLY FOR MODELS.PY:


def pagex_slugifier(txt: str, is_underscore: bool = False, should_prefix: bool = False):
    from django.utils.text import slugify

    # Initial value:
    slugified = slugify(txt)
    # Traditional slug (common):
    if not is_underscore and not should_prefix:
        return slugified  # text-like-this
    # Special slugs:
    special_slugified = slugified.replace("-", "_")
    # Slug with underscore instead:
    if is_underscore and not should_prefix:
        return special_slugified  # text_like_this
    # Slug underscore with prefix:
    if is_underscore and should_prefix:
        from random import randint

        return f"{randint(1, 9999)}_{special_slugified}"  # 0001_text_like_this
    else:
        print("PAGEX ERROR: pagex_slugifier has trying an ilegal setup!")
        return None
