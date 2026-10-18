#### Python > Django > Admin (CMS) > Form soluctions
# Adding an instance with multi-step form

---

**What kind of form do you need (summary):** 
- [/python/web-development/django/4-cms-admin/\_what-kind-of-cms-ux-do-you-need](/python/web-development/django/4-cms-admin/_what-kind-of-cms-ux-do-you-need.md)

For new objects, through the adding detail-view, select an option first (using a radio or drop-down menu), and then Django loads the specific form (still in detail-view) based on the previous selection. For existing entries through the list-view, each listed entry, if clicked, loads its specific form based in a specific model (with its unique fields);

---
## 1) Make sure the project has `django-polymorphic` as an app-level core dependency:
[/python/web-development/django/component-libraries/django-polymorphic/0-djangopolymorphic](/python/web-development/django/component-libraries/django-polymorphic/0-djangopolymorphic.md)

---
## 2) In `models.py`, add `PolymorphicModel` inheritance to each model class you wanna consider as specific form in CMS:

E.g.
```python
class CommonForPeople(PolymorphicModel, models.Model):  # type: ignore[django-manager-missing]  # If MyPy warning it!
	name = ...
class OnlyForMale(CommonForPeople):  # CMS reads it as a specific form for men.
	balls_amount = ...
class OnlyForFemale(CommonForPeople):  # Same logic here.
	pms_cases_by_year = ...
```

---
## 3) In `admin.py`:

E.g.
```python
from polymorphic.admin import (
	PolymorphicParentModelAdmin,
	PolymorphicChildModelAdmin,
)
```

**Child:**
```python
@admin.register(models.OnlyForMale)
class OnlyForMaleAdmin(PolymorphicChildModelAdmin):
	base_model = models.OnlyForMale  # Declared here too only for Polymorphic purpose!
	show_in_index = False  # hide link from CMS home (sidebar menu still shown)

	# Cause you need CMS audit:
	def save_model(self, request, obj, form, change):
		obj.save(user=request.user)
```

And so on for all form options...

**Parent:**
```python
@admin.register(models.CommonForPeople)
class CommonForPeopleAdmin(PolymorphicParentModelAdmin):
	base_model = models.CommonForPeople  # Declared here too only for Polymorphic purpose!
	child_models = (
		models.OnlyForMale,    # First on this tuple's treated as the default!
		models.OnlyForFemale,
	)
	list_display = ("name", "slug", "polymorphic_ctype")
	list_filter = ("polymorphic_ctype",)

	# Cause you need CMS audit:
	def save_model(self, request, obj, form, change):
		obj.save(user=request.user)
```

---
## CSS customization in Django Admin:
[/python/web-development/django/4-cms-admin/1-customizing/css-customization-in-admin](/python/web-development/django/4-cms-admin/1-customizing/css-customization-in-admin.md)

