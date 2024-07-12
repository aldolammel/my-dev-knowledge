

# CREATING A DATABASE TABLE WITH DJANGO


""" 
    In Django, you define everything about your project database through
    the files called 'models.py'. Your project (also called 'main app') 
    can have one or more sub-apps that are where the all models.py are
    allocated.


    First, make sure you already got a sub-app. If not, create one:
    /33-Web-development/general/django/2-creating-and-deleting-apps/


    Into your sub-app folder, open the models.py file and let's create
    a table called 'Movie' with two attributes (they will be colunms
    of the table):
"""


class Movie(models.Model):
    title = models.CharField(max_length=40, unique=True, blank=False)
    released_year = models.PositiveIntegerField(blank=False)

    class Meta:
        # This will rename the default name django would give (<subapp_name>_<table_name>):
        db_table = 'movie'

    def __str__(self):
        # This will override the original object name to something more readable:
        return f'{self.title} ({self.released_year})'

