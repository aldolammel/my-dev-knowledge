#### Python > Django > API
# Serializer class template

---
## Before:
- Assuming you are following Django API roadmap: [/python/web-development/django/0-new-project/api](/python/web-development/django/0-new-project/api.md)
- Assuming your project is using *Django Rest Framework* (DRF): [/python/web-development/django/component-libraries/django-rest-framework/0-restframewok](/python/web-development/django/component-libraries/django-rest-framework/0-restframewok.md)

---

Serialization is a crucial core layer of [API](/api/_about.md) responsible for converting the model data to JSON, making it easier to be sent/transmitted to out there. A view class (`views.py`) could make the same, but with much more code lines and awful scalability. Then use serializer to help view with the JSON task.

---
## Serializer basic template:
In `/apps/subapp_name/serializers.py`:
```python
from rest_framework import serializers
from . import models

class ExampleModelSerializer(serializers.ModelSerializer):
    """Converting xxxxxxxxxxxxxx model instances to JSON data."""

    # Custom Fields (directly based on another serializer class) declaration:
    # Reserved space...

    # Custom Method Fields (SerializerMethodField) declaration:
    # (These declarations call their get_something() automatically)
    # Reserved space...

    class Meta:
        # Which model class the data's coming from:
        model = models.ExampleModel
        # Which fields (attributes) specifically:
        fields = [
            "xxxxxxxxx_1",
            "xxxxxxxxx_2",
            "xxxxxxxxx_3",
            "xxxxxxxxx_4",
            # Custom field:
            # Reserved space...
        ]

    # Custom Method Fields:
    # Reserved space...

```

---
## Creating custom fields directly in a serializer class:
When you create a serializer class, you are building up an API endpoint, and, if needed, with custom fields to extract even more data to complement your API.
 
 Every `serializers.py` file demands:
```python
 from rest_framework import serializers
```

**There are 2 ways to extract data from models using a serializer class:**
- A) **Custom Method Field:** uses a method-automatically-called to extract data elsewhere.
	- You extract external data, creating a method to filtering data with a queryset.
- B) **Custom Field**: uses another endpoint (serializer class) to collect more data.
	- You extract external data too, but without create any method or a queryset.

......................................
### A) Custom method field
You extract external data, creating a method to filtering data with a queryset.

**Example 1/3:**
A very basic custom method field creation where the entire data-flow's shown below.

Context (`models.py`):
```python
class Page(models.Model):
	title = ...
	is_blog = ...

class Post(models.Model):
	blog = ...  # menu drop-down to select some Page that is_blog = True
	title = ...
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, ...)
```

In `serializers.py`:
For *custom method field*, you'll only use the *field-class* `SerializerMethodField` for every attribute.
```python
class PostSerializer(serializers.ModelSerializer):

	# ...
	
	# Custom Method Fields (SerializerMethodField) declaration:
	# (These declarations call their get_something() automatically)
	blog_name = serializers.SerializerMethodField()
	created_by_name = serializers.SerializerMethodField()

	class Meta:
		model = models.Post
		fields = [
			# "blog",  # It would bring the blog ID (e.g. 1) and not the blog name.
			"blog_name",  # Custom method field.
			# "created_by",  # It would bring the user ID (e.g. 1) and not the username.
			"created_by_name",  # Custom method field.
		]

	def get_blog_name(self, obj):
		if obj.blog:
			return obj.blog.title # Output: e.g. "My Blog Name"
		return ""
	
	def get_created_by_name(self, obj):
		if obj.created_by:
			if obj.created_by.get_full_name():
				return obj.created_by.get_full_name() # Output: e.g. "John Doe"
			return obj.created_by.username # Output: e.g. "johndoe1984"
		return ""

```

**Example 2/3:**

These examples below returning list, dict, and even an argument value from another model, unlikely the current model declared in the current serializer's Meta class:

Context (`models.py`):
```python
class AppModel(models.Model):
	is_something_active = ...
	
class Pg(models.Model):
	title = ...
	categories = models.ManyToManyField("PgCategory",...)
	keywords = models.ManyToManyField("PgKeyword", ...)
	
class PgCategory(models.Model):
	name = ...
	slug = ...
	
class PgKeyword(models.Model):
	name = ...
```
In `serializers.py`:
Remember: for *custom method field*, you'll only use the *field-class* `SerializerMethodField` for every attribute.
```python
class PgSerializer(serializers.ModelSerializer):

	# Custom Method Fields (SerializerMethodField) declaration:
	# (These declarations call their get_something() automatically)
	is_active = serializers.SerializerMethodField()
	pg_categories = serializers.SerializerMethodField()
	pg_keywords = serializers.SerializerMethodField()

class Meta:
	model = models.Pg
	fields = [
		"title",
		#"categories", # pg_categories instead!
		"is_active", # Custom method field.
		"pg_categories", # Custom method field.
		"pg_keywords", # Custom method field.
	]

def get_is_active(self, obj):
	"""Example of how to consult an attr status from another model not used in local Meta"""
	singleton = models.AppModel.objects.first()
	if singleton and hasattr(singleton, "is_something_active"):
		return singleton.is_something_active
	return "ERROR: get_is_active"
  
def get_pg_categories(self, obj):
	"""Returns a list with a dict of all page categories in (but if empty, returns [])"""
	return [{"name": cat.title, "slug": cat.slug} for cat in obj.categories.all()]
  
def get_pg_keywords(self, obj):
	"""Returns a list of all page keywords (but if empty, returns [])"""
	return list(obj.keywords.values_list("name", flat=True))
```

**Example 3/3:**

Using another endpoint (serializer) to collect even more data and filtered:

Context (`models.py`):
```python
class Page(models.Model):
	title = ...
	slug = ...
	is_published = ...
	categories = models.ManyToManyField(
	"PageCategory",
	related_name="related_page_categories",
	)

class PageCategory(models.Model):
	name = ...
	slug = ...
```
In `serializers.py`:
Remember once more: for *custom method field*, you'll only use the *field-class* `SerializerMethodField` for every attribute.
```python
class CategoryDetailSerializer(serializers.ModelSerializer): # serializer used to detail something

	class Meta:
		model = models.Page
		fields = [
			"title",
			"slug",
			"desc",
		]


class CategorySerializer(serializers.ModelSerializer):  # main serializer what will be the endpoint!

	# Custom Method Fields (SerializerMethodField) declaration:
	# (These declarations call their get_something() automatically)
	related_pages = serializers.SerializerMethodField()
	
	class Meta:
		model = models.PageCategory
		fields = [
			"slug",
			"name",
			"related_pages", # Custom method field
		]

	def get_related_pages(self, obj):
		# This 'related_page_categories' comes from the PageModel's category attribute that has defined the 'related_name' argument:
		qs_published_pages = obj.related_page_categories.filter(is_published=True).order_by("title")
		return CategoryDetailSerializer(qs_published_pages, many=True).data

```

......................................

### B) Custom fields
Unlike the *custom method field* that uses a filtered data from another endpoint (serializer), using this *custom field* (not method) you can extract external data too, but without a custom queryset:

Context (`models.py`):
```python
class Menu(...):
	"""It manages which Menus exist through the app."""
	# ...
	
class MenuLink(...):
	"""Each instance is a link in the app menus."""
	menu = models.ForeignKey(
		Menu,
		related_name="menu_links",
		# ...
	)

	# ...
```
In `serializers.py`:
```python
class MenuLinkSerializer(serializers.ModelSerializer):
	"""It packages all links of a menu to be used by MenuSerializer."""
	# ...

	class Meta:
		model = models.MenuLink
		# ...

class MenuSerializer(serializers.ModelSerializer):
	"""Creating the Pagex Menu API where all menus data is converted to JSON format."""

	# Custom Fields (directly based on another serializer class):
	links = MenuLinkSerializer(many=True, read_only=True, source="menu_links")
	
	class Meta:
		# Which model class the data's coming from:
		model = models.Menu
		# Which fields (attributes) specifically:
		fields = [
			# ...
			"links", # Custom field
		]
	# ...
```


---
## Creating API roadmap:
[/python/web-development/django/0-new-project/api](/python/web-development/django/0-new-project/api.md)



