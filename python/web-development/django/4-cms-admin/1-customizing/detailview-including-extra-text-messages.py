"""
    DJANGO CMS: INCLUDING EXTRA TEXT (HTML) MESSAGES IN DETAIL-VIEW

    Imagine you are in a movie instance in CMS, and you wanna see all actors added to this movie as part of casting. Each actor was previously added to the CMS and, after that, added to the movie instance. But your movie has an empty actor list. So you try to add someone and no actor is available in your DB. That said, you wanna add a text/html simple message warning the CMS user that's need to add actors in the db first. This will show how to do this message warning.
    
"""

# admin.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from django.urls import reverse
from django.utils.html import format_html

class MovieContentInline(admin.StackedInline):
    ...
    # Custom form:
    # form = no matter if this admin class uses custom form or not!

    readonly_fields = (
        "no_actors_msg",  # Custom method field
        ...
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "no_actors_msg",  # Custom method field  # May removed dynamically if conds are met.
                    ...
                )
            }
        )
    )

    def get_fieldsets(self, request, obj=None):
        """Brings all data from fieldsets of the admin class."""
        fieldsets = list(super().get_fieldsets(request, obj))
        title, options = fieldsets[0]
        fields = list(options["fields"])

        if models.Actor.objects.exists():
            fields.remove("no_actors_msg")

        fieldsets[0] = (title, {**options, "fields": tuple(fields)})
        return fieldsets

    def no_actors_msg(self, request, obj=None):
        """Custom method field that xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx."""
        url = reverse("admin:myappname_actor_add")
        # For one-language-app:
        return format_html(
            "<div class=''>No actors found in the casting library: <a href='{}'>Add actor/actress</a></div>",
            url,
        )
        # Or for multilingual-app:
        return format_html(
            "<div class=''>{} <a href='{}'>{}</a></div>",
            f"{lang.txt_1}",
            url,
            f"{lang.txt_2}",
        )

    # Defining custom method field labels:
    no_actors_msg.short_description = "Warning"  # type: ignore[attr-defined]