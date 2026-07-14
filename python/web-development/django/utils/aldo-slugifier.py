"""
    DJANGO > UTILS: ALDO'S SLUGIFIER SOLUTION

    
"""


# apps/your_app/utils.py:

def pagex_slugifier(txt: str, is_underscore: bool = False, should_suffix: bool = False):
    """Extended Django slugify function to serve Pagex purposes."""
    from django.utils.text import slugify

    # Initial value:
    slugified = slugify(txt)
    # Traditional slug (common):
    if not is_underscore and not should_suffix:
        return slugified  # E.g. text-like-this
    # Special slugs:
    special_slugified = slugified.replace("-", "_")
    # Slug with underscore instead:
    if is_underscore and not should_suffix:
        return special_slugified  # E.g. text_like_this
    # Slug underscore with prefix:
    if is_underscore and should_suffix:
        from random import randint

        return f"{special_slugified}_{randint(20, 9999)}"  # E.g. text_like_this_3023
    else:
        print(f"{consts.TAG_E}: pagex_slugifier() has trying a forbidden setup!")
        return None
