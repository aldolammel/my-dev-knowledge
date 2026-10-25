a#### Python > Django > Forms > QuerySets examples
# Example 3

---
## Business Rule:
- A `CompConcept` can be used only once per `Plane`.
- Limit the `comp_concept` field choices with only those `CompConcept` instances never used by other `CompBase` instance of the same `Plane`.
## Context:
You're creating a new instance of *Component Base* (`CompBase`) where the adding detail-view is split by [2 screens flow (this solution)](python/web-development/django/4-cms-admin/1-customizing/cms-multi-step-adding-using-session.md). 
- Screen 1: the user picks the `plane` and hits "next" button. Only the chosen value is kept in `request.session` (nothing is written to the db).
- Screen 2: the form loads an unsaved instance (`pk` is `None`) built with the `plane_id` from the session. After "Save" it has a `pk`.
```python
# models.py
class CompBase(...):
	plane = models.ForeignKey("Plane", ...)  # It auto-created plane_id attr/column locally.
	comp_concept = models.ForeignKey("CompConcept", ...)  # It auto-created comp_concept_id attr/column locally.
	
class Plane(...):
	# ...
	
class CompConcept(...):
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
			comp_concept = self.fields["comp_concept"]
			if isinstance(comp_concept, forms.ModelChoiceField):
				used_concepts = models.CompBase.objects.filter(
					# CompBase instances using the same plane:
					plane_id=plane_id,
					# But only those CompBase instances whose comp_concept exist:
					comp_concept__isnull=False,
				)
				# For existing instance (non-session):
				if self.instance.pk is not None:
					# Remove this instance from used_concepts to keep it as current value on field:
					used_concepts = used_concepts.exclude(pk=self.instance.pk)

				# 3) Finally, offer (.queryset) only comp_concept instances that aren't in use:
				comp_concept.queryset = models.CompConcept.objects.exclude(
					# Every CompConcept whose pk ISN'T among the comp_concept_ids already used in this plane:
					pk__in=used_concepts.values("comp_concept_id"),
				)
```
## Output result:
- Screen 2:
	- For new instance not saved: `comp_concept` offering only its instances that weren't used by any other `CompBase` instance associated with the same `plane`.
	- For existing instance: the same result of the unsaved one, but preserving the current saved `comp_concept` instance as `comp_concept` options to select.

---


