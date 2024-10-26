from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'movie_title',
        'created_by',
        'updated_by',
    )
    readonly_fields = (
        'created_by',
        'updated_by',
        'created_at',
        'updated_at',
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # New movie
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
