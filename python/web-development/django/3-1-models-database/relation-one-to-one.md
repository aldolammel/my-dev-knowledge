#### Python > Django > Models > Attribute types
# OneToOneField

---

In Django, a One-to-One relationship is a type of database relationship where each record in one model is linked to exactly one record in another model, and vice versa. This is represented in Django using the OneToOneField. This relationship is typically used when  you want to extend the functionality of an existing model by adding additional fields in a separate model, but with a one-to-one correspondence between the two models.

E.g. If you want to record a phone for a user, we know the phone is unique by user so it's never share with more than one user, but can be transferred:
```
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
## How to avoid Circular Import issue:
[/python/web-development/django/6-errors-and-validations/importing-no-circular](/python/web-development/django/6-errors-and-validations/importing-no-circular.md)
