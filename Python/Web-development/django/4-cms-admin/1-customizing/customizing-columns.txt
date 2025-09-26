

CUSTOMIZING CMS COLUMNS:


    >> In case of admin.py files, any Admin Class created there WON'T affect database tables and
        their columns. Admin Classes stay in Django back-end level only.
    

    >> As any class in Python, Admin Class names must be written as PascalCase;


    >> If you want to add new html-table-columns in the CMS list-view and/or detail-view, and you
        already got least a Model class (in models.py), follow these steps:


        1) In that sub-app folder, open the 'admin.py' file;


        2) Import the Model Class you want to custom in the CMS interface:
            
            E.g. 
                # In case the models.py is in the same folder of admin.py:
                from .models import Recipe


        3) Create an Admin Class with a similar name of the original Model Class name you're
            working on:

            E.g. 
                class RecipeAdmin(admin.ModelAdmin):  # this 'Admin' in the classname is a convention.
                    # The tuple 'list_display' will reorder columns (attributes) on the CMS front-end:
                    list_display = (
                        'id',
                        'name',
                        'created_at',
                    )
                    # It activates the searching field and select which columns will be used as source:
                    search_fields = [
                        'name',
                        'description'
                    ]


        4) If the Model Class wasn't register yet, do it, adding also its Admin Class version:

            E.g.
                admin.site.register(Recipe, RecipeAdmin)


        5) (If applicable) If something was changed in the Model Class, update the db and stuff:
            
            $ python manage.py makemigrations
            $ python manage.py migrate
            or 
            $ uv run manage.py makemigrations
            $ uv run manage.py migrate


        6) Test the result:

            $ python manage.py runserver
            or
            $ uv run manage.py runserver
            
            http://localhost:8000/admin/




>> VERBOSE IN ADMIN LIST AND DETAIL VIEWS
    
    If you want to create a verbose-name for an CMS html table column, in the sub-app models.py,
    add the argument "verbose_name='<something>'" in the specific attribute of the specific
    Model Class you wanna customize:

        E.g. 
            class Recipe(models.Model):
                start_datetime = models.DateTimeField(
                    verbose_name='Start',
                )

