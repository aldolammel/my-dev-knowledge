
""" 
    DJANGO: CREATING A DATABASE TABLE THROUGH MODELS.PY
    
    In Django, you define everything about your project database through the files called 'models.py'. Your project (also called 'main app') can have one or more sub-apps that are where the all models.py are allocated.

    >> First, make sure you already got a sub-app. If not, create one:
        /Python/Web-development/django/2-creating-and-deleting-apps/

    Into your sub-app folder, open the models.py file and let's create a table called 'Movie' with two attributes (they will be colunms of the table):
"""

# FILE: e.g. /project_folder/apps/my_app/models.py

class Movie(models.Model):
    """This table stores all the movies available through the app."""
    
    title = models.CharField(
        max_length=40,
        unique=True,
        blank=False,
    )
    released_year = models.PositiveIntegerField(blank=False)

    class Meta:
        # This will rename the default name django would give (<subapp_name>_<table_name>):
        db_table = "movie_film_video"

    def __str__(self):
        # This will override the original object name to something more readable:
        return f'{self.title} ({self.released_year})'


class ExampleModel(models.Model):
    """Always describe here what this class do in the app xxxxxxxxxxxxxxxxxxxxxx."""
    
    id = models.SmallAutoField(  # Django auto-creates id attr, but's good to choose what fit better
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(            # Defining the atribute 'name' as a Char field.
        max_length=100,
        unique=True,                    # Optional
        blank=False,                    # Optional
        nullable=False,                 # Optional
    )

    class Meta:
        db_table = "example_only"                # Optional
        ordering = ["name"]                      # Optional
        verbose_name = "Bla Bla bla"             # Optional
        verbose_name_plural = "Bla Bla blases"   # Optional

    def __str__(self):
        # return self.name  # simplest
        return f"{self.name} (id-{self.pk})"