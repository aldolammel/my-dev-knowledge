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
        '''Dunder method called 'constructor' that runs automatically when a class instance is created.'''
        
        # 'seller' is the authenticated User that I need for specific example:
        seller = kwargs.pop('seller', None)
        super().__init__(*args, **kwargs)
        
        # Once the user exists and they got a brand attribute:
        if seller and seller.brand:
			# Now, I am replacing the original data associated with these fields below by a new filtered data:
			
            ## (Simplest version):
            self.fields['sold_vehicle'].queryset = models.Vehicle.objects.filter(brand=seller.brand)  # type: ignore[attr-defined]
            
            ## (Safier version):
            sold_veh = self.fields["sold_vehicle"]
            if isinstance(sold_veh, forms.ModelChoiceField): # Basically you likely will use this field type in here!
                sold_veh.queryset = models.Vehicle.objects.filter(brand=seller.brand)
            
		# Extra fields, pre-populating:
		# Unlike fields from tied model, extra fields must be manually linked!
		# Reserved space...
            
	# Extra form fields (Not tied to the model):
	# Reserved space...
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

