from django.contrib.auth import get_user_model
from django.db import models

#from . import constants as consts

# Defining the User model with Django default solution:
User = get_user_model()

"""
class ExampleModel(models.Model):
    '''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''
    
    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=100,
        verbose_name="xxxxxxxxx",
        help_text="xxxxxxxxxxxxxxxxxxxxxxxx",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )
    updated_by = models.ForeignKey(
        User,
        related_name="updated_layouts",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Atualizado por",
    )
    class Meta:
        db_table = "xxxxx_xxxxx"
        ordering = ["name"]
        verbose_name = "xxxxxxxxx"
        verbose_name_plural = "xxxxxxxx"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        '''Built-in method that's executed when the entry saving runs.'''
        if self.name:
            self.name = self.name.strip().title()
            self.slug = slugify(self.name)
            # Register who's modifying this:
            user = kwargs.pop("user", None)
            if user and user.is_authenticated and user != self.updated_by:
                self.updated_by = user
            super().save(*args, **kwargs)
"""
