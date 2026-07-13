"""
    DJANGO CMS: DETAIL-VIEW LISTING INLINE ENTRIES FROM ANOTHER MODEL CLASS

    Regardless new or existing object, you wanna see an *inline* table where every row comes from another model class object. You must add and/or remove each row if needed. Important: both models are tied for the database.

    For example where data is not tied between each other:
        /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx (PagexPage and its PagexContent instances)
"""

# Example context: each movie detail-view has a list of its casting actors. For new movies, the casting list has a button to add them. If a movie is deleted, nothing happen with actors. If an actor is permanently removed from the db, all movies that actor was tied lost that relation.

# models.py - - - - - - - - - - - - - - - -

class Movie(models.Model):
    title = models.CharField(max_length=80)

class Actor(models.Model):
    name = models.CharField(max_length=80)

class Casting(models.Model):
    movie = models.ForeignKey(
        "Movie",
        on_delete=models.CASCADE,       # delete movie → its casting rows vanish too.
        related_name="castings",
        null=True,
        blank=True,
    )
    actor = models.ForeignKey(
        "Actor",
        on_delete=models.SET_NULL,      # delete actor → casting row stays, actor ref becomes NULL.
        related_name="castings",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.actor} in {self.movie}"



# forms.py - - - - - - - - - - - - - - - - 

class CastingForm(forms.ModelForm):
    class Meta:
        model = models.Casting
        # Bringing specific fields from the model:
        # Django rule: to be called here, the field CANNOT be 'editable=False', nor custom method. If the field is editable but for the form it should be readonly_fields, no problem, call it!
        fields = "__all__" # Automatically remove fields editable=False!


# admin.py - - - - - - - - - - - - - - - - 

@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    ...

class MovieCastingInline(admin.StackedInline):
    model = models.Casting
    form = forms.CastingForm
    extra = 0

@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieCastingInline]