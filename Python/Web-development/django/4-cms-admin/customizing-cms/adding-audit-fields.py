
"""
    ADDING AUDIT FIELDS (WITH AUTO-FILL)
                
        >> If you wanna add audit fields (auto-fill) to control content changes through CMS:
"""
# FILE: /apps/my_app/models.py

class PageModel(models.Model):
    ...
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        User,
        related_name="pages",
        on_delete=models.SET_NULL,
        null=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="updated_pages",
        on_delete=models.SET_NULL,
        null=True,
    )

    def save(self, *args, **kwargs):
        """Built-in method that's executed when the entry saving runs."""
        
        # Retrieve the user from kwargs, default to None if not passed:
        user = kwargs.pop("user", None)
        if self.something_exist_an_important_field:
            ...
            # Set created_by if this is a new object:
            if not self.pk and user:
                self.created_by = user
            # Otherwise, set updated_by:
            elif user and user.is_authenticated and user != self.updated_by:
                self.updated_by = user
            # Save instance:
            super().save(*args, **kwargs)


# FILE: /apps/my_app/admin.py

@admin.register(PageModel)
class PageModelAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    )

    def save_model(self, request, obj, form, change):
        """It's a key part of Django's admin customization that allows you to control what happens
        when a model instance (models.py) is created/updated through the CMS."""
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)