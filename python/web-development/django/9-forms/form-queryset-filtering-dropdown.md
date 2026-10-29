#### Python > Django > Forms
# Filtering a drop-down in a form (using QuerySets)

---
## Before:
- What are QuerySets? [/python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset](/python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset.md)
- ModelForm templates: [/python/web-development/django/9-forms/\_form-class-model.py](/python/web-development/django/9-forms/_form-class-model.py)

---
## 1) Creating or editing the custom form:
Creating/editing a custom form, let's tell to Django filter a specific field options before it be rendered in CMS (and app's front-end form if applicable).
```python
from typing import Any
from django import forms 
from . import models

class SomethingAdminForm(...):
    # ...
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
		"""Dunder method called 'constructor' that runs automatically when a class instance is created."""
		super().__init__(*args, **kwargs)
		
		# REMEMBER WHY to use 'attrname_id' instead of attrname.pk or .id:
		# /python/web-development/django/3-1-models-database/4-querysets/attname.md
		
		# The family comes from the current instance (or from request.session if a new adding):
		family_id = self.instance.family_id
		# If the aircraft exists:
		if family_id is not None:
			# COMP_SHAPE QUERY:
			# comp_shape offering only its shapes that are compatible (comp_concept_type) with the selected comp_concept on the form.
			# Defining the field:
			comp_shape = self.fields["comp_shape"]
			# Creating the QuerySet:
			if isinstance(comp_shape, forms.ModelChoiceField):
				available_shapes = models.CompShape.objects.filter(
					# Filtering shapes to be only those with the same type of selected comp_concept:
					comp_concept_type=self.instance.comp_concept.comp_concept_type
				)
				# For existing instance (non-session):
				if self.instance.pk is not None:
					# Remove this instance from used_concepts to keep it as current value on field:
					available_shapes = available_shapes.exclude(pk=self.instance.pk)
				# Finally, offer (.queryset) only the right comp_concept instances:
				comp_shape.queryset = available_shapes
			
			# COMP_REF QUERY:
			# In comp_ref field, exclude itself from the drop-down menu options (because this model if self-referential), and exclude those components that don't belong the same aircraft:
			# Defining the field:
			comp_ref = self.fields["comp_ref"]
			# Creating the QuerySet:
			if isinstance(comp_ref, forms.ModelChoiceField):
				available_comps = models.CompBase.objects.filter(
					# CompBase instances using the same aircraft:
					family_id=family_id
				)
				# For existing instance (non-session):
				if self.instance.pk is not None:
					# Remove this instance from comp_ref to keep it as current value on field:
					available_comps = available_comps.exclude(pk=self.instance.pk)
				# Finally, offer (.queryset) only the right comp_ref instances:
				comp_ref.queryset = available_comps
				
		# __init__ extra fields, pre-populating:
		# Unlike fields from tied model, extra fields must be manually linked!
		# Reserved space...
		
	# ...
```
### Another example when you wanna exclude the current instance when the model is self-referential:
```python
from typing import Any
from django import forms 
from . import models

class SomethingAdminForm(...):
    # ...

	def __init__(self, *args: Any, **kwargs: Any) -> None:
		"""..."""
		super().__init__(*args, **kwargs)

		# Exclude itself from the drop-down menu options (because this model if self-referential):
		comp_ref = self.fields["comp_ref"]
		if isinstance(comp_ref, forms.ModelChoiceField):
			comp_ref.queryset = models.CompBase.objects.exclude(pk=self.instance.id)
			
		# __init__ extra fields, pre-populating:
		# Unlike fields from tied model, extra fields must be manually linked!
		# Reserved space...
			
	# ...
```
What is self-referential model: [/python/web-development/django/3-1-models-database/relation-self-referential](/python/web-development/django/3-1-models-database/relation-self-referential.md)
### One more example, commonly used to filter a form field depending its previous form selection:
```python
from typing import Any
from django import forms 
from . import models

class SomethingAdminForm(...):
    # ...

	def __init__(self, *args: Any, **kwargs: Any) -> None:
		"""..."""
		# ...
		# Sometimes plane_seat field is not available in the form (because could be readonly_field):
		# Seat options should respect which plane's procedure is loaded on screen:
		if "plane_seat" in self.fields:
			# Defining the object (procedure) that the plane_model attr. exists:
			procedure = self.instance.procedure if self.instance.procedure.id else None
			# Taking the procedure plane_model's ID:
			plane_model_id = procedure.plane_model_id if procedure else None
			# Finally, loading only those PlaneSeat instances that the plane_model are the same of the procedure plane_model already selected on the form:
			plane_seat = self.fields["plane_seat"]
			if isinstance(plane_seat, forms.ModelChoiceField):
				plane_seat.queryset = models.PlaneSeat.objects.filter(plane_model_id=plane_model_id)
		
		# __init__ extra fields, pre-populating:
		# Unlike fields from tied model, extra fields must be manually linked!
		# Reserved space...
	
	# ...
```

---
## 2) Tying the form to its admin class:
```python
from . import forms, models

@admin.register(models.Something)
class SomethingAdmin(admin.ModelAdmin):
    
    # Custom form:
    form = forms.SomethingAdminForm
    
    # ...
```
Case you need a ModelAdmin template: [/python/web-development/django/4-cms-admin/\_admin-class-model.py](/python/web-development/django/4-cms-admin/_admin-class-model.py)

---
## (If applicable) VIEWS.PY:
Make sure your View FBV or CBV has in its Context the 'form' with 'seller' data!
## Alternatively, check this admin.py solution for drop-down filtering (Not recommended):
[/python/web-development/django/4-cms-admin/1-customizing/detailview-filtering-any-data](/python/web-development/django/4-cms-admin/1-customizing/detailview-filtering-any-data.md)

