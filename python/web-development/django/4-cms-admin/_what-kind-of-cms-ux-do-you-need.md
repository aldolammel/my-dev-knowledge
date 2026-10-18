#### Python > Django > Admin (CMS)
# What kind of form do you need

---

A list of different approaches to list and/or visualize existing entries in the database. Below, you see a title, a description about the desired UX in CMS, and then the step-by-step to build up that.

---
## A) Regular Django behavior:

For new objects, you click over the add button and then, through the adding detail-view, you add the new object data. For existing objects, you access the object list-view and see all its entries listed where each of them are linked for its existing object detail-view.

 1. Create a [model class](/python/web-development/django/3-1-models-database/_model-class-model.py) in `models.py`.
 2. Create and register the model class as [admin class](/python/web-development/django/4-cms-admin/_admin-class-model.py) in `admin.py`.
 3. [Access the CMS](/python/web-development/django/_running-app.md), and test it. 

---
## B) Adding an instance with multi-step form:

For new objects, through the adding detail-view, select an option first (using a radio or drop-down menu), and then Django loads the specific form (still in detail-view) based on the previous selection. For existing entries through the list-view, each listed entry, if clicked, loads its specific form based in a specific model (with its unique fields);

- Solution without any dependency: [/python/web-development/django/4-cms-admin/1-customizing/cms-views-based-on-selection-with-no-dependency](/python/web-development/django/4-cms-admin/1-customizing/cms-views-based-on-selection-with-no-dependency.md)
- Solution with `django-polymorphic`: [/python/web-development/django/4-cms-admin/1-customizing/cms-views-based-on-selection](/python/web-development/django/4-cms-admin/1-customizing/cms-views-based-on-selection.md)

---
## C) Detail-view listing inline entries from another model class:

Regardless new or existing object, you wanna see an *inline* table where every row comes from another model class object. You must add and/or remove each row if needed;

[/python/web-development/django/4-cms-admin/1-customizing/detailview-inline-data-from-another-model.py](/python/web-development/django/4-cms-admin/1-customizing/detailview-inline-data-from-another-model.py)

---
## D) xxxxxxxxx

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

- D1. xxxxxxxxxxx
- D1. xxxxxxxxxxx
- D1. xxxxxxxxxxx

---
## CSS customization in Django Admin:
[/python/web-development/django/4-cms-admin/1-customizing/css-customization-in-admin](/python/web-development/django/4-cms-admin/1-customizing/css-customization-in-admin.md)
