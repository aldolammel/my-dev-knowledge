#### Python > Django > Forms > QuerySets examples
# Example, dealing with a self-referential field

---
## Business Rule:
- A `CompBase` can refer only to another `CompBase` of the same `Plane`.
- A `CompBase` can never refer to itself.
- Limit the `comp_ref` field choices to the `CompBase` instances of the same `Plane`, excluding the instance being edited.
## Context:
You're creating a new instance of *Component Base* (`CompBase`) where the adding detail-view is split by [2 screens flow (this solution)](python/web-development/django/4-cms-admin/1-customizing/cms-multi-step-adding-using-session.md). 
- Screen 1: the user picks the `plane` and hits "next" button. Only the chosen value is kept in `request.session` (nothing is written to the db).
- Screen 2: the form loads an unsaved instance (`pk` is `None`) built with the `plane_id` from the session. After "Save" it has a `pk`.
```python
# models.py
class CompBase(...):
	plane = models.ForeignKey("Plane", ...)  # It auto-created plane_id attr/column locally.
	comp_ref = models.ForeignKey("self", ...)  # It auto-created comp_ref_id attr/column locally.
	
class Plane(...):
	# ...
```
## Solution:
```python
# forms.py
class SomethingAdminForm(forms.ModelForm):
	#...

	def __init__(...):
		super().__init__(...)
		  
		# 1) The plane comes from the current instance (from request.session if a new adding):
		plane_id = self.instance.plane_id
		# The plane is the core of this query:
		if plane_id is not None:
		
			# 2) Creating the QuerySet (filtering):
			# Defining which form field demands a new query:
			comp_ref = self.fields["comp_ref"]
			if isinstance(comp_ref, forms.ModelChoiceField):
				available_comps = models.CompBase.objects.filter(
					# CompBase instances using the same plane:
					plane_id=plane_id,
				)
			
			# For existing instance (saved):
			if self.instance.pk is not None:
				# Self-referential model: exclude itself, so it can't refer to itself:
				available_comps = available_comps.exclude(pk=self.instance.pk)
			
			# 3) Finally, offer (.queryset) only the CompBase instances of the same plane (except itself):
			comp_ref.queryset = available_comps
```
## Output result:
- Screen 2:
	- For new instance not saved: `comp_ref` offers only the `CompBase` instances of the same `plane`. There is nothing to exclude yet, since the instance doesn't exist.
	- For existing instance: the same result, but without the instance itself, so it can't be selected as its own reference.

---


