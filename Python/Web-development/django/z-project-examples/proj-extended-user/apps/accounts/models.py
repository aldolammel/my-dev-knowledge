from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinLengthValidator
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields

# from parler.managers import TranslatableManager, TranslatableQuerySet
from .validators import validate_user_agreement, validate_birth, validate_goals
from core import language as lng
from core.constants import (
    CHOICES_STATUS_CONTENT,
    CHOICES_PHONE_CODE,
    CHOICES_PROFILE_TYPE,
    REL_PROFILE_1,
    REL_PROFILE_2,
    CHOICES_SEX,
    VAL_PROFILE_1_NAME_MAXLNGH,
    VAL_PROFILE_2_BNAME_MAXLNGH,
    VAL_PROFILE_2_LEGAL_MAXLNGH,
    VAL_PROFILE_2_CITY_MAXLNGH,
    VAL_PROFILE_2_DESC_MAXLNGH,
)

# MODEL MANAGERS & MODEL QUERYSETS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


"""class GoalQuerySet(TranslatableQuerySet):
    '''Model queryset to xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.'''

    def profile_one(self):
        return self.filter(profile_type='1')

    def profile_two(self):
        return self.filter(profile_type='2')


class GoalManager(TranslatableManager):
    '''Model manager to xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.'''

    # Defining the class where is stored the queryset to use here:
    def get_queryset(self):
        return GoalQuerySet(self.model, using=self._db)

    def profile_one(self):
        return self.get_queryset().profile_one()

    def profile_two(self):
        return self.get_queryset().profile_two()

"""
# MODELS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class Language(models.Model):
    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False,
        verbose_name=lng.LB_NAME,
        validators=[MinLengthValidator(3)],
    )
    iso_code = models.CharField(
        max_length=5,
        unique=False,  # For flexibility, I can set the same ISO for more than one language.
        blank=False,
        null=False,
        verbose_name=lng.LB_ISO_CODE,
        help_text=lng.TX_HELP_USER_LANG_ISO,
        validators=[MinLengthValidator(2)],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name=lng.LB_CREATED_AT,
    )
    status = models.CharField(
        max_length=10,
        choices=CHOICES_STATUS_CONTENT,
        default="on",
        verbose_name=lng.LB_STATUS_CONTENT,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        "User",  # Circular relationship!
        related_name="updated_languages",
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    # Model Managers:
    # Reserved space...

    class Meta:
        db_table = "user_language"
        ordering = ["name"]
        verbose_name = "User Language"
        verbose_name_plural = "User Languages"

    def __str__(self):
        return f"{self.name} ({self.iso_code})"

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.iso_code = self.iso_code.lower()
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop("user", None)
        if user and user.is_authenticated and self.updated_by != user:
            self.updated_by = user
        super().save(*args, **kwargs)


class Country(models.Model):
    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=40,
        unique=True,
        blank=False,
        null=False,
        verbose_name=lng.LB_NAME,
        validators=[MinLengthValidator(4)],
    )
    abbreviation = models.CharField(
        max_length=2,
        unique=True,
        blank=False,
        null=False,
        verbose_name=lng.LB_ABBREV,
        validators=[MinLengthValidator(2)],
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name=lng.LB_LANG_INTERFACE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name=lng.LB_CREATED_AT,
    )
    status = models.CharField(
        max_length=10,
        choices=CHOICES_STATUS_CONTENT,
        default="on",
        verbose_name=lng.LB_STATUS_CONTENT,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        "User",  # Circular relationship!
        related_name="updated_countries",
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    # Model Managers:
    # Reserved space...

    class Meta:
        db_table = "user_country"
        ordering = ["name"]
        verbose_name = "User Country"
        verbose_name_plural = "User Countries"

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.abbreviation = self.abbreviation.upper()
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop("user", None)
        if user and user.is_authenticated and self.updated_by != user:
            self.updated_by = user
        super().save(*args, **kwargs)


class Phone(models.Model):
    phone_id = models.PositiveBigIntegerField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    country_code = models.CharField(
        max_length=100,
        choices=CHOICES_PHONE_CODE,
        null=False,
        blank=False,
        verbose_name=lng.LB_PHONE_COUNTRY_CODE,
    )
    region_code = models.PositiveSmallIntegerField(
        verbose_name=lng.LB_PHONE_REGION_CODE,
    )
    number = models.PositiveBigIntegerField(
        verbose_name=lng.LB_PHONE_NUMBER,
        # TODO: Min and max characters!
    )
    # TODO FIX: if someone has register your number. How to validate the number is yours...
    """owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=False,
        related_name='phone',
        verbose_name=lng.LB_PHONE_OWNER,
    )"""
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name=lng.LB_CREATED_AT,
    )

    # Model Managers:
    # Reserved space...

    class Meta:
        db_table = "user_phone"
        ordering = ["phone_id"]
        verbose_name = "User Phone"
        verbose_name_plural = "User Phones"

    def __str__(self):
        # +55 (51) 980394586
        return f"+{self.country_code} ({self.region_code}) {self.number}"

    def save(self, *args, **kwargs):
        # Build the phone_id by concatenating the fields:
        self.phone_id = int(f"{self.country_code}{self.region_code}{self.number}")
        super().save(*args, **kwargs)


class Goal(TranslatableModel):
    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    profile_type = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        choices=CHOICES_PROFILE_TYPE,
        verbose_name=lng.LB_PROFILE_TYPE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name=lng.LB_CREATED_AT,
    )
    status = models.CharField(
        max_length=10,
        choices=CHOICES_STATUS_CONTENT,
        default="on",
        verbose_name=lng.LB_STATUS_CONTENT,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        "User",  # Circular relationship!
        related_name="updated_goals",
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )
    translations = TranslatedFields(
        goal=models.CharField(
            max_length=60,
            unique=False,  # For model translation, this argument is set via 'meta' argument!
            blank=False,
            null=False,
            verbose_name=lng.LB_GOAL,
            validators=[MinLengthValidator(10)],
        ),
    )
    # TODO Fix, try to fix this Parler issue (handling with Unique attributes) that i didn't yet:
    """translations = TranslatedFields(
        goal=models.CharField(
            max_length=60,
            unique=False,  # For model translation, this argument is set via 'meta' argument!
            blank=False,
            null=False,
            verbose_name=lng.LB_GOAL,
            meta={
                'unique_together': [('language_code', lng.LB_GOAL)]
            },  # unique title for each single language!
        ),  # type: ignore
    )"""

    # Model Managers:
    # Reserved space...

    class Meta:
        db_table = "goal"
        ordering = ["-status"]
        # verbose_name = 'Goal'
        # verbose_name_plural = 'Goals'

    def __str__(self):
        return self.goal

    def save(self, *args, **kwargs):
        self.goal = self.goal.capitalize()
        super().save(*args, **kwargs)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a user with an email and password."""
        if not email:
            raise ValueError("The Email field must be set")  # TODO translate it!
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
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=lng.LB_LANG_INTERFACE,
        help_text=lng.TX_HELP_USER_LANG,
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
        """Built-in Model method used to provide custom model-level validation logic, and is called by full_clean() before save() the instance."""
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
    # It's not used anymore!
    """last_name = models.CharField(
        max_length=VAL_PROFILE_1_NAME_MAXLNGH,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_LNAME,
        validators=[MinLengthValidator(3)],
        error_messages={
            'max_length': lng.TX_ERRO_PROFILE_1_LNAME_MAXLNGH
            % {
                'txt': lng.LB_PROFILE_1_LNAME,
                'val': VAL_PROFILE_1_NAME_MAXLNGH,
            }
        },
    )"""
    sex = models.CharField(
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
    )
    # TODO
    """phone = models.OneToOneField(
        Phone,
        on_delete=models.SET_NULL,
        null=True,  # Ensure it's optional
        blank=True,  # Allow blank in form
        related_name='user',
        verbose_name=lng.LB_PHONE_NUMBER,
    )"""
    # TODO is_notified_by_phone = models.BooleanField(default=False, verbose_name=lng.LB_NOTIF_BY_PHONE,)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_1_COUNTRY,
        help_text=lng.TX_HELP_PROFILE_1_COUNTRY,
        error_messages={
            "blank": lng.TX_ERRO_PROFILE_1_COUNTRY_BLNK,
        },
    )
    is_nomad = models.BooleanField(
        default=False,
        verbose_name=lng.LB_PROFILE_1_NOMAD,
        help_text=lng.TX_HELP_PROFILE_1_NOMAD,
    )
    city = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_CITY,
        help_text=lng.TX_HELP_PROFILE_1_CITY,
        validators=[MinLengthValidator(3)],
    )
    goal_primary = models.ForeignKey(
        Goal,
        related_name="goal_primary_personals",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_GOAL_PRI,
        help_text=lng.TX_HELP_PROFILE_1_GOAL_PRI,
    )
    goal_secondary = models.ForeignKey(
        Goal,
        related_name="goal_secundary_personals",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_GOAL_SEC,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        User,
        editable=False,
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
        """Built-in Model method used to provide custom model-level validation logic, and is called by full_clean() before save() the instance."""
        validate_birth(self.birthdate)
        validate_goals(self.goal_primary, self.goal_secondary)

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
        if user and user.is_authenticated:
            self.updated_by = user
        super().save(*args, **kwargs)


class UserProfileTwo(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,  # Tells Django to del the UserProfileTwo if the User is deleted.
        related_name=REL_PROFILE_2,
        verbose_name=lng.LB_PROFILES_USER,
    )
    business_name = models.CharField(
        max_length=VAL_PROFILE_2_BNAME_MAXLNGH,
        # unique=True,  # Commercial name must be flexible! Legal name, not!
        null=False,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_BNAME,
        help_text=lng.TX_HELP_PROFILE_2_BNAME,
        validators=[MinLengthValidator(4)],
        error_messages={
            "blank": lng.TX_ERRO_PROFILE_2_BNAME_BLNK,
            # 'unique': 'This business name already exists.'
            "max_length": lng.TX_ERRO_PROFILE_2_BNAME_MAXLNGH
            % {
                "txt": lng.LB_PROFILE_2_BNAME,
                "val": VAL_PROFILE_2_BNAME_MAXLNGH,
            },
        },
    )
    legal_name = models.CharField(
        max_length=VAL_PROFILE_2_LEGAL_MAXLNGH,
        unique=True,
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_LEGAL,
        help_text=lng.TX_HELP_PROFILE_2_LEGAL,
        validators=[MinLengthValidator(6)],
        error_messages={
            "blank": lng.TX_ERRO_PROFILE_2_LEGAL_BLNK,
            "unique": lng.TX_ERRO_PROFILE_2_LEGAL_UNIQ,
            "max_length": lng.TX_ERRO_PROFILE_2_LEGAL_MAXLNGH
            % {
                "txt": lng.LB_PROFILE_2_LEGAL,
                "val": VAL_PROFILE_2_LEGAL_MAXLNGH,
            },
        },
    )
    country_business = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_COUNTRY,
        help_text=lng.TX_HELP_PROFILE_2_COUNTRY,
        error_messages={
            "blank": lng.TX_ERRO_PROFILE_1_COUNTRY_BLNK,
        },
    )
    city_business = models.CharField(
        max_length=VAL_PROFILE_2_CITY_MAXLNGH,
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_CITY,
        help_text=lng.TX_HELP_PROFILE_2_CITY,
        validators=[MinLengthValidator(3)],
        error_messages={
            "blank": lng.TX_ERRO_PROFILE_2_CITY_BLNK,
            "max_length": lng.TX_ERRO_PROFILE_2_CITY_MAXLNGH
            % {
                "txt": lng.LB_PROFILE_2_CITY,
                "val": VAL_PROFILE_2_CITY_MAXLNGH,
            },
        },
    )
    description = models.TextField(
        max_length=VAL_PROFILE_2_DESC_MAXLNGH,
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_DESC,
        help_text=lng.TX_HELP_PROFILE_2_DESC,
        validators=[MinLengthValidator(40)],
        error_messages={
            "blank": lng.TX_ERRO_PROFILE_2_DESC_BLNK,
            "max_length": lng.TX_ERRO_PROFILE_2_DESC_MAXLNGH
            % {
                "txt": lng.LB_PROFILE_2_DESC,
                "val": VAL_PROFILE_2_DESC_MAXLNGH,
            },
        },
    )
    business_url = models.URLField(
        blank=True,
        verbose_name=lng.LB_PROFILE_2_URL,
        validators=[MinLengthValidator(12)],
    )
    social_media = models.URLField(
        blank=True,
        verbose_name=lng.LB_PROFILE_2_URL_SOCIAL,
        validators=[MinLengthValidator(12)],
    )
    business_email = models.EmailField(
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_EMAIL,
        validators=[MinLengthValidator(8)],
        error_messages={
            "blank": lng.TX_ERRO_PROFILE_2_EMAIL_BLNK,
            "invalid": lng.TX_ERRO_PROFILE_2_EMAIL_INVLD,
        },
    )
    """phone = models.OneToOneField(
        Phone,
        on_delete=models.SET_NULL,
        null=True,  # Ensure it's optional
        blank=True,  # Allow blank in form
        related_name='user',
        verbose_name=lng.LB_PHONE_NUMBER,
    )"""
    # TODO is_notified_by_phone = models.BooleanField(default=False, verbose_name=lng.LB_NOTIF_BY_PHONE,)
    goal_primary = models.ForeignKey(
        Goal,
        related_name="goal_primary_businesses",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=lng.LB_PROFILE_2_GOAL_PRI,
    )
    goal_secondary = models.ForeignKey(
        Goal,
        related_name="goal_secundary_businesses",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=lng.LB_PROFILE_2_GOAL_SEC,
    )
    busi_first_name = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=lng.LB_PROFILE_2_FNAME,
        validators=[MinLengthValidator(3)],
    )
    busi_last_name = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=lng.LB_PROFILE_2_LNAME,
        validators=[MinLengthValidator(3)],
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        User,
        editable=False,
        related_name="updated_profiles_2",
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    # Model Managers:
    # Reserved space...

    class Meta:
        db_table = "user_profile_two"
        ordering = ["user", "-updated_at"]
        verbose_name = "Profile, Business"
        verbose_name_plural = "Profiles, Business"

    def __str__(self):
        if self.user:
            if self.business_name:
                return f"{self.business_name} ({self.user.username})"
            return self.user.username
        return lng.CMS_ERRO_PROFILE

    def clean(self):
        """Built-in Model method used to provide custom model-level validation logic, and is called by full_clean() before save() the instance."""
        validate_goals(self.goal_primary, self.goal_secondary)

    def save(self, *args, **kwargs):
        if self.business_name:
            self.business_name = self.business_name.title()
        if self.legal_name:
            self.legal_name = self.legal_name.upper()
        if self.busi_first_name:
            self.busi_first_name = self.busi_first_name.title()
        if self.busi_last_name:
            self.busi_last_name = self.busi_last_name.title()
        if self.city_business:
            self.city_business = self.city_business.title()
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop("user", None)
        if user and user.is_authenticated and self.updated_by != user:
            self.updated_by = user
        super().save(*args, **kwargs)
