# FILE: /apps/my_apps/validators.py

import re
from functools import partial
from django.core.exceptions import ValidationError

def validate_chars_no_spaces(value, can_space: bool = False) -> None:
    """Checks if a text field is using only valid characters (alpha-numeric)."""
    # Escape:
    if not value:
        return None
    # Defining:
    chars = r"^[A-Za-z0-9À-ÿ ]+$" if can_space else r"^[A-Za-z0-9À-ÿ]+$"
    msg = "Use only characters from A to Z"
    msg_add1 = "using one or more forbidden characters"
    msg_add2 = f"{msg}, space and numbers" if can_space else f"{msg}, numbers, and NO spaces"
    if not re.match(chars, value):
        raise ValidationError(
            f"This field's {msg_add1}. {msg_add2}.",
            code="invalid",
        )


# Specialized validators:
validate_chars_spaces_enabled = partial(validate_chars_no_spaces, can_space=True)


# FILE: /apps/my_apps/models.py or forms.py
# Call that specialized validator name in the class field you wanna protect!