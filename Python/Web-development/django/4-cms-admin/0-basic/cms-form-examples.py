from django.contrib import admin
from .models import UserProfileOne, Goal # type: ignore



class UserProfileOneCMS(admin.ModelAdmin):
    '''Defining how the UserProfileOne Model class (personal) will exclusivily be shown on the CMS.'''

    # Those fields that will be shown on the CMS list-page as columns:
    list_display = (
        'user',
        'sex',
        'birth_year',
        'country',
        # List_display accept imported fields using prefix and imported method (prefix recommended):
        'user__last_login',
    )
    
    # Those fields that must be hidden on the CMS detail-page:
    exclude = ('birth_year',)
    
    # Those fields that can be data filters on this CMS list page:
    list_filter = (
        'sex',
        'country',
        'is_nomad',
        'goal_primary',
        'goal_secondary',
        # List_filter only accepts imported fields using prefix:
        'user__language',
    )
    
    # Those fields that can be read if the search box is used on this CMS page:
    search_fields = [
        'user',
        'city',
        'first_name',
        'last_name',
        'birth_year',
        # Search_fields accept imported fields using prefix and imported method (prefix recommended):
        'user__email',
    ]
    
    # Those fields that are not editable on this CMS page:
    readonly_fields = (
        'user',
        'updated_at',
        'updated_by',
        # Readonly_fields only accept imported method, never with prefix:
        'email',  # Imported from User
        'is_notified_by_email',  # Imported from User
        'language',  # Imported from User
        'last_login',  # Imported from User
        'date_joined',  # Imported from User
    )
    
    # Defining the Admin layout only:
    fieldsets = (
        ('Basic', {
            'fields': (
                'user',
                'sex',
            )
        }),
        ('Details', {
            'fields': (
                'is_nomad',
                'birth_year',
                'country',
                'goal_primary',
                'goal_secondary',
            )
        }),
        ('Metadata', {
            'fields': (
                'user__last_login',
                'date_joined',
                'updated_at',
                'updated_by',
            )
        }),
    )

    # Importing field from User model class:
    def email(self, obj):
        return obj.user.email

    def is_notified_by_email(self, obj):
        return obj.user.is_notified_by_email

    def language(self, obj):
        return obj.user.language

    def last_login(self, obj):
        return obj.user.last_login

    def date_joined(self, obj):
        return obj.user.date_joined

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        '''This built-in method allows to override the default formfield for a foreign keys field.'''
        # It filters the goal fields by user's profile type:
        if db_field.name in ['goal_primary', 'goal_secondary']:
            # Get the current object being edited:
            obj_id = request.resolver_match.kwargs.get('object_id')  # type: ignore
            if obj_id:
                # Retrieve the related UserProfile instance:
                profile = UserProfileOne.objects.get(pk=obj_id)
                # Filter the queryset based on the user's profile_type:
                kwargs['queryset'] = Goal.objects.filter(profile_type=profile.user.profile_type)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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
        if request.path.startswith('/admin/auth/user/'):
            return True
        return False

    def has_add_permission(self, request):
        '''This built-in method should return True if adding an object is permitted.'''
        # Prevent the addition of a lone profile accidentally:
        return False

    def save_model(self, request, obj, form, change):
        # Checks to save the current user as updated_by:
        cms_user = request.user
        if change and cms_user != obj.updated_by:
            obj.updated_by = cms_user
        super().save_model(request, obj, form, change)
        
        
        
"""

    A BLANK VERSION FOR NEW PROJECTS:
    
    /Python/Web-development/django/4-cms-admin/0-basic/cms-form-blank-for-new-projects.py

"""