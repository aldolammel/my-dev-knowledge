#### Python > Django > Validations > Constraints
# Uniqueness of fields (simplest & combined solutions)

---

You can define a field is unique or a combination of them to create the uniqueness. Let's see both cases.

---
## A) Using `unique=True` for basic:
```python
# models.py:
class Something(...):
	name = models.CharField(
		...
		unique=True,  # Enforces a UNIQUE constraint at the db-level.
	)
```

**How it works across Django layers:**
- **Database level:** Creates a `UNIQUE` constraint on the table column to guarantee data integrity at the DB level.
- **ModelForm & Admin level:** Django automatically generates validation rules for forms and the admin panel, catching duplicates _before_ saving and displaying a clean form error rather than a database integrity crash.
- **Template level:** Templates only render the error messages passed down by the form.
---
## B) Using `UniqueConstraint()` to create combined uniqueness
The individual fields don't need to be unique. Only their combination does. This constraint means that the combination of `platform`, `proc_type` and `created_by` must be unique.
```python
# models.py:
from django.db import models
from django.db.models import Q

class Procedure(models.Model):
    platform = models.ForeignKey(...)
    proc_type = models.ForeignKey(...)
    created_by = models.ForeignKey(...)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
	                "platform",
	                "proc_type",
	                "created_by",  # created_by demands this model admin form actions!
				],
                name="unique_procedure_type_and_platform_per_user",  # be specific, be accurate to name it!
                nulls_distinct=False, # Django 5.0+, PostgreSQL 15+
                violation_error_message="You already created this procedure type associated with the current platform.",
            ),
        ]
```
Now, run `makemigrations` and `migrate` commands.

Done!
### Are you getting `IntegrityError`?
If so, it's because you're using, in *UniqueConstraint* `fields=[]`, one or more class attributes/fields using `editable=False` argument, what means these attributes are excluded and not deliver to the form (in this case, `created_by` is `editable=False`). Once the ModelForm `clean()` runs, the form has no idea who the logged-in user is. It happens because forms don’t have access to `request` by default. To pass the current user to the form’s `clean()`, first, let's create a custom form that will figure out who is the current user. Do it:

In `forms.py`:
```python
class ProcedureAdminForm(forms.ModelForm):
	"""..."""
	
	class Meta:
		# Model tied used to populate it:
		model = models.Procedure
		# Bringing specific fields from the model:
		fields = "__all__"

	def __init__(self, *args, request=None, **kwargs):
		"""Dunder method called 'constructor' that runs automatically when a class instance is created."""
		super().__init__(*args, **kwargs)
		# Why I'm using this dunder init + request to extract the current user:
		# Once created_by is editable=False, it doesn't exist to the form, making clean() blocked to validate that field. Unfortunately, neither save_model() cannot tell me which user is here because the UniqueConstraints validation trigger first, creating an error on screen. To to create a friendly message on the form (app-level) with a field not present originally, I need to request the user from other way (this one below):
		self.request = request
		
		# __init__ extra fields, pre-populating:
		# Unlike fields from connected model, extra fields must be manually linked!
		# Reserved space...
	
	def clean(self):
		"""Built-in Form method to cross-field custom validations at the form level that runs after individuals' clean. Reminder: any clean isn't allowed directly in admin.py."""
		cleaned_data = super().clean() or {}
		
		# Those model UniqueConstraint fields, except the editable=False ones:
		keys = ("platform", "proc_type")
		if any(key in self.errors for key in keys):
			return cleaned_data
		
		# Once we know who's the current user, let's keep the data even though no obj instance yet:
		author = self.instance.created_by if self.instance.pk else self.request.user
		
		# If current instance is violating the model UniqueConstraint rule per user, warn it:
		if (
			models.Procedure.objects.filter(
				created_by=author,
				# dict comprehension:
				**{
					key: (
						cleaned_data[key]
						if key in cleaned_data
						else getattr(self.instance, f"{key}_id")
					)
					for key in keys
				},
			)
			.exclude(pk=self.instance.pk)
			.exists()
		):
			raise forms.ValidationError("You already created this procedure type associated with the current platform.")
		return cleaned_data
		
	# Extra form fields (Not tied to the model):
	# Reserved space...
```

After that, tie the custom form in the right admin model:

In `admin.py`:
```python
@admin.register(...)
class ProcedureAdmin(...):
    
    # Custom form:
	form = forms.ProcedureAdminForm
	
	# ...
```

Still in `admin.py`, if you are NOT using [multi-step adding detail-view](/python/web-development/django/4-cms-admin/1-customizing/cms-multi-step-adding-using-session.md), do it below, otherwise, take the further `get_form()` solution:
```python
    def get_form(self, request, obj=None, change=False, **kwargs):
		"""Built-in admin method to customize the form that's displayed in the interface."""
		form = super().get_form(request, obj, change, **kwargs)
		
		class RequestForm(form):  # Type: ignore[valid-type]
			def __init__(self, *args, **inner_kwargs):
				"""Dunder method called 'constructor' that runs automatically when a class instance is created."""
				super().__init__(*args, request=request, **inner_kwargs)
			
		return RequestForm
```
Or this solution for [multi-step adding detail-view](/python/web-development/django/4-cms-admin/1-customizing/cms-multi-step-adding-using-session.md):
```python
	def get_form(self, request, obj=None, change=False, **kwargs):
		"""..."""
		form = super().get_form(request, obj, change=change, **kwargs)
		locked = request.session.get(consts.STR_SOMETHING_SESSION_KEY, {}) if obj is None else {}
		
		class MultiStepForm(form): # type: ignore[valid-type, misc]
			def __init__(self, *args, **kw):
				"""..."""
				# Admin passes no instance on add (GET or POST).
				if obj is None and kw.get("instance") is None:
					kw["instance"] = build_multi_screen_instance(models.ProcTypeGroup, locked)
				kw["request"] = request
				super().__init__(*args, **kw)
		
		return MultiStepForm
```

Done! The combined `UniqueConstraint` with one or more fields using `editable=False` argument will work fine.

---
## Conditional example - demands `UniqueConstraint()`
E.g., email must be unique only if the user is active:
```python
# FILE: /apps/my_app/models.py
from django.db import models
from django.db.models import Q

class UserProfile(models.Model):
	email = models.EmailField()
	is_active = models.BooleanField(default=True)

	class Meta:
		# ...
		constraints = [
			models.UniqueConstraint(
				fields=["email"],
				condition=Q(is_active=True),
				name="unique_active_email"
			)
		]
```
How Django translates it to SQL:
```sql
CREATE UNIQUE INDEX "unique_active_email"
ON "userprofile" ("email")
WHERE "is_active";
```

---
## Does it replace `clean()`?
For uniqueness rules, often yes. For business validation in general, no, you need the [clean() method](/python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form.md).

---
## Other db-level constraint types:
[/python/web-development/django/6-errors-and-validations/validation-1-for-database](/python/web-development/django/6-errors-and-validations/validation-1-for-database.md)
## This constraint type on SQL:
[/database/constraint-type-unique](/database/constraint-type-unique.md)


