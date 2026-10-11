from django.conf import settings
from django.db import models

from . import consts, lang


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
