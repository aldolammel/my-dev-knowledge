"""
    DJANGO: ALDO'S SOLUTION

    Set this function in your app's validators.py:
"""

import re
from functools import partial
from django.core.exceptions import ValidationError


# Validators - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
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

# Validators > Specialized - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# A validate_chars_no_spaces variant, but accepting spaces:
validate_chars_spaces_enabled = partial(validate_chars_no_spaces, can_space=True)

# Not traditional validators - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Reserved space...