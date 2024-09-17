"""
    REMOVING CMS PERMISSION: TO DELETE AN ENTRY
    
    Case:

        Let's imagine you want to see each entry of UserProfile listed on the CMS but
        no one must delete a UserProfile entry manually through the CMS, leaving the deletion task
        for the 'on_delete' argument configured as 'CASCADE' in UserProfile model-class (models.py) 
        if the related User (built-in class linked with that UserProfile entry) is deleted.
        
        >> More about the model argument 'on_delete':
            /33-Web-development/general/django/3-1-backend-models-database/_model-arguments.txt

"""

from django.contrib import admin
from .models import UserProfile


class UserProfileCMS(admin.ModelAdmin):

    # Remove the delete action (bulk) from the list-view:
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    # Remove all CMS capacity to delete a UserProfile entry, removing buttons and hyperlinks too:
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(UserProfile, UserProfileCMS)
