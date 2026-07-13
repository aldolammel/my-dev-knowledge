from django import forms
from . import models

class MovieForm(forms.ModelForm):
    class Meta:
        # Model tied used to populate it:
        model = models.Movie
        # Bringing specific fields from the model:
        # Django rule: to be called here, the field CANNOT be 'editable=False', nor custom method. If the field is editable but for the form it should be readonly_fields, no problem, call it!
        fields = [
            'movie_title',
        ]

    def save(self, user, *args, **kwargs):
        instance = super().save(commit=False)
        if not instance.pk:  # New movie
            instance.created_by = user
        instance.updated_by = user
        instance.save()
        return instance
