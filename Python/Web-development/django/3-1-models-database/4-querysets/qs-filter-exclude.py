
"""
    DJANGO MODELS > QUERYSETS: EXCLUDE FILTERING

        >> What is it:
            ./_what-is-queryset.txt

        >> Here we will see:
            1. Declaring a QuerySet for Models (models.py);
            2. Declaring a QuerySet for Forms (forms.py);
            3. Calling the QuerySet method for CMS (admin.py);
"""


# 1. QUERYSETS FOR MODELS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# /apps/my_app/models.py:


class Movie(models.Model):
    title = ...
    category = ...
    status = ...

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""

        # Check if other movie has the same title but using case-insensitive:
        is_same_title = Movie.objects.exclude(pk=self.pk).filter(title__iexact=self.title).exists()
        if is_same_title:
            raise ValidationError(f"At least another movie has the same title as this one.")
        

# 2. QUERYSETS FOR FORMS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# /apps/my_app/forms.py:     

class MovieForm(forms.ModelForm):
    class Meta:
        # Connected model:
        model = Movie
        # Ordering fields on the form:
        fields = [
            'category',  # from connected model
            'country',  # extra
        ]

    # Extra fields:
    country = forms.ModelChoiceField(
        queryset=Country.objects.filter(status='on'),  # Assuming there's a Country model.
        required=False,
    )

    def __init__(self, *args, **kwargs):
        '''Built-in method called 'Constructor', designed to initialize the instance.'''
        super().__init__(*args, **kwargs)
        
        # Connected fields (from connected model), customizations:
        self.fields['category'].queryset = Category.objects.filter(status='on')

        # Extra fields, pre-populating:
        # Unlike fields from connected model, extra fields must be manually linked!
        self.fields['country'].initial = user.country


# More:
# /Python/Web-development/django/9-forms/form-queryset-filtering-dropdown.py



# 3. QUERYSETS FOR ADMIN (CMS) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# /apps/my_app/admin.py:

class MovieCMS(admin.ModelAdmin):
    ...

    def get_queryset(self, request):
        """Built-in method for Admin (CMS)."""
        return super().get_queryset().exclude(status='off')


# More:
# /Python/Web-development/django/4-cms-admin/customizing/detailview-filtering-any-data.py


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


"""
    AWARE: 
        When an entry-queried is flagged as 'archived' for example, everything that had the entry-queried as part of its data, won't show the entry-queried anymore, but it the entry-queried is 'active' again, the entry-queried turn visible back to all entry that entry-queried belonged.
"""