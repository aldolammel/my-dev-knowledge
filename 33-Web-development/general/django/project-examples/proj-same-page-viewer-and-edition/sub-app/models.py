from django.db import models


# Create your models here.
class Movie(models.Model):
    name = ...
    released_year = ...
    director = ...
    rating = ...

    def __str__(self):
        return f'{self.name} ({self.released_year})'


"""
    MORE OPTIONS:
    /33-Web-development/general/django/3-1-backend-models-database/

"""
