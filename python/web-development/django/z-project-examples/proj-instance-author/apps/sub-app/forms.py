from django import forms
from . import models

class MovieForm(forms.ModelForm):
    class Meta:
        # Model tied to populate:
        model = models.Movie
        # Bringing specific fields from the model:
        # Django rule: to be called here, the field CANNOT be 'editable=False'. If the field is editable but for the form it should be readonly_fields, no problem, you can called here!
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
