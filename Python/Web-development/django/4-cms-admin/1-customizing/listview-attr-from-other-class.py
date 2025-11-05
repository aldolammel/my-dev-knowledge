

"""
    ATTRIBUTE FROM OTHER CLASS: SHOWING IN A LIST-VIEW
    
        What is a list-view:
            /Python/Web-development/django/4-cms-admin/_about.txt
    
"""


    # In the sub-app admin.py:

        # Example:
        from django.contrib import admin
        
        class UserProfileCMS(admin.ModelAdmin):
            
            list_display = (
                'id',
                'user',
                'first_name',  # Custom method field from other class
                'age',
                'sex',
                'country',
                'last_login',  # Custom method field from other class
            )

            # To custom the queryset of something in list_filter():
            # ./listview-model-option-list_filter.py

            # Declaring a existent method from another class:
            def first_name(self, obj):
                return obj.user.first_name

            # Declaring a existent method from another class:
            def last_login(self, obj):
                return obj.user.last_login


            # Custom methods above are fields that AREN'T listed as UserProfile attributesin sub-app models.py file. These custom methods are coming from the Django built-in class called 'User'.
