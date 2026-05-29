from django.db import models
from django.conf import settings as stgs

class Movie(models.Model):
    movie_title = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(stgs.AUTH_USER_MODEL, editable=False, related_name='movies_created', on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(stgs.AUTH_USER_MODEL, editable=False, related_name='movies_updated', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_title
