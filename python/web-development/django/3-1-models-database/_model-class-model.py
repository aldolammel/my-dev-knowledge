"""
    GET A MODEL CLASS TEMPLATE:
        1. Concrete Parent/Base class.
        2. Concrete Parent/Base with AuditMixin inheritance (RECOMMENDED!)
        3. Concrete Child class.
        4. Abstract Mixin class.
        5. Virtual model class.
"""

# 1. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.db import models
from django.utils.text import slugify
from . import consts, lang
#from django.forms import ValidationError
#from django.core.validators import MinLengthValidator,MaxLengthValidator
#from django.db.models.functions import Length
#models.CharField.register_lookup(Length)

"""
Model class model:
https://...
"""


class ExampleModel(models.Model):  # If it's a base model class, use in its class name a "Base" suffix!
    '''Stores xxxxxxxxxxxxxxxxxxxxxxx.'''

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=consts.VAL_GENERIC_MAX,
        unique=True,
        verbose_name="Name",
        help_text="",
        validators=[
            # MinLengthValidator(consts.VAL_GENERIC_MIN),
            # MaxLengthValidator(consts.VAL_GENERIC_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_GENERIC_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        db_index=True,
        editable=False,
        verbose_name="Slug",
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
                    <attrname>__length__range=(consts.VAL_GENERIC_MIN, consts.VAL_GENERIC_MAX)
                ),
                name="<classname>_<attrname>_length",
            ),
        ]"""

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        
        # Runs full validation before saving:
        self.full_clean()

        if self.name:
            # Creating the slug based in another field:
            self.slug = slugify(self.name)
            # Saving:
            super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # Nothing yet.


# 2. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.db import models
from django.utils.text import slugify
from core.models import AuditMixin
from . import consts, lang
#from django.forms import ValidationError
#from django.core.validators import MinLengthValidator,MaxLengthValidator
#from django.db.models.functions import Length
#models.CharField.register_lookup(Length)

"""
Model class model:
https://...
"""


class ExampleModel(AuditMixin):  # If it's a base model class, use in its class name a "Base" suffix!
    '''Stores xxxxxxxxxxxxxxxxxxxxxxx.'''

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=consts.VAL_GENERIC_MAX,
        verbose_name="name",
        help_text="",
        validators=[
            # MinLengthValidator(consts.VAL_GENERIC_MIN),
            # MaxLengthValidator(consts.VAL_GENERIC_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_GENERIC_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        db_index=True,
        editable=False,
        verbose_name="Slug",
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
                    <attrname>__length__range=(consts.VAL_GENERIC_MIN, consts.VAL_GENERIC_MAX)
                ),
                name="<classname>_<attrname>_length",
            ),
        ]"""

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        
        # Runs full validation before saving:
        self.full_clean()

        if self.name:
            # Creating the slug based in another field:
            self.slug = slugify(self.name)
            # Tracking the current user:
            user = kwargs.pop("user", None)
            if user and user.is_authenticated:
                if not self.created_by:
                    self.created_by = user
                else:
                    self.updated_by = user
            # Saving:
            super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # Nothing yet.


# 3. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.db import models
from django.utils.text import slugify
from . import consts, lang
#from django.forms import ValidationError
#from django.core.validators import MinLengthValidator,MaxLengthValidator
#from django.db.models.functions import Length
#models.CharField.register_lookup(Length)

"""
Model class model:
https://...
"""

class ExampleChildModel(ExampleModel):
    '''Stores xxxxxxxxxxxxxxxxxxxxxxx.'''

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=consts.VAL_GENERIC_MAX,
        unique=True,
        verbose_name="Name",
        help_text="",
        validators=[
            MinLengthValidator(consts.VAL_GENERIC_MIN),
            MaxLengthValidator(consts.VAL_GENERIC_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_GENERIC_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        db_index=True,
        editable=False,
        verbose_name="Slug",
        help_text=""
    )

    class Meta:
        db_table = "xxxxxxxx"
        ordering = ["xxxxxx"]
        verbose_name = "x. xxxxxxx"
        verbose_name_plural = "x. xxxxxxxxxxxxxxx"
        """constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    <attrname>__length__range=(consts.VAL_GENERIC_MIN, consts.VAL_GENERIC_MAX)
                ),
                name="<classname>_<attrname>_length",
            ),
        ]"""

    def __str__(self):
        return self.name

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


# 4. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.conf import settings

"""
Model class model:
https://...
"""

class AuditMixin(models.Model):  # Abstract model!
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



# 5. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# E.g. /python/web-development/django/3-1-models-database/model-type-virtual.py

