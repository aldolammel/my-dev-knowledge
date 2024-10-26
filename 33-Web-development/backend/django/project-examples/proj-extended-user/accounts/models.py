from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_user_agreement, validate_birth
from parler.models import TranslatableModel, TranslatedFields
from cefalog import language as lng
from cefalog.constants import (
    BRAND_NAME,
    CHOICES_STATUS_CONTENT,
    CHOICES_PHONE_CODE,
    CHOICES_PROFILE_TYPE,
    REL_PROFILE_1,
    REL_PROFILE_2,
    CHOICES_SEX,
    VAL_PROFILE_1_NAME_MAXLNGH,
    VAL_PROFILE_1_BIRTH_MIN,
    VAL_PROFILE_2_BNAME_MAXLNGH,
    VAL_PROFILE_2_LEGAL_MAXLNGH,
    VAL_PROFILE_2_CITY_MAXLNGH,
    VAL_PROFILE_2_DESC_MAXLNGH,
)


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
    )
    iso_code = models.CharField(
        max_length=3,
        unique=False,  # For flexibility, I can set the same ISO for more than one language.
        blank=False,
        null=False,
        verbose_name=lng.LB_ISO_CODE,
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
        default='on',
        verbose_name=lng.LB_STATUS_CONTENT,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        'User',  # Circular relationship!
        related_name='updated_languages',
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    class Meta:
        db_table = 'user_language'
        ordering = ['name']
        verbose_name = 'User Language'
        verbose_name_plural = 'User Languages'

    def __str__(self):
        return f'{self.name} ({self.iso_code})'

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.iso_code = self.iso_code.lower()
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop('user', None)
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
    )
    abbreviation = models.CharField(
        max_length=2,
        unique=True,
        blank=False,
        null=False,
        verbose_name=lng.LB_ABBREV,
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
        default='on',
        verbose_name=lng.LB_STATUS_CONTENT,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        'User',  # Circular relationship!
        related_name='updated_countries',
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    class Meta:
        db_table = 'user_country'
        ordering = ['name']
        verbose_name = 'User Country'
        verbose_name_plural = 'User Countries'

    def __str__(self):
        return f'{self.name} ({self.abbreviation})'

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.abbreviation = self.abbreviation.upper()
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop('user', None)
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
    )
    # TODO FIX: if someone has register your number. How to validate the number is yours...
    """owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=False,
        related_name='phone',
        verbose_name=lng.LB_OWNER,
    )"""
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name=lng.LB_CREATED_AT,
    )

    class Meta:
        db_table = 'user_phone'
        ordering = ['phone_id']
        verbose_name = 'User Phone'
        verbose_name_plural = 'User Phones'

    def __str__(self):
        # +55 (51) 980394586
        return f'+{self.country_code} ({self.region_code}) {self.number}'

    def save(self, *args, **kwargs):
        # Build the phone_id by concatenating the fields:
        self.phone_id = int(f'{self.country_code}{self.region_code}{self.number}')
        super().save(*args, **kwargs)



class User(AbstractUser):
    id = models.BigAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    profile_type = models.CharField(
        max_length=15,
        choices=CHOICES_PROFILE_TYPE,
        default='1',  # 1=Personal / 2=Business. Needed, e.g. when Django superuser is created.
        null=False,
        blank=False,
        verbose_name=lng.LB_PROFILE_TYPE,
        help_text=lng.TX_HELP_USER_PROFILE,
        error_messages={
            'blank': lng.TX_ERRO_USER_PROFILE_BLNK % {'txt': lng.LB_PROFILE_TYPE},
        },
    )
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name=lng.LB_USER_EMAIL,
        error_messages={
            'blank': lng.TX_ERRO_USER_EMAIL_BLNK % {'txt': lng.LB_USER_EMAIL},
            'invalid': lng.TX_ERRO_USER_EMAIL_INVLD,
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
        help_text=lng.TX_HELP_USER_LANG % {'txt': BRAND_NAME},
    )
    accepted_min_age = models.BooleanField(
        default=False,
        verbose_name=lng.LB_USER_AGE_MIN % {'val': VAL_PROFILE_1_BIRTH_MIN},
        help_text=lng.TX_HELP_USER_AGE_MIN % {'val': VAL_PROFILE_1_BIRTH_MIN},
        # error_messages in validators.py
    )
    accepted_our_privacy = models.BooleanField(
        default=False,
        verbose_name=lng.LB_USER_PRIVACY % {'txt': lng.S_G_PRIVACY_NAME},
        help_text=lng.TX_HELP_USER_PRIVACY % {'txt': lng.LB_USER_PRIVACY},
        # error_messages in validators.py
    )
    """last_pwd_update = models.DateField(
        editable=False,
        null=True,
        verbose_name=lng.LB_PWD_LAST_UPDATE,
    )"""
    # created_at = 'date_joined' from AbstractUser
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        'self',  # Itself relationship!
        related_name='updated_users',
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    class Meta:
        db_table = 'auth_user'
        ordering = ['username']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def clean(self):
        '''It's a built-in method for adding custom validation logic before saving data to the db.'''
        validate_user_agreement(self)

    def save(self, *args, **kwargs):
        '''Built-in method that's executed when the entry saving runs.'''
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop('user', None)  # Retrieve the user from kwargs!
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
        verbose_name=lng.LB_USER,
    )
    first_name = models.CharField(
        max_length=VAL_PROFILE_1_NAME_MAXLNGH,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_FNAME,
        error_messages={
            'max_length': lng.TX_ERRO_PROFILE_1_FNAME_MAXLNGH
            % {
                'txt': lng.LB_PROFILE_1_FNAME,
                'val': VAL_PROFILE_1_NAME_MAXLNGH,
            },
        },
    )
    last_name = models.CharField(
        max_length=VAL_PROFILE_1_NAME_MAXLNGH,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_LNAME,
        error_messages={
            'max_length': lng.TX_ERRO_PROFILE_1_LNAME_MAXLNGH
            % {
                'txt': lng.LB_PROFILE_1_LNAME,
                'val': VAL_PROFILE_1_NAME_MAXLNGH,
            }
        },
    )
    sex = models.CharField(
        max_length=20,
        choices=CHOICES_SEX,
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_1_SEX,
        help_text=lng.TX_HELP_PROFILE_1_SEX % {'txt': BRAND_NAME},
        error_messages={
            'blank': lng.TX_ERRO_PROFILE_1_SEX_BLNK % {'txt': lng.LB_PROFILE_1_SEX},
        },
    )
    birthdate = models.DateField(
        null=True,
        blank=True,
        verbose_name=lng.LB_PROFILE_1_BIRTHDATE,
        error_messages={
            'invalid': lng.TX_ERRO_PROFILE_1_BIRTH_INVLD,
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
            'blank': lng.TX_ERRO_PROFILE_1_COUNTRY_BLNK % {'txt': lng.LB_PROFILE_1_COUNTRY}
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
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        User,
        related_name='updated_profiles_1',
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    class Meta:
        db_table = 'user_profile_one'
        ordering = ['user', '-updated_at']
        verbose_name = 'Profile, Personal'
        verbose_name_plural = 'Profiles, Personal'

    def __str__(self):
        if self.user:
            if self.first_name and self.last_name:
                return f'{self.user.username} ({self.first_name} {self.last_name})'
            return self.user.username
        return lng.CMS_ERRO_PROFILE

    def clean(self):
        '''It's a built-in method for adding custom validation logic before saving data to the db.'''
        validate_birth(self.birthdate)

    def save(self, *args, **kwargs):
        if self.first_name:
            self.first_name = self.first_name.title()
        if self.last_name:
            self.last_name = self.last_name.title()
        if self.city:
            self.city = self.city.title()
        # Defining the user's birth year automatically:
        if self.birthdate:
            self.birth_year = str(self.birthdate)[:4]
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop('user', None)
        if user and user.is_authenticated and self.updated_by != user:
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
        verbose_name=lng.LB_USER,
    )
    business_name = models.CharField(
        max_length=VAL_PROFILE_2_BNAME_MAXLNGH,
        # unique=True,  # Commercial name must be flexible! Legal name, not!
        null=False,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_BNAME,
        help_text=lng.TX_HELP_PROFILE_2_BNAME,
        error_messages={
            'blank': lng.TX_ERRO_PROFILE_2_BNAME_BLNK % {'txt': lng.LB_PROFILE_2_BNAME},
            # 'unique': 'This business name already exists.'
            'max_length': lng.TX_ERRO_PROFILE_2_BNAME_MAXLNGH
            % {
                'txt': lng.LB_PROFILE_2_BNAME,
                'val': VAL_PROFILE_2_BNAME_MAXLNGH,
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
        error_messages={
            'blank': lng.TX_ERRO_PROFILE_2_LEGAL_BLNK % {'txt': lng.LB_PROFILE_2_LEGAL},
            'unique': lng.TX_ERRO_PROFILE_2_LEGAL_UNIQ,
            'max_length': lng.TX_ERRO_PROFILE_2_LEGAL_MAXLNGH
            % {
                'txt': lng.LB_PROFILE_2_LEGAL,
                'val': VAL_PROFILE_2_LEGAL_MAXLNGH,
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
            'blank': lng.TX_ERRO_PROFILE_1_COUNTRY_BLNK,
        },
    )
    city_business = models.CharField(
        max_length=VAL_PROFILE_2_CITY_MAXLNGH,
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_CITY,
        help_text=lng.TX_HELP_PROFILE_2_CITY,
        error_messages={
            'blank': lng.TX_ERRO_PROFILE_2_CITY_BLNK % {'txt': lng.LB_PROFILE_2_CITY},
            'max_length': lng.TX_ERRO_PROFILE_2_CITY_MAXLNGH
            % {
                'txt': lng.LB_PROFILE_2_CITY,
                'val': VAL_PROFILE_2_CITY_MAXLNGH,
            },
        },
    )
    description = models.TextField(
        max_length=VAL_PROFILE_2_DESC_MAXLNGH,
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_DESC,
        help_text=lng.TX_HELP_PROFILE_2_DESC,
        error_messages={
            'blank': lng.TX_ERRO_PROFILE_2_DESC_BLNK % {'txt': lng.LB_PROFILE_2_DESC},
            'max_length': lng.TX_ERRO_PROFILE_2_DESC_MAXLNGH
            % {
                'txt': lng.LB_PROFILE_2_DESC,
                'val': VAL_PROFILE_2_DESC_MAXLNGH,
            },
        },
    )
    business_url = models.URLField(
        blank=True,
        verbose_name=lng.LB_PROFILE_2_URL,
    )
    social_media = models.URLField(
        blank=True,
        verbose_name=lng.LB_PROFILE_2_URL_SOCIAL,
    )
    business_email = models.EmailField(
        null=True,
        blank=False,
        verbose_name=lng.LB_PROFILE_2_EMAIL,
        error_messages={
            'blank': lng.TX_ERRO_PROFILE_2_EMAIL_BLNK % {'txt': lng.LB_PROFILE_2_EMAIL},
            'invalid': lng.TX_ERRO_PROFILE_2_EMAIL_INVLD,
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
    contact_first_name = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=lng.LB_PROFILE_2_FNAME,
    )
    contact_last_name = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=lng.LB_PROFILE_2_LNAME,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=lng.LB_UPDATED_AT,
    )
    updated_by = models.ForeignKey(
        User,
        related_name='updated_profiles_2',
        on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
        null=True,
        verbose_name=lng.LB_UPDATED_BY,
        help_text=lng.TX_HELP_UPDATED_BY,
    )

    class Meta:
        db_table = 'user_profile_two'
        ordering = ['user', '-updated_at']
        verbose_name = 'Profile, Business'
        verbose_name_plural = 'Profiles, Business'

    def __str__(self):
        if self.user:
            if self.business_name:
                return f'{self.business_name} ({self.user.username})'
            return self.user.username
        return lng.CMS_ERRO_PROFILE

    def clean(self):
        '''It's a built-in method for adding custom validation logic before saving data to the db.'''
        pass

    def save(self, *args, **kwargs):
        if self.business_name:
            self.business_name = self.business_name.title()
        if self.legal_name:
            self.legal_name = self.legal_name.upper()
        if self.contact_first_name:
            self.contact_first_name = self.contact_first_name.title()
        if self.contact_last_name:
            self.contact_last_name = self.contact_last_name.title()
        if self.city_business:
            self.city_business = self.city_business.title()
        # Checking the updated_by:
        # Important: this need to be checked in admin.py and views.py as well!
        user = kwargs.pop('user', None)
        if user and user.is_authenticated and self.updated_by != user:
            self.updated_by = user
        super().save(*args, **kwargs)
