#### Python > Django > Models > Query sets
# Filtering

---
## Before:
- What is QuerySet: [/python/web-development/django/3-1-models-database/4-querysets/\_what-is-queryset](/python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset.md)

---
In these examples, consider each queryset is asking data to a model called `Recipe`:
### Showing the first entry on this model/table (Recipe)
```python
from . import models

r_first = models.Recipe.objects.first()
```
### Showing the entry with pk/id = 4
```python
from . import models

r_specific = models.Recipe.objects.get(id=4)
```
### Showing all objects in a specific table (Recipe)
```python
from . import models

r_all = models.Recipe.objects.all()
```
### Showing a specific number of entries
More about: [/python/python-knowledge/slicing](/python/python-knowledge/slicing.md)
```python
from . import models

r_three = models.Recipe.objects.all()[:3]  # Using the slicing technic.
```
### Showing all entries greater than a value
This 'id__' is the column (attribute) you want to search, and that `__gt` means *greater than* command. You can use `__gte` for *greater than or equal to* command.
```python
from . import models

greater_than = models.Recipe.objects.filter(id__gt=3)
```
### Collecting all posts from the same user and created in the same date or later
```python
from . import models

user_posts = models.Recipe.objects.filter(
    created_at__gte=instance.created_at,
    created_by=instance.created_by,
).exclude(pk=instance.pk)
```
### Filtering only entries from a specific category
This `i` before `exact` means the search must not be case-sensitive. `category__name__exact` is case-sensitive. 

Be aware:
- this `__name__` is exactly the attribute the filter will be applied. If you're looking for `author` it must be written as `__author__`.
- Not sure, but maybe the `category__` is editable too.

```python
from . import models

all_from_cat = models.Recipe.objects.filter(category__name__iexact='salad')
```
### Filtering only entries that contain a certain string in its name
This `i` before `contains` means the search must not be case-sensitive. `category__name__contains` is case-sensitive.

Be aware:
- This `__name__` is exactly the attribute the filter will be applied. If you're looking for `author` it must be written as `__author__`.
- Not sure, but maybe the `category__` is editable too.

```python
from . import models

search_in_cat = models.Recipe.objects.filter(category__name__icontains='soup')
```
### Filtering only entries that DON'T contain a certain string in its name
This `i` before `contains` means the search must not be case-sensitive. `name__contains` is case-sensitive.

Be aware:
- This `name__` is exactly the attribute the exclude will be applied. If you're looking for `author` it must be written as `author__contains`.

```python
from . import models

exclude_those = models.Recipe.objects.exclude(name__icontains='soup')
```
### Filtering even more
This `-date_added` is asking for descending order of `date_added`.
```python
from . import models

super_search = models.Recipe.objects.exclude(name__icontains='soup').order_by('-date_added')
```
### Condition, using the operator `OR`:
Creating a condition inside the `.filter()` using the operator `OR` but here just a `Q`:
```python
from django.db.models import Q
from . import models

# QuerySet of all event instances where platform is the same of my current object, including those events with no platform at all:
models.Event.objects.filter(Q(platform=self.instance.platform) | Q(platform__isnull=True))
```
### Condition, using the operator `AND`:
In Django, the operator `AND` is just a comma `,` making each argument part of the condition:
```python
from . import models

# QuerySet of all event instances that the platform is the same of my current object, and, at the same time, those event instances must belong to existing users:
models.Event.objects.filter(platform=self.instance.platform, created_by__isnull=False)
```
### Filtering a field to show only options that are using a common foreignkey instance:
```python
from django import forms
from . import models

# Sometimes plane_seat field is not available in the form (because could be readonly_field):
# Seat options should respect which plane's procedure is loaded on screen:
if "plane_seat" in self.fields:
	# Defining the object (procedure) that the plane_model attr. exists:
	procedure = self.instance.procedure if self.instance.procedure.id else None
	# Taking the procedure plane_model's ID:
	plane_model_id = procedure.plane_model_id if procedure else None
	# Finally, loading only those PlaneSeat instances that the plane_model are the same of the procedure plane_model already selected on the form:
	plane_seat = self.fields["plane_seat"]
	if isinstance(plane_seat, forms.ModelChoiceField):
		plane_seat.queryset = models.PlaneSeat.objects.filter(plane_model_id=plane_model_id)
```
---
Returning other formats:
### Return as object (default)
```python
as_obj = models.Recipe.objects.filter(id=7)
# Output: <QuerySet [<Recipe: African Chicken Curry>]>
```
### Return as dictionary
```python
as_dict = models.Recipe.objects.filter(id=7).values()
# Output: 
#     <QuerySet [
#         {
#             'id': 7, 
#             'name': 
#             'African Chicken Curry', 
#             'description': 'Are you ready!', 
#             'date_added': datetime.datetime(
#                 2024, 
#                 7, 
#                 3, 
#                 15, 
#                 29, 
#                 41, 
#                 39059, 
#                 tzinfo=datetime.timezone.utc
#             ), 
#             'category_id': 1
#         }
#     ]> 
```
### Return as tuple
```python
as_tuple = models.Recipe.objects.filter(id=7).values_list()
# Output: 
#     <QuerySet [
#         (
#             7, 
#             'African Chicken Curry', 
#             'Are you ready!', 
#             datetime.datetime(
#                 2024, 
#                 7, 
#                 3, 
#                 15, 
#                 29, 
#                 41, 
#                 39059, 
#                 tzinfo=datetime.timezone.utc
#             ), 
#             1
#         )
#     ]>
```
### Return as boolean
```python
as_bool = models.Recipe.objects.filter(id=7).exists()
# Output: True
```

---
## Examples:
How to make the CMS doens't show unpublished things with the published ones: [/python/web-development/django/4-cms-admin/method-formfield_for_foreignkey](/python/web-development/django/4-cms-admin/method-formfield_for_foreignkey.md)


