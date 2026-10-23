#### Python > Django > Forms > QuerySets examples
# Example X

---
## Business Rule:
- A `xxxxxxxxxx` can be used only once per `xxxxxxxxx`.
- Limit the `comp_concept` field choices with only those `xxxxxxxxxxx` instances never used by other `xxxxxxxxxxxx` instance of the same `xxxxxxxxxxx`.
## Context:
You're creating a new instance of *Friendly Class Name* (`<ClassNameOnModel>`) where the adding detail-view is split by [2 screens flow (this solution)](python/web-development/django/4-cms-admin/1-customizing/cms-multi-step-adding-using-session.md). 
- Screen 1: the user picks the `xxxxxx` and hits "next" button. Only the chosen value is kept in `request.session` (nothing is written to the db).
- Screen 2: the form loads an unsaved instance (`pk` is `None`) built with the `xxxxxxxx` from the session. After "Save" it has a `pk`.
```python
# models.py
class ClassName(...):
	xxxxx = models.ForeignKey("ClassName", ...)  # It auto-created xxxxxx_id attr/column locally.
	xxxxx = models.ForeignKey("ClassName", ...)  # It auto-created xxxxxx_id attr/column locally.
	
class ClassName(...):
	# ...
	
class ClassName(...):
	# ...
```
## Solution:
```python
# forms.py
class SomethingAdminForm(forms.ModelForm):
	#...
	
	def __init__(...):
		super().__init__(...)
		
		xxxxxxxxxxxxxxx
```
## Output result:
- Screen 2:
	- For new instance not saved: `xxxxxxxx` offering only its instances that xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
	- For existing instance: the same result of the unsaved one, but xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.

---


