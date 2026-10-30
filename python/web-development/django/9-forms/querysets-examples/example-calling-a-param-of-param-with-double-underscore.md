#### Python > Django > Forms > QuerySets examples
# Calling a param of param ( _ _ lookups)

---
## Business Rule:
- A `Fruit` is owned by one `Variety`.
## Context:
You're creating a new instance of *Fruit* (`Fruit`). 
```python
# models.py
class VarietyFamily(...):
    # ...

class Variety(...):
    family = models.ForeignKey("VarietyFamily", ...)  # It auto-created family_id attr/column locally.

class Fruit(...):
    variety = models.ForeignKey("Variety", ...)  # It auto-created variety_id attr/column locally.
```
## Solution:
```python
# forms.py
class FruitAdminForm(forms.ModelForm):
	#...
	
	def __init__(...):
		super().__init__(...)
		
		# FRUIT QUERY
		# If fruit is not from a specific family, remove it from the initial field options:
		fruit = self.fields["fruit"]
		# Creating the QuerySet:
		if isinstance(fruit, forms.ModelChoiceField):
			variety = self.instance.variety_id if self.instance and self.instance.variety_id else None
			family_id = self.instance.variety.family_id if self.instance.variety_id and self.instance.variety.family_id else None
			# No matter if new or existing instance, do it:
			# Offer (.queryset) only the right fruit instances:
			fruit.queryset = models.Fruit.objects.filter(
				variety__family_id=family_id,  # Apply conditional queryset filtering using __id lookups!
			)
```
## Output result:
- For new instance not saved: `fruit` field will offer only its instances that the `variety` instance's `family` belongs a specific `family_id`.
- For existing instance: the same result described above.

---


