#### Python > Django > Model matters
# What are QuerySets

---

In Django, a QuerySet (`qs` commonly used) is a collection of database queries that represents a set of objects from your database. It's one of the most powerful and fundamental concepts in Django's ORM (Object-Relational Mapper).

==Are you sure?==
Sometimes you can use the relationship directly between model classes to request a data, without to create a `qs`:  [/python/web-development/django/3-1-models-database/Inheriting-attributes](/python/web-development/django/3-1-models-database/Inheriting-attributes.md)

---
## Key Characteristics:

**Lazy Evaluation:** 
QuerySets don't hit the db 'til you actually need the data.

E.g.
```python
# No database query executed here
users = User.objects.all()

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
active_adults = User.objects.filter(
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
qs1 = User.objects.all()
qs2 = qs1.filter(is_active=True)  # New QuerySet
# qs1 remains unchanged
```

---
## Common QuerySet Operations: 
   
### Filtering
```python
# Basic filtering
active_users = User.objects.filter(is_active=True)

# Field lookups
users_over_30 = User.objects.filter(age__gt=30)
users_named_john = User.objects.filter(username__startswith='john')
```

**More filtering examples:** [/python/web-development/django/3-1-models-database/4-querysets/qs-filtering.py](/python/web-development/django/3-1-models-database/4-querysets/qs-filtering.py)
### Excluding
```python
# Exclude certain records
non_staff_users = User.objects.exclude(is_staff=True)
```
### Ordering
```python
# Order by specific fields
users_ordered = User.objects.all().order_by('last_name', 'first_name')
reverse_order = User.objects.all().order_by('-date_joined')  # Descending
```
### Slicing
```python
# Get first 10 users
first_10 = User.objects.all()[:10]

# Get users 11-20
next_10 = User.objects.all()[10:20]
```
### Aggregation
```python
from django.db.models import Count, Avg

# Count active users
active_count = User.objects.filter(is_active=True).count()

# Average age
avg_age = User.objects.aggregate(Avg('age'))

# Group by and count
users_by_city = User.objects.values('city').annotate(count=Count('id'))
```

**More aggregation examples:** [/python/web-development/django/3-1-models-database/4-querysets/qs-aggregation.py](/python/web-development/django/3-1-models-database/4-querysets/qs-aggregation.py)

---
## Using QuerySets with Foreigner Keys:
[/python/web-development/django/3-1-models-database/4-querysets/qs-with-foreigner-keys](/python/web-development/django/3-1-models-database/4-querysets/qs-with-foreigner-keys.md)

## Usign QuerySets with Many-to-Many:
[/python/web-development/django/3-1-models-database/4-querysets/qs-with-many-to-many](/python/web-development/django/3-1-models-database/4-querysets/qs-with-many-to-many.md)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

**QuerySets on ADMIN/CMS:**
- Method *get_queryset()*: [/python/web-development/django/4-cms-admin/method-get_queryset.py](/python/web-development/django/4-cms-admin/method-get_queryset.py)
- [/python/web-development/django/4-cms-admin/1-customizing/detailview-filtering-any-data.py](/python/web-development/django/4-cms-admin/1-customizing/detailview-filtering-any-data.py)

