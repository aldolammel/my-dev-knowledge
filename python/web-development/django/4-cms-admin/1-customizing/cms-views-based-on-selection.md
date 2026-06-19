#### Python > Django > Admin (CMS)
# What kind of form do you need: "B" 

---

**What kind of form do you need (summary):** 
[python/web-development/django/4-cms-admin/\_what-kind-of-cms-ux-do-you-need](python/web-development/django/4-cms-admin/_what-kind-of-cms-ux-do-you-need.md)

---

For new objects, through the adding detail-view, select an option first (using a radio or drop-down menu), and then Django loads the specific form (still in detail-view) based on the previous selection. For existing entries through the list-view, each listed entry, if clicked, loads its specific form based in a specific model (with its unique fields);
## B1) Install the dependency 'PolymorphicModel':
[python/web-development/django/component-libraries/django-polymorphic/0-djangopolymorphic](python/web-development/django/component-libraries/django-polymorphic/0-djangopolymorphic.md)
## B2) In models.py, add 'PolymorphicModel' inheritance to each model class you wanna consider as specific form in CMS:

E.g.
```
class CommonForPeople(PolymorphicModel, models.Model):  # type: ignore[django-manager-missing]  # If MyPy warning it!
	name = ...
class OnlyForMale(CommonForPeople):  # CMS reads it as a specific form for men.
	balls_amount = ...
class OnlyForFemale(CommonForPeople):  # Same logic here.
	pms_cases_by_year = ...
```
## B3) In *admin.py*:

E.g.
```
from polymorphic.admin import (
	PolymorphicParentModelAdmin,
	PolymorphicChildModelAdmin,
)
```

**Child:**
```
@admin.register(models.OnlyForMale)
class OnlyForMaleAdmin(PolymorphicChildModelAdmin):
	base_model = models.OnlyForMale
	show_in_index = False  # hide link from CMS home (sidebar menu still shown)

	# Cause you need CMS audit:
	def save_model(self, request, obj, form, change):
		obj.save(user=request.user)
```

And so on for all form options...

**Parent:**
```
@admin.register(models.CommonForPeople)
class CommonForPeopleAdmin(PolymorphicParentModelAdmin):
	base_model = models.CommonForPeople
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
[python/web-development/django/4-cms-admin/1-customizing/css-customization-in-admin](python/web-development/django/4-cms-admin/1-customizing/css-customization-in-admin.md)
