"""
    ATTRIBUTE FROM OTHER CLASS: SHOWING IN A DETAIL-VIEW
    
        >> What is a detail-view:
        
            /Python/Web-development/django/4-cms-admin/_about.txt
            
        
        >> Different approach between Custom Model and Built-in Model:
        
            There are 2 ways to customize a CMS detail-view where one of them is specific for
            detail-view from a custom model, and the other one specifically for detail-view from
            a built-in Django model class.
    
"""


    # FOR DETAIL-VIEW BASED IN A CUSTOM MODEL CLASS:
    # In the sub-app admin.py:

        # Example:
        from django.contrib import admin
        
        class UserProfileCMS(admin.ModelAdmin):
            
            readonly_fields = (
                'user',
                'first_name',  # imported from User model class!
                'last_login',  # imported from User model class!
            )

            # Importing field from User model class:
            def first_name(self, obj):
                return obj.user.first_name

            # Importing field from User model class:
            def last_login(self, obj):
                return obj.user.last_login


            # Custom methods above are fields that AREN'T listed as UserProfile attributes
            # in sub-app models.py file. These custom methods are coming from the
            # Django built-in class called 'User'.
            
            
            
            
    # FOR DETAIL-VIEW BASED IN A BUILT-IN MODEL CLASS:
    # In the sub-app admin.py:

    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from django.conf import settings as stgs
    from django.utils.html import format_html
    from django.urls import reverse


    # Adding a link to UserProfile in the Django Built-in UserAdmin:
    class CustomUserAdmin(UserAdmin):
        list_display = (
            #...,
            'profile_link',  # The custom field !!!
        )
        # Adding the UserProfile in the User detail-view:
        fieldsets = (
            #...
            (
                'Personal info',
                {
                    'fields': (
                        'first_name',
                        'last_name',
                        'profile_link',  # The custom field !!!
                    )
                },
            ),
            #...
        )

        def profile_link(self, obj):
            if hasattr(obj, 'profile'):
                url = reverse('admin:accounts_userprofile_change', args=[obj.profile.id])
                return format_html('<a href="{}">More details</a>', url)
            return "ERROR: no profile for this user!"

        profile_link.short_description = 'User Profile'

        # It's mandatory call this, 'cause it's not possible to edit here an attr from another table:
        def get_readonly_fields(self, request, obj=None):
            # Make profile_link readonly in the detail-view:
            return super().get_readonly_fields(request, obj) + ('profile_link',)  # type: ignore


    # Django CMS customs:
    admin.site.unregister(stgs.AUTH_USER_MODEL)
    admin.site.register(stgs.AUTH_USER_MODEL, CustomUserAdmin)
    # Product CMS features:
    # ...