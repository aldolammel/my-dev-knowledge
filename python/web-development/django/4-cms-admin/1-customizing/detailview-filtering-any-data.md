#### Python > Django > CMS
# Filtering a drop-down in a CMS form (using QuerySets)

---
## Before:

- What are QuerySets: [/python/web-development/django/3-1-models-database/4-querysets/\_what-is-queryset.md](/python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset.md)

---
## In `forms.py` (RECOMMENDED):

Sometimes, the best way to do this is edit the custom form of that admin class or create one to set this filtering! The great stuff in to filtering through the form class is the way is reproduced to the app's front-end easily, and not just for CMS: [/python/web-development/django/9-forms/form-queryset-filtering-dropdown](/python/web-development/django/9-forms/form-queryset-filtering-dropdown.md)

---
## Filtering directly in `admin.py`:

Solutions:
- Filtering objects directly from the database (Not recommended): [/python/web-development/django/4-cms-admin/method-get_queryset.py](/python/web-development/django/4-cms-admin/method-get_queryset.py)
- Filtering from a field/attribute (drop-down): [/python/web-development/django/4-cms-admin/method-formfield_for_foreignkey](/python/web-development/django/4-cms-admin/method-formfield_for_foreignkey.md)

---

