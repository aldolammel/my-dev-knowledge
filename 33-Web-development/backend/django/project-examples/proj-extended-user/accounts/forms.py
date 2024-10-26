from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .validators import validate_user_agreement
from .models import User, UserProfileOne, UserProfileTwo, Language
from cefalog import language as lng


class CustomUserCreationForm(UserCreationForm):
    """Customizing the Django User Registration form for front-end."""

    class Meta:
        # Connected model to populate:
        model = User
        # Ordering fields on the form:
        fields = [
            'profile_type',
            'username',
            'email',
            'password1',
            'password2',
            'accepted_min_age',
            'accepted_our_privacy',
        ]

    # Extra fields:
    # Important: signals.py: should the extra fields be declared over there? Check it!
    # Reserved space...


class UserProfileOneForm(forms.ModelForm):
    """UserProfile form specific for Personal usage through front-end."""

    class Meta:
        # Connected model to populate:
        model = UserProfileOne
        # Ordering fields on the form:
        fields = [
            'first_name',  # from connected model
            'last_name',  # from connected model
            'sex',  # from connected model
            'birthdate',  # from connected model
            'email',  # extra
            'is_notified_by_email',  # extra
            'language',  # extra
            'country',  # from connected model
            'is_nomad',  # from connected model
            'city',  # from connected model
        ]

    # Extra fields:
    email = forms.EmailField(
        required=True,
        label=lng.LB_USER_EMAIL,
    )
    is_notified_by_email = forms.BooleanField(
        required=False,
        label=lng.LB_USER_NOTIF_BY_EMAIL,
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        required=False,
        label=lng.LB_USER_LANG,
    )

    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is instantiated.'''
        user = kwargs.pop('user', None)  # Get the current user (from view)!
        super().__init__(*args, **kwargs)
        if user:

            # Connected fields (from connected model), customizations:
            self.fields['birthdate'].widget = forms.DateInput(attrs={'type': 'date'})

            # Extra fields, pre-populating:
            # Unlike fields from connected model, extra fields must be manually linked!
            self.fields['email'].initial = user.email
            self.fields['is_notified_by_email'].initial = user.is_notified_by_email
            self.fields['language'].initial = user.language

    def save(self, user=None, commit=True):
        instance = super().save(commit=False)  # commit=False will not save in db immediately.
        if user:
            instance.updated_at = timezone.now()
            instance.updated_by = user
        if commit:
            instance.save()
        return instance


class UserProfileTwoForm(forms.ModelForm):
    """UserProfile form specific for Business usage through front-end."""

    class Meta:
        # Connected model to populate:
        model = UserProfileTwo
        # Ordering fields on the form:
        fields = [
            'country_business',  # from connected model
            'city_business',  # from connected model
            'language',  # extra
            'business_name',  # from connected model
            'legal_name',  # from connected model
            'description',  # from connected model
            'business_url',  # from connected model
            'social_media',  # from connected model
            'business_email',  # from connected model
            'contact_first_name',  # from connected model
            'contact_last_name',  # from connected model
            'email',  # extra
            'is_notified_by_email',  # extra
        ]

    # Extra fields:
    email = forms.EmailField(
        required=True,
        label=lng.LB_USER_EMAIL,
    )
    is_notified_by_email = forms.BooleanField(
        required=False,
        label=lng.LB_USER_NOTIF_BY_EMAIL,
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        required=False,
        label=lng.LB_USER_LANG,
    )

    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is instantiated.'''
        user = kwargs.pop('user', None)  # Get the current user (from view)!
        super().__init__(*args, **kwargs)
        if user:

            # Connected fields (from connected model), customizations:
            # Reserved space...

            # Extra fields, pre-populating:
            # Unlike fields from connected model, extra fields must be manually linked!
            self.fields['email'].initial = user.email
            self.fields['is_notified_by_email'].initial = user.is_notified_by_email
            self.fields['language'].initial = user.language

    def save(self, user=None, commit=True):
        instance = super().save(commit=False)  # commit=False will not save in db immediately.
        if user:
            instance.updated_at = timezone.now()
            instance.updated_by = user
        if commit:
            instance.save()
        return instance
