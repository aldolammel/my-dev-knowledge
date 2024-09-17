"""
    REMOVING CMS PERMISSION: TO ADD NEW ENTRY
    
    Case:

        Let's imagine you want to see each entry of UserProfile listed on the CMS but
        no one must include a UserProfile manually through the CMS, leaving the creation task
        for a signals.py or forms.py file code.

"""

from django.contrib import admin
from .models import UserProfile


class UserProfileCMS(admin.ModelAdmin):

    # Remove all CMS capacity to add a UserProfile entry, removing buttons and hyperlinks too:
    def has_add_permission(self, request):
        return False


admin.site.register(UserProfile, UserProfileCMS)
