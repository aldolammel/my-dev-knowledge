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
                fields=["platform", "proc_type", "created_by"],  # No limit for combination!
                name="unique_procedure_type_and_platform_per_user",  # be specific, be accurated to name it!
                nulls_distinct=False, # Django 5.0+, PostgreSQL 15+
                violation_error_message="You already created this procedure type associated with the current platform.",
            ),
        ]
```
Now, run `makemigrations` and `migrate` commands.
### Are you getting `IntegrityError`?
If so, it's because you're using in `fields=[]` a class attribute/field that uses `editable=False`, what means this attribute is excluded and not delivered to the form (in this case, `created_by` is `editable=False`). At ModelForm `clean()` time the form has no idea who the logged-in user is, because forms don’t have access to `request` by default. To pass the user to the form’s `clean()`, first, let's create a custom form that will figure out who is the current user:

In `forms.py`:
```python
class ProcedureAdminForm(forms.ModelForm):
	class Meta:
		model = models.Procedure
		fields = "__all__"
	
	def __init__(self, *args, request=None, **kwargs):
		"""Dunder method called 'constructor' that runs automatically when a class instance is created."""
		super().__init__(*args, **kwargs)
		# In order to tell the ProcedureAdmin form who is the current user without to depend of the save_model() method (too late for this case):
		self.request = request
	
	def clean(self):
		"""Built-in Form method to cross-field custom validations at the form level that runs after individuals' clean. Reminder: any clean isn't allowed directly in admin.py."""
		cleaned_data = super().clean()
		keys = ("platform", "proc_type")
		
		if any(key in self.errors for key in keys):
			return cleaned_data
		
		# Once now finally we know who is the current user, let's tell it even if the instance doesn't exist yet:
		author = self.instance.created_by if self.instance.pk else self.request.user
		# If current procedure and type exists for the user (now we know who is it), warn them:
		if (
			models.Procedure.objects.filter(
				created_by=author,
				# dict comprehension:
				**{key: cleaned_data.get(key) for key in keys},  # Type: ignore[union-attr]
			)
			.exclude(pk=self.instance.pk)
			.exists()
		):
			raise forms.ValidationError("You already created this procedure type associated with the current platform.")
		return cleaned_data
```

After that, tie the custom form in the right admin model:

In `admin.py`:
```python
@admin.register(...)
class ProcedureAdmin(...):
    
    # Custom form:
	form = forms.ProcedureAdminForm
	
	# ...
	
    def get_form(self, request, obj=None, change=False, **kwargs):
		"""Built-in CMS method to customize the form that's displayed in the interface."""
		form = super().get_form(request, obj, change, **kwargs)
		
		class RequestForm(form):  # Type: ignore[valid-type]
			def __init__(self, *args, **inner_kwargs):
				"""Dunder method called 'constructor' that runs automatically when a class instance is created."""
				super().__init__(*args, request=request, **inner_kwargs)
			
		return RequestForm
```
Done! The combined `UniqueConstraint` with a non-form field has friendly warn message if something wrong.

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


