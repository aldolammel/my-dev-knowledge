#### Python > Django > Structure
# `Models.py` file

---

Django is divided in 3 main parts: models, views, and templates. Models are responsible for listing the data structure of a Django app, using classes to build tables and their attributes in a database. Through `models.py` you:

- Define the schema of your database;
- Provide methods for querying and manipulating the data;
- Enforce data integrity by defining constraints and validations.

---
## Model-class examples:
Django Model-class example that is used to create database structure: [/python/web-development/django/3-1-models-database/\_model-class-model.py](/python/web-development/django/3-1-models-database/_model-class-model.py)

---
## Common attribute-types (field classes):
Most common attribute-types you will use to build up every class fields/db columns: [/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

---
## Form fields, including widget fields:
[/python/web-development/django/9-forms/\_forms_knowledge](/python/web-development/django/9-forms/_forms_knowledge.md)

---
## Understanding the model field arguments (parameters):
E.g. `<some-attr-name> = models.<some-field-class>(arg1, arg2, ...)`: [/python/web-development/django/3-1-models-database/2-model-arguments](/python/web-development/django/3-1-models-database/2-model-arguments.md)

---
## Renaming a class model:
Pay attention, following this checklist to avoid crashes widely in your app: [/python/web-development/django/3-1-models-database/renaming-model-class](/python/web-development/django/3-1-models-database/renaming-model-class.md)

---
## Other Django structural parts:
- Views: [/python/web-development/django/3-2-views-and-API/\_about](/python/web-development/django/3-2-views-and-API/_about.md)
- Templates: [/python/web-development/django/3-3-frontend-templates/\_about](/python/web-development/django/3-3-frontend-templates/_about.md)

