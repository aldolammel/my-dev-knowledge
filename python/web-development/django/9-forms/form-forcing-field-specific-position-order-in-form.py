"""
    DJANGO > FORMS > FORCING A SPECIFIC ORDER POSITION IN THE RENDERED FORM:

    >> Context:
        You wanna see in your CMS form the 'elm_content_key' always as the first field, but as it's a non-editable attribute on the db, Django won't put it automatically as something to be rendering in a form (once the field couldn't be editable). 

    >> Solutions below:
        A. Using explicit declaration via model admin class!
        B. Using the admin class' built-in get_fields() method!
        C. Using the admin class' built-in get_fieldsets() method!

"""

# CONTEXT - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# models.py
class PagexContent(models.Model):
    id = models.SmallAutoField(editable=False, ...)
    elm_content_key = models.SlugField(editable=False, ...)
    elm_content_css = models.CharField(...)
    ...

# admin.py
class PagexPageContentInline(...):
    model = models.PagexContent
    form = forms.PagexContentForm
    ...
    readonly_fields = (
        "elm_content_key",
    )

# forms.py
class PagexContentForm(...):
    class Meta:
        # Model tied used to populate it:
        model = models.PagexContent
        # Django rule: to be called here, the field CANNOT be 'editable=False', nor custom method. If the field is editable but for the form it should be readonly_fields, no problem, call it!
        fields = [
            # "id",               # non-editable!
            # "elm_content_key",  # non-editable!
            "elm_content_css",
        ]

# CMS INTERFACE RENDERING ISSUE:
# You will see the "elm_content_key" always as the last field in the form because Django first set in the interface every field listed in the form 'fields' array and, just after that, append every field listed in the admin 'readonly_fields' (because only there you can call a non-editable field).



# SOLUTIONS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# A) SIMPLEST WAY:
# Explicit declaration of every field u wanna make known by the form, including non-editable fields!

# admin.py
class PagexPageContentInline(...):
    model = models.PagexContent
    form = forms.PagexContentForm
    ...
    readonly_fields = (
        # "id",
        "elm_content_key",
    )
    ...
    # All fields exclusively for the CMS' EXISTING object detail-view:
    fieldsets = (
        (
            None,
            {
                "fields": (
                    # "id",  # non-editable
                    "elm_content_key", # non-editable here only if declared in readonly_fields list!
                    "elm_content_css",
                )
            },
        ),
    )

# forms.py
class PagexContentForm(...):
    class Meta:
        model = models.PagexContent
        # This "__all__" below should take everything u set in that admin class of the tied model. So, if you got an admin class that explicit says which fields this form could to known, it means all those fields declared and NOT necessarily all model fields case the admin is not listing everyone exists in model:
        fields = "__all__"


# B) FORCING VIA GET_FIELDS() METHOD:
# For example, in case you won't explicit declare fields through the admin class.

# admin.py
class PagexPageContentInline(...):
    ...
    def get_fields(self, request, obj=None):
        """Built-in method to retrieve a tuple of all field instances associated with a model."""
        fields = list(super().get_fields(request, obj))

        if "elm_content_key" in fields:
            fields.remove("elm_content_key")
            fields.insert(0, "elm_content_key")

        return fields

# forms.py
class PagexContentForm(...):
    class Meta:
        model = models.PagexContent
        fields = "__all__"


# C) FORCING VIA GET_FIELDSETS METHOD:
# For example, in case you won't explicit declare fields through the admin class.

# admin.py
class PagexPageContentInline(...):
    ...
    def get_fieldsets(self, request, obj=None):
        """Built-in method that brings all data from fieldsets of the admin class."""
        fieldsets = list(super().get_fieldsets(request, obj))  # type: ignore[misc]
        title, options = fieldsets[0]
        fields = list(options["fields"])

        if "elm_content_key" in fields:
            fields.remove("elm_content_key")
            fields.insert(0, "elm_content_key")

        fieldsets[0] = (title, {**options, "fields": tuple(fields)})
        return fieldsets

# forms.py
class PagexContentForm(...):
    class Meta:
        model = models.PagexContent
        fields = "__all__"