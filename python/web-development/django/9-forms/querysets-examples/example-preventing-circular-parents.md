#### Python > Django > Forms > QuerySets examples
# Preventing circular parents

---
## Business Rule:
- `Fruit` owns none, one or many `Fruit`.
- `Fruit` "A" cannot own `Fruit` "B" if `Fruit` "B" already owns `Fruit` "A" (circular parent issue).
## Context:
You're creating a new instance of *Fruit* (`Fruit`).
```python
# models.py
class Fruit(...):
	owner_of = models.ForeignKey("self", ...)  # It auto-created owner_of_id attr/column locally.
```
## Solution:
In `models.py`:
```python
class Fruit(...):
	# ...
	
	def get_descendant_ids(self) -> set[int]:
		"""Returns PKs of every instance below this one, at any depth."""
		descendant_ids: set[int] = set()
		frontier = [self.pk]
		while frontier:
			children_ids = (
				set(
					type(self)
					.objects.filter(owner_of__in=frontier)
					.values_list("pk", flat=True)
				)
				- descendant_ids
			) # The subtraction also protects against bad legacy data!!!
			descendant_ids.update(children_ids)
			frontier = list(children_ids)
		return descendant_ids
```
In `forms.py`:
```python
class FruitAdminForm(forms.ModelForm):
	#...
	
	def __init__(...):
		super().__init__(...)
		
		# OWNER_OF QUERY:
		owner_of = self.fields["owner_of"]
		# Creating the QuerySet:
		if isinstance(owner_of, forms.ModelChoiceField):
			# Reserved space for logic for brand new fruit instance... For this example, it's not needed once this is a new instance been created, making it unknown for any other instance yet:
			available_fruits = models.Fruit.objects
			
			# For existing instance:
			if self.instance.pk is not None:
				# Remove this instance (and all its descendants) to prevent circular parents:
				excluded_ids = {self.instance.pk, *self.instance.get_descendant_ids()}
				available_fruits = available_fruits.exclude(pk__in=excluded_ids)
			# Finally, offer (.queryset) only the right owner_of instances:
			owner_of.queryset = available_fruits
```
(Optional) Again in `models.py`
```python
class Fruit(...):
	# ...
	
	def clean(self):
		'''...'''
		super().clean()
		if self.pk and self.owner_of_id and (self.owner_of_id == self.pk or self.owner_of_id in self.get_descendant_ids()):
			raise ValidationError(
				{"owner_of": "A fruit cannot owned of itself, nor owned of those already owned it."}
			)
```
## Output result:
- For new instance not saved: `owner_of` field will be loaded normally, with all its options available.
- For existing instance: `owner_of` field will be loaded with all its options, except the current instance and all other options that is using the current instance as their `owner_of`.

---


