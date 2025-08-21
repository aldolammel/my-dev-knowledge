"""
    REMOVING CMS PERMISSION: TO DELETE AN ENTRY
    
    Case:

        Let's imagine you want to see each entry of UserProfile listed on the CMS but
        no one must delete a UserProfile entry manually through the CMS, leaving the deletion task
        for the 'on_delete' argument configured as 'CASCADE' in UserProfile model-class (models.py) 
        if the related User (built-in class linked with that UserProfile entry) is deleted.
        
        >> More about the model argument 'on_delete':
            /Python/Web-development/django/3-1-backend-models-database/_model-arguments.txt

"""

from django.contrib import admin
from .models import UserProfile  # type: ignore


class UserProfileCMS(admin.ModelAdmin):

    def get_actions(self, request):
        '''This built-in method can conditionally enable or disable CMS actions, returning
        a dictionary of actions allowed.'''
        # Remove the delete action from the list-view:
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        '''This built-in method should return True if deleting obj is permitted.'''
        # Prevent deletion of profile from the CMS, except when User is deleted:
        if request.path.startswith('/admin/auth/user/'):  # or '/admin/accounts/user/'
            return request.user.is_superuser  # True if superuser!
        return False


admin.site.register(UserProfile, UserProfileCMS)
