#### Python > Django > Model matters
# QuerySets: the built-in get_queryset() method

---
## Before:
1. What is it: [python/web-development/django/3-1-models-database/4-querysets/\_what-is-queryset](python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset.md)

---
## You can use *get_queryset()* in:

- Admin classes (*admin.py*);
- Class-Based Views (*views.py*);
- Custom Managers (*models.py*);
- Django REST Framework (*DRF*) ViewSets or APIViews;

E.g.
- Filtering:  [python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/QuerySet-filtering.py](python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/QuerySet-filtering.py)
- Aggregation: [python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/QuerySet-aggregation.py](python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/QuerySet-aggregation.py)
- Counting: [python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/QuerySet-counting.py](python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/QuerySet-counting.py)
- Other formats: [python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/QuerySet-other-formats.py](python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/QuerySet-other-formats.py)

---
## Avoid redundancies:

For example, if you're working in an Admin class, you could set the ordering through the Meta class and via *get_queryset* as well, but this approach is absolutely a bad practice:

BAD:
```
class Meta:
	ordering = ["order"]
	
# Doing exactly the same as in Meta ordering:
def get_queryset(self, request):
	"""Built-in method to customize the initial db records list retrieved and processed."""
	qs = super().get_queryset(request)
	return qs.order_by("order")
```
GOOD:
```
class Meta:
	ordering = ["order"]
```

---
## QuerySets in Forms.py:
[python/web-development/django/9-forms/form-queryset-filtering-dropdown.py](python/web-development/django/9-forms/form-queryset-filtering-dropdown.py)

