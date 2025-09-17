"""
    REMOVING CMS PERMISSION: TO ADD NEW ENTRY
    
    Case:

        Let's imagine you want to see each entry of UserProfile listed on the CMS but
        no one must include a UserProfile manually through the CMS, leaving the creation task
        for a signals.py or forms.py file code.

"""

from django.contrib import admin
from .models import UserProfile  # type: ignore


class UserProfileCMS(admin.ModelAdmin):

    def has_add_permission(self, request):
        """This built-in method should return True if adding obj's allowed."""
        # Prevent the addition of a lone profile accidentally:
        return False


admin.site.register(UserProfile, UserProfileCMS)
