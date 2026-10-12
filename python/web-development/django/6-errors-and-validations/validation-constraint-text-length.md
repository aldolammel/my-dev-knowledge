DJANGO FORM VALIDATIONS > DB CONSTRAINTS: TEXT WITH LENGTH CHECK

### Unsupported lookup?
In case of a "Unsupported lookup" error message for `length` or `length_range` during the `migrate` command, just register that lookup on the right `models.py`:
```python
from django.db.models.functions import Length
models.CharField.register_lookup(Length)
```
### E.g., ensure a txt field has minimum of X chars amount
```python
class PagexCategory(models.Model):
	# ...
	cat = models.CharField(...)

	class Meta:
		# ...
		constraints = [
			models.CheckConstraint(
				condition=models.Q(cat__length__gte=3),
				name="category_cat_min_length",
			)
		]
```
What will take place in db:
```shell
ALTER TABLE pagex_category
ADD CONSTRAINT cat_min_length
CHECK (LENGTH(cat) >= 3);
```
### E.g., ensure a txt field has minimum and maximum chars amount
```python
class PagexCategory(models.Model):
	# ...
	cat = models.CharField(...)

	class Meta:
		# ...
		constraints = [
			models.CheckConstraint(
				condition=models.Q(cat__length__range=(consts.VAL_TITLE_MIN, consts.VAL_TITLE_MAX)),
				name="category_cat_length",
			),
		]
```
What will take place in db:
```shell
ALTER TABLE pagex_category
ADD CONSTRAINT cat_length 
CHECK (LENGTH(cat) >= 3 AND LENGTH(cat) <= 100);
```

---

