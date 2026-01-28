
"""
    DJANGO > CMS > CREATING A ENTIRELY NEW FIELDSET
    
        >> Other options:
            ./detailview-custom-fieldset.txt
        
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

# models.py:

class PagexContent(models.Model):
    """Stores the customized content for each element seen in a page OR structure. Reused by both PagexPage and PagexStructure."""

    #...
    element_content_txt = models.TextField(
        blank=True,
    )
    element_content_file_img = models.ImageField(
        upload_to="images",
        blank=True,
        null=True,
    )
    #...


# admin.py:

class PagexPageContentInline(admin.StackedInline):
    """Shows each page content's element editable through an existing page."""

    model = models.PagexContent
    form = forms.PagexContentForm
    # ...
    verbose_name = "Elemento"
    verbose_name_plural = "Conteúdo da Página"
    readonly_fields = (
        "where_display",
        # ...,
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "where_display",
                    "element_content_txt",
                    "element_content_file_img",
                    #...,
                )
            },
        ),
    )

    class Media:
        css = {
            # Location: /static/css/
            "all": ("css/pagex_admin_content_inline.css",),
        }

    def where_display(self, obj):
        # return f"{obj_type} > {obj.section_element.section.name} > {obj.element_identifier}"
        return obj.section_element.section.name

    # ...
    # Defining method field labels:
    where_display.short_description = "Da seção"  # type: ignore[attr-defined]



# forms.py:

class PagexContentForm(forms.ModelForm):
    """Custom form for PagexContent that adapts fields based on element type."""

    class Meta:
        model = models.PagexContent
        fields = [
            "element_content_txt",
            "element_content_file_img",
            #...,
        ]

    def __init__(self, *args, **kwargs):
        """Built-in method called 'Constructor', designed to initialize the instance."""
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.section_element:
            element = self.instance.section_element.element

            # Configure fields based on element type and hide irrelevant ones:
            if isinstance(element, models.PagexElementTxt):
                self.fields["element_content_txt"].widget = forms.Textarea(
                    attrs={"rows": 4, "placeholder": ""}
                )
                # Hide irrelevant fields:
                self.fields["element_content_file_img"].widget = forms.HiddenInput()

            elif isinstance(element, models.PagexElementImg):
                self.fields["element_content_file_img"].widget = forms.ClearableFileInput(
                    attrs={"accept": "image/*"}
                )
                # Hide irrelevant fields:
                self.fields["element_content_txt"].widget = forms.HiddenInput()


# .css file:

"""
.inline-related {
  padding: 20px 0;
}

.inline-related fieldset {
  background-color: transparent;
}
.inline-related:nth-child(even) {
  background-color: var(--darkened-bg); /* Django theme light/dark compatible */
  line-height: 100%;
}

.inline-related:nth-child(odd) {
  background-color: var(--body-bg); /* Django theme light/dark compatible */
}
"""
