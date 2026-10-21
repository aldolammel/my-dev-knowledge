#### Python > Django > Validations > Constraints
# Conditionals

---

Actually, conditions is the use of uniqueness well applied: [/python/web-development/django/6-errors-and-validations/validation-constraint-uniqueness](/python/web-development/django/6-errors-and-validations/validation-constraint-uniqueness.md)
E.g.
```python
from django.db.models import Q

models.UniqueConstraint(
	# ...
	condition=Q(is_active=True),
	# ...
)
```