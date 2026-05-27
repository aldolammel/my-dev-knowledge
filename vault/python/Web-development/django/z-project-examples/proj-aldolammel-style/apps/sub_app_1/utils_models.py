# TO AVOID CIRCULAR IMPORT ERRORS, THIS FILE DOESN'T IMPORT ANY FROM MODELS.PY, AND ITS UTILS ARE APPLIED ONLY FOR MODELS.PY:


def slugifier(txt: str, is_underscore: bool = False):
    from django.utils.text import slugify

    # Traditional slug:
    if not is_underscore:
        return slugify(txt)  # text-like-this
    # Underscored slug:
    return slugify(txt).replace("-", "_")  # text_like_this
