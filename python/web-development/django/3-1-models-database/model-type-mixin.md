#### Python > Django > Models > Class types
# Mixin class

---

In Django, a model mixin is an [abstract](/dev-concepts/class-type-abstract.md) class that provides reusable fields and methods to other models via multiple inheritance, promoting the [DRY principles](/dev-concepts/principles-dry.md). Mixins are typically used to inject common functionalities without forcing a strict "is-a" relationship (unlike typical inheritance). So it's absolutely professional to use mixin classes everywhere you using Django.

**Mixin concept:** [/dev-concepts/class-type-mixin](/dev-concepts/class-type-mixin.md)

==Important 1==
Once pretty often mixin is an abstract class, abstract models SHOULDN'T have a primary key!

==Important 2==
Mixin model classes demand special attention when they are using [ForeignKey()](/python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md) field class. The [related_name](/python/web-development/django/3-1-models-database/arg-related_name.md) argument will clash is the same name is applied for more than one model class that inherits it. To result in its name: `%(app_label)s_` or `%(class)s_` or both, e.g., `related_name="%(class)s_steps"`.

---
## In `models.py`:
Example of a mixin widely called through an entire app (through is sub-apps):
```python
# /core/models.py: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class AuditMixin(models.Model): # Abstract model!
	"""Creates attributes commonly used by those model classes that demand audit control. Classes that inherited this mixin class must send the user via admin class' save_model() method!"""
	# ...
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
		

# /apps/subapp_name/models.py: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
from core.models import AuditMixin
class Post(AuditMixin):
	# ...
```
A complete example of `AuditMixin` model class you take here: [/python/web-development/django/3-1-models-database/\_model-class-model.py](/python/web-development/django/3-1-models-database/_model-class-model.py)

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
## Otherwise, in case you wanna benefits of a Base Model class:
[/python/web-development/django/3-1-models-database/model-type-base](/python/web-development/django/3-1-models-database/model-type-base.md)

