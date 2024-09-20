

FIELD EXCLUSION FROM THE CMS:

    >> To make a field/attribute be available only in the database, not in list-view and 
        detail-view, go to the sub-app 'admin.py' file and:

            class MovieCMS(admin.ModelAdmin):
                exclude = ('full_name',)
                