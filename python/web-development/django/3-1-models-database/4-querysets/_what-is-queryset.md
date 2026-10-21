#### Python > Django > Models
# QuerySets, what are they

---

In Django, a QuerySet (`qs` commonly used) is a collection of database queries that represents a set of objects from your database. It's one of the most powerful and fundamental concepts in Django's ORM (Object-Relational Mapper).

==Are you sure?==
Sometimes you can use the relationship directly between model classes to request a data, without to create a `qs`:  [/python/web-development/django/3-1-models-database/model-attr-field-foreignKey](/python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md)

---
## Key Characteristics:

**Lazy Evaluation:** 
QuerySets don't hit the db 'til you actually need the data.

E.g.
```python
# No database query executed here
users = models.User.objects.all()

# Database query executed here (when we iterate)
for user in users:
	print(user.username)
```

**For partial data:**

[/python/web-development/django/3-1-models-database/4-querysets/qs-partial-data](/python/web-development/django/3-1-models-database/4-querysets/qs-partial-data.md)

**Chainable:**
You can chain multiple methods together.

E.g. Chain multiple filters:
```python
active_adults = models.User.objects.filter(
	is_active=True
).filter(
	age__gte=18
).exclude(
	is_staff=True
)
```

**Immutable:**
Each chain operation returns a new QuerySet.

E.g.
```python
qs1 = models.User.objects.all()
qs2 = qs1.filter(is_active=True)  # New QuerySet
# qs1 remains unchanged
```

---
## Common QuerySet Operations: 
### Filtering
```python
# Basic filtering
active_users = models.User.objects.filter(is_active=True)

# Field lookups
users_over_30 = models.User.objects.filter(age__gt=30)
users_named_john = models.User.objects.filter(username__startswith='john')
```
More filtering examples: [/python/web-development/django/3-1-models-database/4-querysets/qs-filtering](/python/web-development/django/3-1-models-database/4-querysets/qs-filtering.md)
### Excluding
```python
# Exclude certain records
non_staff_users = models.User.objects.exclude(is_staff=True)
```
### Ordering
```python
# Order by specific fields
users_ordered = models.User.objects.all().order_by('last_name', 'first_name')
reverse_order = models.User.objects.all().order_by('-date_joined')  # Descending
```
### Slicing
```python
# Get first 10 users
first_10 = models.User.objects.all()[:10]

# Get users 11-20
next_10 = models.User.objects.all()[10:20]
```
### Aggregation
```python
from django.db.models import Count, Avg

# Count active users
active_count = models.User.objects.filter(is_active=True).count()

# Average age
avg_age = models.User.objects.aggregate(Avg('age'))

# Group by and count
users_by_city = models.User.objects.values('city').annotate(count=Count('id'))
```
More aggregation examples: [/python/web-development/django/3-1-models-database/4-querysets/qs-aggregation.py](/python/web-development/django/3-1-models-database/4-querysets/qs-aggregation.py)
### Boolean
```python
is_alive = models.User.objects.filter(id=7).exists()
```
More boolean examples: [/python/web-development/django/3-1-models-database/4-querysets/qs-exists](/python/web-development/django/3-1-models-database/4-querysets/qs-exists.md)

---
## Using QuerySets on Model or Form `clean()` method to validation:
[/python/web-development/django/3-1-models-database/4-querysets/qs-for-validations](/python/web-development/django/3-1-models-database/4-querysets/qs-for-validations.md)

---
## Using QuerySets with Foreigner Keys:
[/python/web-development/django/3-1-models-database/4-querysets/qs-with-foreigner-keys](/python/web-development/django/3-1-models-database/4-querysets/qs-with-foreigner-keys.md)

---
## Usign QuerySets with Many-to-Many:
[/python/web-development/django/3-1-models-database/4-querysets/qs-with-many-to-many](/python/web-development/django/3-1-models-database/4-querysets/qs-with-many-to-many.md)

---
## Loading Admin/CMS fields already filtered:
- Method `get_queryset()`: [/python/web-development/django/4-cms-admin/method-get_queryset.py](/python/web-development/django/4-cms-admin/method-get_queryset.py)
- [/python/web-development/django/4-cms-admin/1-customizing/detailview-filtering-any-data](/python/web-development/django/4-cms-admin/1-customizing/detailview-filtering-any-data.md)


