#### Python > Django > CMS
# Detail-view listing inline instances from another model class

---

Regardless new or existing object, you wanna see an *inline* table where every row comes from another model class object. You must add and/or remove each row if needed. 

![/web-development/frontend/css/css-examples/django-css-zebra-striping-for-admin-inline.png](/web-development/frontend/css/css-examples/django-css-zebra-striping-for-admin-inline.png)

Important: both models are tied for the database.

For example where data is not tied between each other:  /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx (PagexPage and its PagexContent instances - for future example!)

---
# In `models.py`:
```python
# Example context: each movie detail-view has a list of its casting actors. For new movies, the casting list has a button to add them. If a movie is deleted, nothing happen with actors. If an actor is permanently removed from the db, all movies that actor was tied lost that relation.

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


```

---
# In `forms.py`:
```python
class CastingForm(forms.ModelForm):
    class Meta:
        model = models.Casting
        # Bringing specific fields from the model:
        # Django rule: to be called here, the field CANNOT be 'editable=False', nor custom method. If the field is editable but for the form it should be readonly_fields, no problem, call it!
        fields = "__all__" # Automatically remove fields editable=False!


```

---
# In `admin.py`:
```python
@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    ...


class MovieCastingInline(admin.StackedInline):
    model = models.Casting
    fk_name = "actor"  # to flag what Foreignkey (attr) is the the main one for this inline class case the model class has more than one foreignekey.
    form = forms.CastingForm
    extra = 0


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieCastingInline]

    # def get_inline_instances(self, request, obj=None):
    #     """Built-in admin method that returns the inline model admin instances to be displayed on another model's admin page."""
    #
    #     # /python/web-development/django/4-cms-admin/method-get_inline_instances.md
    #     # ...
```

---
## Making zebra striping color in an inline table:
[/web-development/frontend/css/css-examples/zebra-striping](/web-development/frontend/css/css-examples/zebra-striping.md)

