from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from django.utils.html import format_html
from django.urls import reverse



class UserCMS(UserAdmin):
    '''Defining how the User Model class will exclusivily be shown on the CMS.'''

    # Specify the custom form for creating users
    add_form = CustomUserCreationForm

    list_display = (
        'username',
        'email',
        'last_login',
        'is_staff',
        # List_display accept imported fields using prefix and imported method (prefix recommended):
        # Reserved space...
    )
    # All fields exclusivily for the CMS Adding New User:
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'profile_type',
                    'username',
                    'email',
                    'password1',
                    'password2',
                    'accepted_min_age',
                    'accepted_our_privacy',
                ),
            },
        ),
    )
    # All fields exclusivily for the CMS Visualizing a User:
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password',
                    'profile_type',
                    'profile_link',  # Adding the UserProfile link in the User Detail-view!
                )
            },
        ),
        (
            'Personal info',
            {
                'fields': (
                    'email',
                    'language',
                )
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_notified_by_email',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'date_joined',
                    'last_login',
                    'updated_at',
                    'updated_by',
                )
            },
        ),
    )
    list_filter = (
        'profile_type',
        'language',
        'is_notified_by_email',
        'is_active',
        'is_staff',
        'is_superuser',
        # List_filter only accepts imported fields using prefix:
        # Important: Don't call UserProfile's content here in this case!
    )
    search_fields = [
        'username',
        'email',
        'date_joined',
        # Search_fields accept imported fields using prefix and imported method (prefix recommended):
        'userprofile__first_name',
        'userprofile__last_name',
        'userprofile__birth_year',
        'userprofile__city',
        'userprofile__country',
    ]
    readonly_fields = (
        # 'profile_type',  # Dynamicaly included!
        # 'username',  # Dynamicaly included!
        'profile_link',  # Important: don't remove 'profile_link' from here!
        'date_joined',
        'last_login',
        'updated_at',
        'updated_by',
        # Readonly_fields only accept imported method, never with prefix:
        # Important: Don't call UserProfile's content here in this case!
    )

    # Create a hyperlink to the associated UserProfile to be used on the list-view and detail-view:
    def profile_link(self, obj):
        if obj:
            url = reverse(
                # Automatic admin-view creation structure: 'admin:app_label_modelname_change':
                'admin:accounts_userprofile_change',
                args=[getattr(obj, 'profile_1').id],
            )
            return format_html("<a href='{}'>{} ({})</a>", url, 'User Profile', CMS_MORE_DETAILS)
        return CMS_ERRO_PROFILE

    profile_link.short_description = 'User Profile'

    def get_readonly_fields(self, request, obj=None):
        """Built-in method to extend the 'readonly_fields' power."""

        if obj:
            # If the user exists (obj), make some fields field read-only on detail-view,
            # but still editable on the CMS Add User form:
            return self.readonly_fields + (
                'profile_type',
                'username',
                'accepted_min_age',
                'accepted_our_privacy',
            )  # type: ignore
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        # Checks to save the current user as updated_by:
        cms_user = request.user
        if change and cms_user != obj.updated_by:
            obj.updated_by = cms_user
        super().save_model(request, obj, form, change)