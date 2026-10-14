DJANGO > MODELS: INHERITING METHODS

---

**Before:**
- What is method: [/dev-concepts/oop-class-method](/dev-concepts/oop-class-method.md)

**How method inheritance works:**

- Child class can extend its parent's methods actions with no lost;
	- A parent method is NOT called automatically through the child;
		- You must explicitly call it using super().

**So this is the golden rule:**

- If you want to extend behavior from Parent to Child, call super();
- If you forget super(), the Parent logic is skipped;
- Don't call full_clean() in child if their parent already did it;
	- If Parent already did it, in Child use super().clean().

---
## Examples:
### Parent model class
```python
class ParentModel(models.Model):
	...parent attributes here...


	def save(self, *args, **kwargs):
		# 1. Runs full validation before saving:
		self.full_clean()

		# 2. Save logic will run only here through its model!

		# 3. Saving the data in the db:
		super().save(*args, **kwargs)


	def clean(self):
		# Clean validations will run only here through its local attributes!
```
### Child model class
```python
class ChildModel(ParentModel):
	...child attributes here...


	def save(self, *args, **kwargs):
		# NEVER CALL "self.full_clean()" IN CHILD IF PARENT ALREADY CALLS!

		# 1. The saving logic you wanna work here!

		# 2. Saving the data (including changes in parent via this child) in the db:
		super().save(*args, **kwargs)


	def clean(self):
		# 1. Allows the parent class to execute full_clean() in this child too:
		super().clean()  # <-- Exactly, not full_clean() here, just clean()!

		# 2. Clean validations for this child runs.

```

---

**Mixin model type:**
- A great way to share methods among many classes: [/python/web-development/django/3-1-models-database/model-type-mixin](/python/web-development/django/3-1-models-database/model-type-mixin.md)

**Base model type:**
- Also a way to share methods among many classes: [/python/web-development/django/3-1-models-database/model-type-base](/python/web-development/django/3-1-models-database/model-type-base.md)

