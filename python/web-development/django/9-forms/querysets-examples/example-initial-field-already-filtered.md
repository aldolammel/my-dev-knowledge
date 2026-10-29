#### Python > Django > Forms > QuerySets examples
# Initial field already filtered

---
## Business Rule:
- A `Fruit` is owned by one `Planet`.
- A `Planet` owns none, one or more `Fruit`.
## Context:
You're creating a new instance of *Fruit* (`Fruit`). 
```python
# models.py
class Planet(...):
	# ...
	is_active = models.BooleanField(...)
	
class Fruit(...):
	planet = models.ForeignKey("Planet", ...)  # It auto-created planet_id attr/column locally.
	# ...

```
## Solution:
```python
# forms.py
class FruitAdminForm(forms.ModelForm):
	#...
	
	def __init__(...):
		super().__init__(...)
		
		# PLANET QUERY
		# If a planet is not active, remove it from the initial field options:
		planet = self.fields["planet"]
		# Creating the QuerySet:
		if isinstance(planet, forms.ModelChoiceField):
			# No matter if new or existing instance, do it:
			# Offer (.queryset) only the right planet instances:
			planet.queryset = models.Planet.objects.filter(is_active=True)
```
## Output result:
- For new instance not saved: `planet` field will offer only its instances that are `is_active=True`.
- For existing instance: the same result described above.

---


