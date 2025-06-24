

CMS DETAIL-VIEW: HOW TO CLONE BEHAVIORS FROM A FRONT-END FORM


    from .forms import MovieForm

    class MovieCMS(admin.ModelAdmin):
        form = MovieForm  # cloning the form behavior like required fields.

        list_display = (
            'name',
            'year_released',
            'director',
        )
        readonly_fields = (
            'created_by',
        )
        exclude = ('language',)