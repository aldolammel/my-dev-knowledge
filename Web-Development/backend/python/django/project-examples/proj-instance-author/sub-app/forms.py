from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_title']

    def save(self, user, *args, **kwargs):
        instance = super().save(commit=False)
        if not instance.pk:  # New movie
            instance.created_by = user
        instance.updated_by = user
        instance.save()
        return instance
