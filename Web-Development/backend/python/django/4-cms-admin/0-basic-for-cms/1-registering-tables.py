
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




    # Management with customization (METHOD 1):
    # In this method, you register each CMS customized model at the admin.py footer at once!

        # 1) In the sub-app folder, open the 'admin.py':

            # Import the parent class needed for customizations:
            from django.contrib import admin
            # Import the specific model/table of the sub-app:
            from .models import Movie

            # Create an Admin class that will be responsable for all customization of the
            # original model from models.py:
            class MovieAdmin(admin.ModelAdmin):  # 'Admin' in classname is convension for CMS.
                # Each specifically fields will be visible on CMS movies list-view:
                list_display = (
                    # these fields right below are known because you are creating a 'relation'
                    # with the 'Movie' class when you declare 'admin.site.register(Movie, MovieCMS):
                    'title', 
                    'director', 
                    'year_released',
                    
                    # List_display accept imported fields using prefix and imported method (prefix recommended):
                    'user__first_name',  # Calling field from a 'non-connected' class!
                )
        
            # Unlike the first example, to register a customized model for CMS, you must to 'link'
            # the original model with its cusmotized version for Django CMS: 
        
            # Registering the CMS models customizations:
            admin.site.register(Movie, MovieAdmin)
            ...
        
        # 2) Check the result: http://localhost:8000/admin/
        
        
        
        
    # Management with customization (METHOD 2, RECOMMENDED):
    # In this method, you register the CMS customized model using a decorator!
    
        # 1) In the sub-app folder, open the 'admin.py':
        
            # Import the parent class needed for customizations:
            from django.contrib import admin
            # Import the specific model/table of the sub-app:
            from .models import Movie
        
        
            @admin.register(Movie)  # Registering the CMS customized model!
            class MovieAdmin(admin.ModelAdmin):  # 'Admin' in classname is convension for CMS.
                ...

        # 2) Check the result: http://localhost:8000/admin/
