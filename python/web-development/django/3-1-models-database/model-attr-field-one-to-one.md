#### Python > Django > Models > Field Classes (Attribute types)
# OneToOneField()

---
**Before:**
1. What is *One-to-One* in a database: [/database/\_tools/ERD/one-to-one](/database/_tools/ERD/one-to-one.md)

---

Defining a *One-to-One* relationship between two models. This is often used for [model inheritance or extending a model](/python/web-development/django/3-1-models-database/model-type-base.md) with additional information. In fact, Django's `OneToOneField` is literally just a subclass of  [ForeignKey()](/python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md) using `ForeignKey(unique=True)` under the hood. But the BEST DJANGO PRACTICE is always to use `OneToOneField()` to build up an one-to-one relationship between two models.

**Field look-like on front-end:**
`<select>` (single-selection only)

Example:
```python
class Person(models.Model):
    name = models.CharField(
	    max_length=100
    )

class IDCard(models.Model):
    person = models.OneToOneField(
	    Person,
	    on_delete=models.CASCADE,
	    related_name='id_card'  # In this case the related_name is not plural once it's a one to one relation.
	    null=True,
		blank=False,
	    verbose_name="xxxxxx",
		help_text="",
	)
    card_number = models.CharField(
	    max_length=20,
	    unique=True,
	    null=True,
		blank=False,
	    verbose_name="xxxxxx",
		help_text="",
	)
```
Usage:
```python
person = Person.objects.create(name="Alice")
IDCard.objects.create(person=person, card_number="AB123456")

# Accessing the ID card from person (returns a single instance, not a manager):
print(person.id_card.card_number)
```

---

E.g. If you want to record a phone for a user, we know the phone is unique by user so it's never share with more than one user, but can be transferred:
```python
class Phone(models.Model):
	country_code = ...
	region_code = ...
	number = ...
	full_number = ...

	def save(self, *args, **kwargs): 
		...
		self.full_number = int(f'{self.country_code}{self.region_code}{self.number}')  # Build the full number by concatenating the fields!
		...

class User(models.Model):
	first_name = ...
	phone = models.OneToOneField(
		'Phone',  # Set it between quotes to avoid circular import issues in the future. 
		on_delete=models.CASCADE,
		null=True,
	)
```

---
## When One-to-One relationship is automatically created:
In addition, when you are working with inheritance of classes, Django automatically creates the one-to-one relationship between both tables on the database:
```python
class Vehicle(models.Model):
	# ...
	
class Bike(Vehicle):
	# ...
```

---
## Similar field classes:
xxxxxxxxxxxxxxxx
## How to avoid Circular Import issue:
[/python/web-development/django/6-errors-and-validations/importing-no-circular](/python/web-development/django/6-errors-and-validations/importing-no-circular.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

