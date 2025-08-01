from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.utils import timezone
from datetime import timedelta
from .models import User, UserProfileOne, Language  # TODO: has multilingual support?
from core import language as lng
from core.settings import DATE_INPUT_FORMATS
from core.constants import (
    VAL_PROFILE_1_BIRTH_MAX,
    VAL_PROFILE_1_BIRTH_MIN,
)

# It's needed for birthdate calcs:
today = timezone.now()


class CustomUserCreationForm(UserCreationForm):
    """Customizing the Django User Registration form for front-end."""

    class Meta:
        # Connected model to populate:
        model = User
        # Ordering fields on the form:
        fields = [
            "profile_type",
            "username",
            "email",
            "password1",  # Extra
            "password2",  # Extra
            "accepted_min_age",
            "accepted_our_privacy",
        ]
        # Simple and static tweaks only for connected model's fields:
        widgets = {
            #'profile_type': forms.Select(attrs={}),
            "username": forms.TextInput(attrs={"class": "input is-large"}),
            "email": forms.EmailInput(
                attrs={"class": "input is-large", "type": "email"}
            ),
            "accepted_min_age": forms.CheckboxInput(
                attrs={"class": "is-large", "id": "accepted_min_age"}
            ),
            "accepted_our_privacy": forms.CheckboxInput(
                attrs={"class": "is-large", "id": "accepted_our_privacy"}
            ),
        }

    # Extra fields:
    password1 = forms.CharField(
        required=True,
        label=lng.LB_PROFILE_PWD_1,
        widget=forms.PasswordInput(
            attrs={"class": "input is-large", "type": "password"}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        required=True,
        label=lng.LB_PROFILE_PWD_2,
        widget=forms.PasswordInput(
            attrs={"class": "input is-large", "type": "password"}
        ),
        help_text=lng.TX_HELP_PROFILE_PWD2,
    )


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label=lng.LB_USER,
        widget=forms.TextInput(attrs={"class": "input is-large"}),
    )
    password = forms.CharField(
        required=True,
        label=lng.LB_PROFILE_PWD_1,
        widget=forms.PasswordInput(attrs={"class": "input is-large"}),
    )


class CustomPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        required=True,
        label=lng.LB_USER_PWD_NEW,
        widget=forms.PasswordInput(
            attrs={"class": "input is-large", "type": "password"}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        required=True,
        label=lng.LB_USER_PWD_NEW_CONF,
        widget=forms.PasswordInput(
            attrs={"class": "input is-large", "type": "password"}
        ),
        help_text=lng.TX_HELP_PROFILE_PWD2,
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        required=True,
        label=lng.LB_USER_PWD_OLD,
        widget=forms.PasswordInput(
            attrs={"class": "input is-large", "type": "password"}
        ),
    )
    new_password1 = forms.CharField(
        required=True,
        label=lng.LB_USER_PWD_NEW,
        widget=forms.PasswordInput(
            attrs={"class": "input is-large", "type": "password"}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        required=True,
        label=lng.LB_USER_PWD_NEW_CONF,
        widget=forms.PasswordInput(
            attrs={"class": "input is-large", "type": "password"}
        ),
        help_text=lng.TX_HELP_PROFILE_PWD2,
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.CharField(
        required=True,
        label=lng.LB_USER_EMAIL,
        widget=forms.EmailInput(attrs={"class": "input is-large", "type": "email"}),
    )


class UserProfileOneForm(forms.ModelForm):
    """UserProfile form specific for Personal usage through front-end."""

    class Meta:
        # Connected model:
        model = UserProfileOne
        # Ordering fields on form:
        fields = [
            #"sex",  # from connected model
            #"birthdate",  # from connected model
            "first_name",  # from connected model
            #'last_name',  # from connected model # Not used anymore!
            "email",  # extra
            "is_notified_by_email",  # extra
            #"language",  # extra  # TODO: has multilingual support?
            "last_pwd_update",  # extra
        ]
        # Simple and static tweaks only for connected model's fields:
        widgets = {
            # 'sex': forms.Select(attrs={}),
            # "birthdate": forms.DateInput(
            #     format=DATE_INPUT_FORMATS[0],  # Enforcing the db format explicitly!
            #     attrs={"class": "input is-large", "type": "date"},
            # ),
            "first_name": forms.TextInput(attrs={"class": "input is-large"}),
            #'last_name': forms.TextInput(attrs={'class': 'input is-large'}), # Not used anymore!
            # 'country': forms.Select(attrs={}),
        }

    # Extra (non-model) fields:
    email = forms.EmailField(
        required=True,
        label=lng.LB_USER_EMAIL,
        widget=forms.TextInput(attrs={"class": "input is-large"}),
        help_text=lng.TX_HELP_USER_EMAIL,
        error_messages={
            "blank": lng.TX_ERRO_USER_EMAIL_BLNK,
            "invalid": lng.TX_ERRO_USER_EMAIL_INVLD,
        },
    )
    is_notified_by_email = forms.BooleanField(
        required=False,
        label=lng.LB_USER_NOTIF_BY_EMAIL,
        widget=forms.CheckboxInput(
            attrs={"class": "is-large", "id": "is_notified_by_email"}
        ),
        help_text=lng.TX_HELP_USER_NOTIF_EMAIL,
    )
    # TODO: has multilingual support?
    # language = forms.ModelChoiceField(
    #     queryset=Language.objects.filter(status="on"),
    #     required=False,
    #     label=lng.LB_USER_LANG,
    #     help_text=lng.TX_HELP_USER_LANG,
    # )
    last_pwd_update = forms.DateTimeField(
        required=False,
        label=lng.LB_USER_PWD_LAST_UPDATE,
        widget=forms.TextInput(attrs={"class": "input is-small pl-0"}),
    )

    def __init__(self, *args, **kwargs):
        """Built-in method that's called when the form is initializated."""
        user = kwargs.pop("user", None)  # Get the current user (from view)!
        super().__init__(*args, **kwargs)
        if user:
            # More complex or dynamic tweaks for connected model's fields:
            age_min = (
                timezone.now() - timedelta(days=365.25 * VAL_PROFILE_1_BIRTH_MIN)
            ).date()
            age_max = (
                timezone.now() - timedelta(days=365.25 * VAL_PROFILE_1_BIRTH_MAX)
            ).date()
            # self.fields["birthdate"].widget.attrs.update(
            #     {"max": age_min, "min": age_max}
            # )

            # Extra fields, pre-populating:
            # Unlike fields from connected model, extra fields must be manually linked!
            self.fields["email"].initial = user.email
            self.fields["is_notified_by_email"].initial = user.is_notified_by_email
            #self.fields["language"].initial = user.language  # TODO: has multilingual support?
            self.fields["last_pwd_update"].initial = user.last_pwd_update

    def save(self, user=None, commit=True):
        """Built-in method that, if triggered, create or update an instance in the connected model."""
        instance = super().save(
            commit=False
        )  # commit=False will not save in db immediately.
        if user:
            instance.updated_at = timezone.now()
            instance.updated_by = user
        if commit:
            instance.save()
        return instance
