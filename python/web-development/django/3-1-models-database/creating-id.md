#### Python > Django > Models
# Creating a Primary Key (ID)

---

In Django, Primary Keys are created automatically by default, so Django creates a field called `id` for every Model Class created even though you didn't declare its `id`. You can define a default attribute type for the entire app, or by sub-app, or explicit for every class created (recommended).

---
## Expliciting the `id` attribute type in the Model class:
This way the class has no suppressed `id` because you are declaring it explicitly, make it has the highest configure priority. Recommended way to work! 

E.g. in a `/apps/subapp-folder/models.py`:
```python
class Movie(models.Model):
	id = models.AutoField(primary_key=True)  # 'id' attr. can be renamed if u want. What's defining it as PK is its argument/parameter "primary_key=True".
```

---
## Defining by sub-app a default `id` attribute type:
This way makes all suppressed `id` in a specific sub-app has its own default `id` class field to be used. 

E.g. in a `/apps/subapp-folder/apps.py`:
```python
class SubappNameConfig(AppConfig):
	default_auto_field = 'django.db.models.AutoField'
	# ...
```

---
## Defining globally a default `id` attribute type:
This way makes all suppressed `id` from every new sub-app has the same `id` class field. This method is okay only if you just created your Django project. This way has the lowest priority in a class settings. 

In `/core/settings.py`:
```python
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
```

---

## All attribute types (field classes) that works perfectly as Primary Key:

| Field class (attribute type)                                                                         | Full range                                              | Auto-increment range                                                     |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------ |
| [SmallAutoField()](/python/web-development/django/3-1-models-database/model-attr-field-smallAuto.md) | -32,768 to 32,767                                       | 1 to 32,767                                                              |
| [AutoField()](/python/web-development/django/3-1-models-database/model-attr-field-auto.md)           | -2,147,483,648 to 2,147,483,647                         | 1 to 2,147,483,647                                                       |
| [BigAutoField()](/python/web-development/django/3-1-models-database/model-attr-field-bigAuto.md)     | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | 1 to 9,223,372,036,854,775,807                                           |
| [UUIDField()](/python/web-development/django/3-1-models-database/model-attr-field-uuid.md)           | Doesn't work like that (128 bits)                       | Not sequential; can be generated automatically with `default=uuid.uuid4` |

---
## Most common Django field classes:
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

