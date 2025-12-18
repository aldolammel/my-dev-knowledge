"""
    SINGLETON: CREATION WITH DJANGO (STEP 1/2)

    >> What is it:
        /Programming-Concepts/singleton.txt

    >> This file:
        /django_project/apps/your_app/models.py

    >> Step 1/2 (models.py):
        This file!

    >> Step 2/2 (admin.py)
        /Python/Web-development/django/4-cms-admin/singleton.py
"""

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
        # Runs full validation before saving:
        self.full_clean()
        # Ensure there's only one settings instance (Singleton):
        if not self.pk and PagexSettings.objects.exists():
            return PagexSettings.objects.first()

    @classmethod
    def get_settings(cls):
        """Get or create settings object."""
        settings, create = cls.objects.get_or_create(pk=1)
        return settings