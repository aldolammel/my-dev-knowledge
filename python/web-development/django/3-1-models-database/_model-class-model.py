"""
    WHICH MODEL CLASS TEMPLATE YOU WANT?
        1. Concrete common/Parent class.
        2. Concrete child class.
        3. Abstract AuditBase class.
        4. Concrete common with AuditBase inheritance
        5. Virtual model class.
"""

# 1. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.db import models
from django.utils.text import slugify
from . import consts

class ExampleModel(models.Model):
    '''Stores xxxxxxxxxxxxxxxxxxxxxxx.'''

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name_xxxxxx = models.CharField(
        max_length=consts.VAL_XXXXXXXXX_MAX,
        unique=True,
        verbose_name="XXXXXXX",
        help_text="",
        validators=[
            MinLengthValidator(consts.VAL_XXXXXXX_MIN),
            MaxLengthValidator(consts.VAL_XXXXXXXXXX_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_PAGE_TITLE_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        db_index=True,
        editable=False,
        verbose_name="xxxxx",
        help_text="",
    )

    class Meta:
        db_table = "xxxxxxxx"
        ordering = ["xxxxxx"]
        verbose_name = "x. xxxxxxx"
        verbose_name_plural = "x. xxxxxxxxxxxxxxx"
        """constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    xxxxxxx__length__range=(consts.VAL_XXXXXXX_MIN, consts.VAL_XXXXXXXXXX_MAX)
                ),
                name="xxxxxxx_length",
            ),
        ]"""

    def __str__(self):
        return self.xxxxxxxx

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        
        # Runs full validation before saving:
        self.full_clean()

        if self.name_xxxxxx:
            self.slug = slugifier(self.name_xxxxxx)
            super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # Nothing yet.



# 2. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.db import models
from django.utils.text import slugify
from . import consts

class ExampleModel(models.Model):
    '''Stores xxxxxxxxxxxxxxxxxxxxxxx.'''

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name_xxxxxx = models.CharField(
        max_length=consts.VAL_XXXXXXXXX_MAX,
        unique=True,
        verbose_name="XXXXXXX",
        help_text="",
        validators=[
            MinLengthValidator(consts.VAL_XXXXXXX_MIN),
            MaxLengthValidator(consts.VAL_XXXXXXXXXX_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_PAGE_TITLE_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        db_index=True,
        editable=False,
        verbose_name="xxxxx",
        help_text=""
    )

    class Meta:
        db_table = "pagex_xxxxxxxx"
        ordering = ["xxxxxx"]
        verbose_name = "x. xxxxxxx"
        verbose_name_plural = "x. xxxxxxxxxxxxxxx"
        """constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    xxxxxxx__length__range=(consts.VAL_XXXXXXX_MIN, consts.VAL_XXXXXXXXXX_MAX)
                ),
                name="xxxxxxx_length",
            ),
        ]"""

    def __str__(self):
        return self.xxxxxxxx

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # Reserved space for child saving logic...
        # Saving data (including changes in parent via this child) in the db:
        super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # Allows the parent class to execute full_clean() in this child too:
        super().clean()
        # Validations before saving:
        # Reserved space for child validations...


# 3. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.conf import settings

class AuditBase(models.Model):  # Abstract model!
    """Stores who and when things were changed."""

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=lang.lbl_created_at,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_created_by",
        editable=False,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=lang.lbl_created_by,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=lang.lbl_updated_at,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_updated_by",
        editable=False,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=lang.lbl_updated_by,
    )

    class Meta:
        abstract = True  # Flags to the db that no tables should be created from this.


# 4. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.db import models
from django.utils.text import slugify
from . import consts

class ExampleModel(AuditBase):
    '''Stores xxxxxxxxxxxxxxxxxxxxxxx.'''

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    xxxxxx = models.CharField(
        max_length=consts.VAL_XXXXXXXXX_MAX,
        verbose_name="XXXXXXX",
        help_text="",
        validators=[
            MinLengthValidator(consts.VAL_XXXXXXX_MIN),
            MaxLengthValidator(consts.VAL_XXXXXXXXXX_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )

    class Meta:
        db_table = "xxxxxxxx"
        ordering = ["xxxxxx"]
        verbose_name = "x. xxxxxxx"
        verbose_name_plural = "x. xxxxxxxxxxxxxxx"
        """constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    xxxxxxx__length__range=(consts.VAL_XXXXXXX_MIN, consts.VAL_XXXXXXXXXX_MAX)
                ),
                name="xxxxxxx_length",
            ),
        ]"""

    def __str__(self):
        return self.xxxxxx

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        
        # Runs full validation before saving:
        self.full_clean()

        if self.xxxxxx:
            # Tracking the current user:
            user = kwargs.pop("user", None)
            if user and user.is_authenticated:
                if not self.created_by:
                    self.created_by = user
                else:
                    self.updated_by = user
            super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # Nothing yet.


# 5. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# E.g. /python/web-development/django/3-1-models-database/model-type-virtual.py

