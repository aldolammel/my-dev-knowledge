#### Python > Django > Models > Attribute types
# ForeignKey (OneToMany)

---

## 1) Meanwhile an author has one or more books, a book usually has only one author. Here we got a perfect example of one-to-many relationship.

Building up both needed classes for our example in models.py file, remembering in this case we use 'ForeignKey' model:
```
class Author(models.Model):
	name = ...

class Book(models.Model):
	title = ...
	author = models.ForeignKey(
		'Author',  # Set it between quotes to avoid circular import issues in the future.
		related_name='books',
		on_delete=models.CASCADE,    # .PROTECT  or  .SET_NULL   or   .CASCADE
		null=True,
	)
```


MORE ABOUT ON_DELETE:

[/python/web-development/django/3-1-models-database/2-model-arguments](/python/web-development/django/3-1-models-database/2-model-arguments.md)

## 2) Still in the same sub-app, in admin.py file:
```
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
```


## 3) Run the CMS and check the if everything is fine.

---
## How to avoid Circular Import issue:
[/python/web-development/django/6-errors-and-validations/importing-no-circular](/python/web-development/django/6-errors-and-validations/importing-no-circular.md)
