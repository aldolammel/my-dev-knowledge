from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
#from parler.admin import TranslatableAdmin  # TODO: has multilingual support?
from django.utils.html import format_html
from django.urls import reverse
from core.constants import (
    REL_PROFILE_1,
    PATH_CMS_USERS,
)
from .models import (
    User,
    UserProfileOne,
    #Language,  # TODO: has multilingual support?
)
from core.language import (
    TX_PROFILE_1,
    CMS_MORE_DETAILS,
    CMS_ERRO_PROFILE,
)


@admin.register(User)
class UserCMS(UserAdmin):
    '''Defining how the User Model class will exclusivily be shown on the CMS.'''

    # Specify the custom form for creating users
    add_form = CustomUserCreationForm  # TODO What if I don't use it?

    list_display = (
        "username",
        "email",
        "last_login",
        "is_staff",
        # List_display accept imported fields using prefix and imported method (prefix recommended):
        # Reserved space...
    )
    # All fields exclusivily for the CMS Adding New User:
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "profile_type",
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "accepted_min_age",
                    "accepted_our_privacy",
                ),
            },
        ),
    )
    # All fields exclusivily for the CMS Visualizing a User:
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                    "profile_type",
                    "profile_link",  # Adding the UserProfile link in the User Detail-view!
                    "accepted_min_age",
                    "accepted_our_privacy",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "email",
                    #"language",  # TODO: has multilingual support?
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_notified_by_email",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                    "last_pwd_update",
                    "updated_at",
                    "updated_by",
                )
            },
        ),
    )
    list_filter = (
        "profile_type",
        #"language",  # TODO: has multilingual support?
        "is_notified_by_email",
        "is_active",
        "is_staff",
        "is_superuser",
        # List_filter only accepts imported fields using prefix:
        # Important: Don't call UserProfile's content here in this case!
    )
    search_fields = [
        "username",
        "email",
        "date_joined",
        # Search_fields accept imported fields using prefix and imported method (prefix recommended):
        "userprofileone__first_name",
        #'userprofileone__last_name',  # It's not used anymore!
        "userprofileone__birth_year",
        "userprofileone__country",
    ]
    readonly_fields = (
        # 'profile_type',  # Dynamicaly included!
        # 'username',  # Dynamicaly included!
        # 'accepted_min_age',  # Dynamicaly included!
        # 'accepted_our_privacy',  # Dynamicaly included!
        "profile_link",  # Important: don't remove 'profile_link' from here!
        "date_joined",
        "last_login",
        "last_pwd_update",
        "updated_at",
        "updated_by",
        # Readonly_fields only accept imported method, never with prefix:
        # Important: Don't call UserProfile's content here in this case!
    )

    # Create a hyperlink to the associated UserProfile to be used on the list-view and detail-view:
    def profile_link(self, obj):
        if obj.profile_type == "1" and hasattr(obj, REL_PROFILE_1):
            url = reverse(
                # Automatic admin-view creation structure: 'admin:app_label_modelname_change':
                "admin:accounts_userprofileone_change",
                args=[getattr(obj, REL_PROFILE_1).id],
            )
            return format_html(
                "<a href='{}'>{} ({})</a>", url, TX_PROFILE_1, CMS_MORE_DETAILS
            )
        # elif obj.profile_type == "2" and hasattr(obj, REL_PROFILE_2):
        #     url = reverse(
        #         "admin:accounts_userprofiletwo_change",
        #         args=[getattr(obj, REL_PROFILE_2).id],
        #     )
        #     return format_html(
        #         "<a href='{}'>{} ({})</a>", url, TX_PROFILE_2, CMS_MORE_DETAILS
        #     )
        return CMS_ERRO_PROFILE

    profile_link.short_description = "User Profile"

    def get_readonly_fields(self, request, obj=None):
        '''Built-in method to extend the 'readonly_fields' power.'''

        if obj:
            # If the user exists (obj), make some fields field read-only on detail-view,
            # but still editable on the CMS Add User form:
            return self.readonly_fields + (
                "profile_type",
                "username",
                "accepted_min_age",
                "accepted_our_privacy",
            )  # type: ignore
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        '''It's a key part of Django's admin customization that allows you to control what happens
        when a model instance (models.py) is created/updated through the CMS.'''
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)


@admin.register(UserProfileOne)
class UserProfileOneCMS(admin.ModelAdmin):
    '''Defining how the UserProfileOne Model class (personal) will exclusivily be shown on the CMS.'''

    list_display = (
        "user",
        #"sex",
        #"birth_year",
        # List_display accept imported fields using prefix and imported method (prefix recommended):
        "user__last_login",
    )
    #exclude = ("birth_year",)
    list_filter = (
        #"sex",
        # List_filter only accepts imported fields using prefix:
        #"user__language",  # TODO: has multilingual support?
    )
    search_fields = [
        "user",
        "first_name",
        # 'last_name',  # It's not used anymore!
        #"birth_year",
        # Search_fields accept imported fields using prefix and imported method (prefix recommended):
        "user__email",
    ]
    readonly_fields = (
        "user",
        "updated_at",
        "updated_by",
        # Readonly_fields only accept imported method, never with prefix:
        "email",  # Imported from User
        "is_notified_by_email",  # Imported from User
        #"language",  # Imported from User  # TODO: has multilingual support?
        "last_login",  # Imported from User
        "date_joined",  # Imported from User
    )

    # Importing field from User model class:
    def email(self, obj):
        return obj.user.email

    def is_notified_by_email(self, obj):
        return obj.user.is_notified_by_email

    # TODO: has multilingual support?
    '''def language(self, obj):
        return obj.user.language'''

    def last_login(self, obj):
        return obj.user.last_login

    def date_joined(self, obj):
        return obj.user.date_joined

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     '''This built-in method allows to override the default formfield for a foreign keys field.'''
    #     ...
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_actions(self, request):
        '''This built-in method can conditionally enable or disable CMS actions, returning
        a dictionary of actions allowed.'''
        # Remove the delete action from the list-view:
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_delete_permission(self, request, obj=None):
        '''This built-in method should return True if deleting obj is permitted.'''
        # Prevent deletion of profile from the CMS, except when User is deleted:
        if request.path.startswith(PATH_CMS_USERS):
            return request.user.is_superuser  # True if superuser!
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


@admin.register(Language)
class LanguageCMS(admin.ModelAdmin):
    list_display = (
        "name",
        "iso_code",
        "status",
        "updated_at",
        # List_display accept imported fields using prefix and imported method (prefix recommended):
        # Reserved space...
    )
    list_filter = (
        "status",
        # List_filter only accepts imported fields using prefix:
        # Reserved space...
    )
    '''search_fields = [
        'name',
        # Search_fields accept imported fields using prefix and imported method (prefix recommended):
        # Reserved space...    
    ]'''
    # exclude = ('xxxxx',)
    readonly_fields = (
        "created_at",
        "updated_at",
        "updated_by",
        # Readonly_fields only accept imported method, never with prefix:
        # Reserved space...
    )

    def save_model(self, request, obj, form, change):
        '''It's a key part of Django's admin customization that allows you to control what happens
        when a model instance (models.py) is created/updated through the CMS.'''
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)


# Registering Django CMS customizations:
# Reserved space...
