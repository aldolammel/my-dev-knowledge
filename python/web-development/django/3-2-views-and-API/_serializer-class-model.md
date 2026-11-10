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
In `/apps/subapp/serializers.py`:
```python
from rest_framework import serializers
from . import models

class SomethingSerializer(serializers.ModelSerializer):
    """Converting xxxxxxxxSomethingModelClassxxxxxxxx model instances to JSON data."""

    # Explicit Fields declaration:
    # Reserved space...
    
    # Nested Fields (other serializer-based) declaration:
    # Reserved space...

    # Custom Method Fields (SerializerMethodField) declaration:
    # (These declarations call their get_something() automatically)
    # Reserved space...

    class Meta:
        # Which model class the data's coming from:
        model = models.Something
        # Which fields (attributes) specifically:
        fields = "__all__"  # Make this first to reveal all the potential forgotten/inherited fields that are available!
        """fields = [
            "xxxxxxxxx_1",
            "xxxxxxxxx_2",
            "xxxxxxxxx_3",
            "xxxxxxxxx_4",
            # - - - - - - - Custom field - - - - - - -
            # Reserved space...
        ]"""
        

    # Custom Method Fields:
    # Reserved space...

```

---
## Creating fields directly in the serializer class:
When you create a serializer class, you are building up an API endpoint, and, if needed, you can create new fields to extract even more data to complement the API. Below, check the available ways to do that.
 
 Every `serializers.py` file demands:
```python
 from rest_framework import serializers
```

**3 ways to pack data in JSON:**
- A) **Explicit Field:** use it when you can retrieve the information directly from a model field or a related model field.
	- Perfect when the data already is in the target model of your serializer.
- B) **Nested Field**: use it when you want to include data from another serializer in the current one.
	- Perfect when you already got another serialized model and wanna represent that into your current serializer structure.
- C) **Custom Method Field:** use it when the returned value requires custom logic.
	- Perfect when you need Python to figure out what the data should be (using conditions, querysets).

......................................

### A) Explicit field
Use them when you can retrieve the information directly from a model field or a related model field. For example, *DRF* already knows how to retrieve model attributes and relationships. You don't need to write a method (option C) just to access them.
Context (`models.py`):
```python
class Something(...):
	platform = models.ForeignKey(Platform, ...)
	created_by = models.ForeignKey(User, ...)
```
In `serializers.py`:
```python
class SomethingSerializer(serializers.ModelSerializer):

    # Explicit Fields declaration:
    platform = serializers.CharField(
        source="platform.name",  # Instead of the original value (id)
        read_only=True,
    )
    created_by = serializers.CharField(
        source="created_by.username",  # Instead of the original value (id)
        read_only=True,
    )
	
	# ...
	
    class Meta:
        # ...
        fields = [
            "platform",
            "created_by",
        ]
```

......................................

### B) Nested field
Use it when you want to include data from another serializer in the current one.

Context (`models.py`):
```python
class Menu(...):
	# ...
	
class MenuLink(...):
	menu = models.ForeignKey(Menu, related_name="menu_links")
```
In `serializers.py`:
```python
class MenuLinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MenuLink
		# ...

class MenuSerializer(serializers.ModelSerializer):
	# ...
	
	# Nested Fields (other serializer-based) declaration:
	links = MenuLinkSerializer(
		many=True,
		source="menu_links",
		read_only=True,
	)
	
	# ...
	
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

......................................

### C) Custom method field
Use it when the returned value requires custom Python logic. You extract external data, creating a method to filtering data with a queryset.

==Be aware:== `SerializerMethodField` is read-only!

**Example 1/3:**

Context (`models.py`):
```python
class User(...):
	username = ...
	f_name = ...
	l_name = ...

class Something(models.Model):
	# ...
	created_by = models.ForeignKey(User, ...)
```
In `serializers.py`:
```python
class SomethingSerializer(serializers.ModelSerializer):

	# ...
	
	# Custom Method Fields (SerializerMethodField) declaration:
	# (These declarations call their get_something() automatically)
	created_by_name = serializers.SerializerMethodField()

	class Meta:
		model = models.Something
		fields = [
			# ...
			# "created_by",  # It would bring the user ID (e.g. 1) and not the username or user full name.
			"created_by_name",  # Custom method field.
		]
	
	def get_created_by_name(self, obj):
		if obj.created_by:
			if obj.created_by.f_name and obj.created_by.l_name:
				return f"{obj.created_by.f_name} {obj.created_by.l_name}"  # Output: e.g. "John Doe"
			return obj.created_by.username  # Output: e.g. "johndoe1984"
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
```python
class PgSerializer(serializers.ModelSerializer):

	# ...
	
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

---
## Creating API roadmap:
[/python/web-development/django/0-new-project/api](/python/web-development/django/0-new-project/api.md)



