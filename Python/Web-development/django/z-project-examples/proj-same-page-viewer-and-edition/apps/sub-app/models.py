from django.db import models


class Movie(models.Model):
    name = ...
    released_year = ...
    director = ...
    rating = ...

    class Meta:
        db_table = 'movie'
        ordering = ['name', '-released_year']
        # verbose_name = 'Movie'
        # verbose_name_plural = 'Movies'

    def __str__(self):
        return f'{self.name} ({self.released_year})'

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.director = self.director.lower()
        super().save(*args, **kwargs)


"""
    MORE OPTIONS:
    /Python/Web-development/django/3-1-models-database/

"""
