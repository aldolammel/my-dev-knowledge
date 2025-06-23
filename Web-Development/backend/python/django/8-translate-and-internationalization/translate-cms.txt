

    TRANSLATING: DYNAMIC INFORMATION ON THE CMS


        1) Open the 'admin.py' file from the specific sub-app:


        2) Adapting the Admin-classes:
        
            >> Model-class with NO CMS customs:

                from django.contrib import admin
                from .models import Movie
                from parler.admin import TranslatableAdmin

                admin.site.register(Movie, TranslatableAdmin)


            >> Model-class with CMS customs:

                from django.contrib import admin
                from .models import Movie
                from parler.admin import TranslatableAdmin

                @admin.register(Movie)
                class MovieCMS(TranslatableAdmin):
                    list_display = (
                        'title',
                        'country',
                        'year',
                    )




        3) 'list_filter' and 'search_fields' with translatable content:

            E.g.

                @admin.register(Movie)
                class MovieCMS(TranslatableAdmin):
                    ...

                    list_filter = (
                        'translations__country',  # it shows the country as a multilanguage filter.
                    )

                    search_fields = [
                        'translations__title__icontains',  # search the expression (case-insensitive) through all titles in all languages.
                    ]




            >> If you are dealing with some kind of ForeignKey:

                >> In this case, you call the local attribute that is hooked with the original model,
                    and then you set the translation address as you were in the original model:


                        E.g. models.py

                            class Crew(TranslatableModel):        <-- the 'original' model!
                                ...
                                translations = TranslatedFields(
                                    role=models.CharField(
                                        ...
                                    )
                                )
                            
                            class Movie(models.Model):
                                ...
                                team = models.ManyToManyField(    <-- the 'local' attribuite hooked.
                                    Crew,
                                    ...
                                )


                        E.g. admin.py

                            @admin.register(Movie)
                            class MovieCMS(admin.ModelAdmin):
                                ...

                                list_filter = (
                                    '', 
                                )

                                search_fields = [
                                    'team__translations__role__icontains',  
                                ]
