from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinLengthValidator
from django.utils import timezone
#from parler.models import TranslatableModel, TranslatedFields

# from parler.managers import TranslatableManager, TranslatableQuerySet
from .validators import validate_user_agreement, validate_birth
from core import language as lng
from core.constants import (
    CHOICES_PROFILE_TYPE,
    REL_PROFILE_1,
    #CHOICES_SEX,
    VAL_PROFILE_1_NAME_MAXLNGH,
)

# MODEL MANAGERS & MODEL QUERYSETS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Reserved space.

    
# MODELS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a user with an email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        # Set the custom fields as True:
        extra_fields.setdefault("accepted_min_age", True)
        extra_fields.setdefault("accepted_our_privacy", True)

        # Call the existing create_user method from BaseUserManager
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    id = models.BigAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    profile_type = models.CharField(
        max_length=15,
        choices=CHOICES_PROFILE_TYPE,
        default="1",  # 1=Personal / 2=Business. Needed, e.g. when Django superuser is created.
        null=False,
        blank=False,
        verbose_name=lng.LB_PROFILE_TYPE,
        help_text=lng.TX_HELP_USER_PROFILE,
        error_messages={
            "blank": lng.TX_ERRO_USER_PROFILE_BLNK,
        },
    )
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name=lng.LB_USER_EMAIL,
        validators=[MinLengthValidator(8)],
        help_text=lng.TX_HELP_USER_EMAIL,
        error_messages={
            "blank": lng.TX_ERRO_USER_EMAIL_BLNK,
            "invalid": lng.TX_ERRO_USER_EMAIL_INVLD,
        },
    )
    is_notified_by_email = models.BooleanField(
        default=True,
        verbose_name=lng.LB_USER_NOTIF_BY_EMAIL,
        help_text=lng.TX_HELP_USER_NOTIF_EMAIL,
    )
    accepted_min_age = models.BooleanField(
        default=False,
        verbose_name=lng.LB_USER_AGE_MIN,
        help_text=lng.TX_HELP_USER_AGE_MIN,
        # error_messages in validators.py
    )
    accepted_our_privacy = models.BooleanField(
        default=False,
        verbose_name=lng.LB_USER_PRIVACY,
        help_text=lng.TX_HELP_USER_PRIVACY,
        # error_messages in validators.py
    )
    last_pwd_update = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=lng.LB_USER_PWD_LAST_UPDATE,
    )
    # created_at = 'date_joined' from AbstractUser
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        "self",  # Itself relationship!
        related_name="updated_users",
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    # Model Managers:
    # Reserved space...

    objects = (
        CustomUserManager()
    )  # needed coz additional fields of superuser creation by terminal.

    class Meta:
        db_table = "auth_user"
        ordering = ["username"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        """Built-in method to deal the user's password, taking care of the password hashing."""
        super().set_password(raw_password)
        if self.pk:  # avoids the error on register form!
            self.last_pwd_update = timezone.now()
            self.save(update_fields=["password", "last_pwd_update"])

    def clean(self):
        """It's a built-in method for adding custom validation logic before saving data to the db."""
        validate_user_agreement(self)

    def save(self, *args, **kwargs):
        """Built-in method that's executed when the entry saving runs."""
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop("user", None)  # Retrieve the user from kwargs!
        if user and user.is_authenticated and self.updated_by != user:
            self.updated_by = user
        super().save(*args, **kwargs)


class UserProfileOne(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,  # Tells Django to del the UserProfileOne if the User is deleted.
        related_name=REL_PROFILE_1,
        verbose_name=lng.LB_PROFILES_USER,
    )
    first_name = models.CharField(
        max_length=VAL_PROFILE_1_NAME_MAXLNGH,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_FNAME,
        validators=[MinLengthValidator(2)],
        help_text=lng.TX_HELP_PROFILE_1_NAME,
        error_messages={
            "max_length": lng.TX_ERRO_PROFILE_1_FNAME_MAXLNGH
            % {
                "txt": lng.LB_PROFILE_1_FNAME,
                "val": VAL_PROFILE_1_NAME_MAXLNGH,
            },
        },
    )
    """sex = models.CharField(
        max_length=20,
        choices=CHOICES_SEX,
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_1_SEX,
        help_text=lng.TX_HELP_PROFILE_1_SEX,
        error_messages={
            "blank": lng.TX_ERRO_PROFILE_1_SEX_BLNK,
        },
    )
    birthdate = models.DateField(
        null=True,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_BIRTHDATE,
        help_text=lng.TX_HELP_PROFILE_1_BIRTHDATE,
        error_messages={
            "invalid": lng.TX_ERRO_PROFILE_1_BIRTH_INVLD,
        },
    )
    birth_year = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_BIRTH_YEAR,
    )"""
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="updated_profiles_1",
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    # Model Managers:
    # Reserved space...

    class Meta:
        db_table = "user_profile_one"
        ordering = ["user", "-updated_at"]
        verbose_name = "Profile, Personal"
        verbose_name_plural = "Profiles, Personal"

    def __str__(self):
        if self.user:
            if self.first_name:
                return f"{self.user.username} ({self.first_name})"
            return self.user.username
        return lng.CMS_ERRO_PROFILE

    def clean(self):
        """It's a built-in method for adding custom validation logic before saving data to the db."""
        validate_birth(self.birthdate)

    def save(self, *args, **kwargs):
        # if self.first_name:
        #     self.first_name = self.first_name.title()  # Let the user choose their way!
        # if self.last_name:
        #     self.last_name = self.last_name.title()  # It's not used anymore!
        if self.city:
            self.city = self.city.title()
        # Defining the user's birth year automatically:
        if self.birthdate:
            self.birth_year = str(self.birthdate)[:4]
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop("user", None)
        if user and user.is_authenticated and self.updated_by != user:
            self.updated_by = user
        super().save(*args, **kwargs)