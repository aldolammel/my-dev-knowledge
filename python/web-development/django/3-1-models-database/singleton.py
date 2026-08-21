"""
    SINGLETON: CREATION WITH DJANGO (STEP 1/3)

    >> What is it:
        /dev-concepts/singleton.md

    >> This file:
        /django_project/apps/your_app/models.py

    >> Step 1/3 (models.py):
        This file!

    >> Step 2/3 (admin.py)
        /python/web-development/django/4-cms-admin/singleton.py

    >> Step 3/3 (signals.py & apps.py)
        /python/web-development/django/7-middlewares-and-signals/signals/seeding-singleton.md
"""

# subapp/models.py:


class PagexSettings(models.Model):
    """Stores global settings for the Pagex sub-app. This is a singleton!"""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )

    ...

    class Meta:
        db_table = "pagex_settings"
        verbose_name = "Configurações do Pagex"
        verbose_name_plural = "Configurações do Pagex"

    def __str__(self):
        return "Configurações do Pagex"

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # Runs full validation before saving:
        self.full_clean()
        # Never shows adding page for settings if there's already one instance (Singleton):
        if not self.pk and PagexSettings.objects.exists():
            return PagexSettings.objects.first()
        try:
            # Everything should be done in save() act!
            # ...
            # Tracking the current user:
            # ...
            # Saving the singleton:
            super().save(*args, **kwargs)
        # If signals' create_pagex_singleton method to fail, create it:
        except PagexSettings.DoesNotExist:
            super().save(*args, **kwargs)
    
    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # validation stuff:
        # ...

    @classmethod
    def get_settings(cls):
        """Get or create settings object."""
        settings, create = cls.objects.get_or_create(pk=1)
        return settings