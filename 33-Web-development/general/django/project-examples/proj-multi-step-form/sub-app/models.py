from django.db import models
from django.contrib.auth.models import User

# CONSTANTS
RATING = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

DONE = 'true'
DRAFT = 'false'
IS_DONE = ((DONE, 'Done'), (DRAFT, 'Draft'))


class Movie(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=False)
    released_year = models.PositiveIntegerField(blank=True)
    director = models.CharField(max_length=40, blank=True)
    rating = models.CharField(max_length=40, choices=RATING, blank=True)
    status = models.CharField(
        max_length=10,
        choices=IS_DONE,
        default=DRAFT,
        editable=False,
    )
    created_by = models.ForeignKey(
        User,
        related_name='created_movies',
        on_delete=models.SET_NULL,
        null=True,
        # editable=False,
    )

    class Meta:
        db_table = 'movie'
        ordering = ['name', '-released_year']
        # verbose_name = 'Movie'
        # verbose_name_plural = 'Movies'

    def __str__(self):
        return f'{self.name} ({self.released_year})'

    def delete_instance(self):
        self.delete()

    # def save(self, *args, **kwargs):
    # ...
    # super().save(*args, **kwargs)


"""
    MORE OPTIONS:
    /33-Web-development/general/django/3-1-backend-models-database/

"""
