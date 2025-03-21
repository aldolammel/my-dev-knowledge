
"""
    REGISTERING A SUB-APP MODEL (TABLE) TO BE MANAGED BY DJANGO CMS:


"""

    # Management without customization:

        # 1) In the sub-app folder, open the 'admin.py':
            
            from django.contrib import admin
            # Import the specific model/table of the sub-app:
            from .models import Movie
            
            # Registering Django CMS customizations:
            # Reserved space...
            # Registering Product CMS features:
            admin.site.register(Movie)

        # 2) Check the result: http://localhost:8000/admin/




    # Management with customization:

        # 1) In the sub-app folder, open the 'admin.py':

            # Import the parent class needed for customizations:
            from django.contrib import admin
            # Import the specific model/table of the sub-app:
            from .models import Movie # type: ignore # the original model  

            # Create an Admin class that will be responsable for all customization of the
            # original model from models.py:
            class MovieCMS(admin.ModelAdmin):  # this 'CMS' or 'Admin' in classname is convension.
                # Each specifically fields will be visible on CMS movies list-view:
                list_display = (
                    # these fields right below are known because you are creating a 'relation'
                    # with the 'Movie' class when you declare 'admin.site.register(Movie, MovieCMS):
                    'title', 
                    'director', 
                    'year_released',
                    # To call fields from a 'non-connected' class, you might use a prefix with
                    # the class name, making the prefix separed by double underscore:
                    'user__first_name',
                )
        
            # Unlike the first example, to register a customized model for CMS, you must to 'link'
            # the original model with its cusmotized version for Django CMS: 
        
            # Registering Django CMS customizations:
            # Reserved space...
            # Registering Product CMS features:
            admin.site.register(Movie, MovieCMS)
        
        # 2) Check the result: http://127.0.0.1:8000/admin/

