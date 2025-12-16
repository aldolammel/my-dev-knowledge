
"""
    ADDING AUDIT FIELDS (WITH AUTO-FILL)
                
        >> If you wanna add audit fields (auto-fill) to control content changes through CMS:
"""


# FILE: /core/settings.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # /Python/Web-development/django/3-1-models-database/3-users/0-users-setup.txt


# FILE: /apps/my_app/models.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.conf import settings as stgs

class AuditBase(models.Model):
    """Stores who and when things were changed."""

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Instalado em",
    )
    created_by = models.ForeignKey(
        stgs.AUTH_USER_MODEL,
        editable=False,
        related_name="pages",
        on_delete=models.SET_NULL,
        null=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )
    updated_by = models.ForeignKey(
        stgs.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_updated_by",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Atualizado por",
    )

    class Meta:
        abstract = True  # Flags the db to don't create this table!

class PageModel(AuditBase):
    attr_1 = ...
    attr_2 = ...

    # How model inheritance works:
    # /Python/Web-development/django/3-1-models-database/Inheriting-common-attributes.txt

    def save(self, *args, **kwargs):
        """Built-in method that's executed when the entry saving runs."""
        
        # Retrieve the user from kwargs, default to None if not passed:
        user = kwargs.pop("user", None)
        if self.something_exist_an_important_field:
            ...
            # Audit records:
            if user:
                if not self.pk:
                    self.created_by = user
                # Otherwise, set updated_by:
                elif user.is_authenticated:
                    self.updated_by = user
            # Save instance:
            super().save(*args, **kwargs)


# FILE: /apps/my_app/admin.py

@admin.register(PageModel)
class PageModelAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    )

    def save_model(self, request, obj, form, change):
        """Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)