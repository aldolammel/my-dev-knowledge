"""
    DJANGO > VALIDATIONS: ALDO'S SOLUTION

    Set this function in your app's validators.py:
"""

from django.core.exceptions import ValidationError


# Validators - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Reserved space...

# Validators > Specialized - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Reserved space...

# Not traditional validators - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def clean_checker_txt_uniqueness(
    model, obj, f_name: str, f_current_value: str, is_formatted: bool, format_type: str
):
    """Function to be used with clean() method! It checks if Django and db have exactly the same txt field value. It must be used only with txt fields (char/slug/url) that are using UNIQUE TRUE.

    REMINDER:
    In case of the field to be checked has been formatted (with .title() or something else) after the clean() method, it's crucial this function be set as 'is_formatted' TRUE, and 'format_type' as exactly the same way the database expect. Otherwise, existent entries might get IntegrityError if different formatting is tried, e.g., 'Market' to 'market' or 'MARKET'.

    Returns : str | None"""
    prefix = "i"
    f_current_value = f_current_value.strip()
    if is_formatted:
        prefix = ""
        match format_type:
            case "title":  # Hello World
                f_current_value = f_current_value.title()
            case "lower":  # hello world
                f_current_value = f_current_value.lower()
            case "upper":  # HELLO WORLD
                f_current_value = f_current_value.upper()
            case "capitalize":  # Hello world
                f_current_value = f_current_value.capitalize()
    filter_kwargs = {f"{f_name}__{prefix}exact": f_current_value}  # Packing dict!
    # Avoiding just the current obj (if it exists), also filtering by all entries w/ same name:
    if model.objects.exclude(pk=obj.pk).filter(**filter_kwargs).exists():  # Unpacking dict
        raise ValidationError(f"Caution: '{f_current_value}' already exists in another register.")
    # Return:
    return f_current_value