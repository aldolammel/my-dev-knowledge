#### Python > Django > Models > Class types
# Mixin class

---

In Django, a model mixin is an [abstract](/dev-concepts/class-type-abstract.md) class that provides reusable fields and methods to other models via multiple inheritance, promoting the [DRY principles](/dev-concepts/principles-dry.md). Mixins are typically used to inject common functionalities without forcing a strict "is-a" relationship (unlike typical inheritance). So it's absolutely professional to use mixin classes everywhere you using Django.

**Mixin concept:** [/dev-concepts/class-type-mixin](/dev-concepts/class-type-mixin.md)

==Important==
Once pretty often mixin is an abstract class, abstract models SHOULDN'T have a primary key!

---
## In `models.py`:
Example of a mixin widely called through an entire app (through is sub-apps):
```python
# /core/models.py:
class AuditMixin(models.Model): # Abstract model!
	"""Stores who and when things were changed. Those classes that inherited this mixin must send the user via `admin.py` save_model() method!"""
	created_at = models.DateTimeField(
		auto_now_add=True,
		editable=False,
		verbose_name=lang.lbl_created_at,
	)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name="%(app_label)s_%(class)s_created_by",
		editable=False,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name=lang.lbl_created_by,
	)
	# ...
	
	class Meta:
		abstract = True # Flags to the db that no tables should be created from this.
		

# /apps/subapp_name/models.py:
from core.models import AuditMixin
class Post(AuditMixin):
	# ...
```

---
## In `admin.py`:
Same logic for cases using `models.py` or `serializers.py`.
```python
class SaveUserMixin:
    """Automatically passes the current user to the model's save method."""

    def save_model(self, request, obj, form, change):
        """Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)

@admin.register(models.ExampleModelOne)
class ExampleModelOneAdmin(SaveUserMixin):
    # ...
    # the save_model() method is here by inheritance (from SaveUserMixin class)

@admin.register(models.ExampleModelTwo)
class ExampleModelTwoAdmin(SaveUserMixin):
    # ...
    # the save_model() method is here by inheritance (from SaveUserMixin class)
```

Of course, if you wanna customize the `save_model()` method in a Admin class, you cannot use that same `SaveUserMixin` inheritance, making a better approach to declare the `save_model()` into the Admin class instead of to use a mixin class.

---
## In `serializers.py`:
Another example where there's a few differences for each case.
```python
class ContentMixin:
    def _build_content_dict(self, content_qs):
        """Return a dict keyed by unique element_identifier of every content of pages and structures."""
        content_dict = {}
        for el in content_qs:
            element = el.section_element.element
            if isinstance(element, models.PagexElementImg):
                value = el.element_content_file_img.url if el.element_content_file_img else ""
            elif isinstance(element, models.PagexElementFile):
                value = el.element_content_file_doc.url if el.element_content_file_doc else ""
            else:
                value = el.element_content_txt
            content_dict[el.element_identifier] = {"v": value}
        return content_dict

class PagexPageSerializer(ContentMixin, serializers.ModelSerializer):
    # ...

    def get_content(self, obj):
        """Return a dict keyed by unique element_identifier of each page's content."""
        return self._build_content_dict(obj.page_content.all())

class PagexStructureSerializer(ContentMixin, serializers.ModelSerializer):
    # ...

    def get_content(self, obj):
        """Return a dict keyed by unique element_identifier of each structure's content."""
        return self._build_content_dict(obj.struct_content.all())
```

---


