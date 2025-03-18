from django.core.exceptions import ValidationError
from django.utils import timezone
from core.constants import (
    VAL_PROFILE_1_BIRTH_MIN,
    VAL_PROFILE_1_BIRTH_MAX,
)
from core.language import (
    TX_ERRO_USER_AGE_MIN,
    TX_ERRO_USER_PRIVACY,
    # S_G_PRIVACY_NAME,
    TX_ERRO_PROFILE_1_BIRTH_MIN,
    TX_ERRO_PROFILE_1_BIRTH_MAX,
)


def validate_user_agreement(instance):
    """Server-side validation for user's acceptance of the minimum age and privacy policy."""
    if not instance.accepted_min_age:
        raise ValidationError(TX_ERRO_USER_AGE_MIN, code="invalid_choice")
    if not instance.accepted_our_privacy:
        raise ValidationError(TX_ERRO_USER_PRIVACY, code="invalid_choice")


def validate_birth(birth):
    """Server-side validation to check whether the user age makes sense."""
    if birth:
        current_year = timezone.now().year
        if current_year - birth.year < VAL_PROFILE_1_BIRTH_MIN:
            raise ValidationError(TX_ERRO_PROFILE_1_BIRTH_MIN, code="min_length")
        elif current_year - birth.year > VAL_PROFILE_1_BIRTH_MAX:
            raise ValidationError(TX_ERRO_PROFILE_1_BIRTH_MAX, code="max_length")

