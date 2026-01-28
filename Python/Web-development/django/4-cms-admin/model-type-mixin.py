"""
    DJANGO > MODEL/CLASS TYPE: MIXIN

    In Django, a model mixin is an abstract base class that provides reusable fields and methods to other models via multiple inheritance, promoting the "Don't Repeat Yourself" (DRY) principle. Mixins are typically used to inject common functionalities without forcing a strict "is-a" relationship (unlike typical inheritance). 
"""

# admin.py (same logic for cases using models.py or serializers.py, for example) - - - - - - - - - -

class SaveUserMixin:
    """Automatically passes the current user to the model's save method."""

    def save_model(self, request, obj, form, change):
        """Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)


@admin.register(models.ExampleModelOne)
class ExampleModelOneAdmin(SaveUserMixin):
    ...
    # the save_model() method is here by inheritance (from SaveUserMixin class)


@admin.register(models.ExampleModelTwo)
class ExampleModelTwoAdmin(SaveUserMixin):
    ...
    # the save_model() method is here by inheritance (from SaveUserMixin class)


# Of course, if you wanna customize the save_model() method in a Admin class, you cannot use that same SaveUserMixin inheritance, making a better approach to declare the save_model into the Admin class instead of to use a mixin class.



# ANOTHER EXAMPLE (WHEN THERE'S A FEW DIFFERENCES FOR EACH CASE) - - - - - - - - - - - - - - - - - -

# serializers.py

class ContentMixin:
    def _build_content_dict(self, content_qs):
        """Return a dict keyed by unique element_identifier of every content of pages and structures."""
        content_dict = {}
        for el in content_qs:
            element = el.section_element.element
            if isinstance(element, models.PagexElementImg):
                value = el.element_content_file_img or None
            elif isinstance(element, models.PagexElementFile):
                value = el.element_content_file_doc or None
            else:
                value = el.element_content_txt
            content_dict[el.element_identifier] = {"v": value}
        return content_dict

class PagexPageSerializer(ContentMixin, serializers.ModelSerializer):
    ...

    def get_content(self, obj):
        """Return a dict keyed by unique element_identifier of each page's content."""
        return self._build_content_dict(obj.page_content.all())

class PagexStructureSerializer(ContentMixin, serializers.ModelSerializer):
    ...

    def get_content(self, obj):
        """Return a dict keyed by unique element_identifier of each structure's content."""
        return self._build_content_dict(obj.struct_content.all())