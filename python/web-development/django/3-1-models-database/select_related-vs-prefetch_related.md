#### Python > Django > Models > Methods
# `select_related()` VS `prefetch_related()`

---
## Keep in mind:
- `select_related()`: relation returns ONE object (forward FK, OneToOne, reverse OneToOne). Single query using a SQL JOIN.
- `prefetch_related()`: relation returns MANY objects (M2M, reverse FK, GenericRelation). One extra query per relationship, joined in Python memory. Prevents N+1.
- `prefetch_related()` also works on single-valued relations (useful to avoid wide JOINs or to apply a custom queryset via `Prefetch`).
- `GenericForeignKey` works with `prefetch_related()` only, never `select_related()`.

---
## Chaining across levels
```python
Procedure.objects.prefetch_related("procsection_set__stepcommon_set")
```

---
## Prefetch object (filter / order / nested `select_related` / custom attr)
```python
from django.db.models import Prefetch

Procedure.objects.prefetch_related(
    Prefetch(
        "procsection_set",
        queryset=ProcSection.objects.order_by("name"),
        to_attr="ordered_sections",
    )
)
```

---
## Combining both (the common real-world pattern)
```python
Procedure.objects
    .select_related("aircraft_model", "proc_type", "platform", "language", "created_by")
    .prefetch_related("procsection_set__stepcommon_set", "procsection_set__stepglobal_set")
```
(Adjust lookup names to your `related_name` values.)

---
## Gotcha
Calling `.filter()`, `.order_by()`, `.exclude()` etc. on an already-prefetched relation (e.g. `procedure.procsection_set.filter(...)`) IGNORES the cache and hits the DB again. Filter/order inside a `Prefetch(queryset=...)` instead.

---
## Debugging
Use `django-debug-toolbar` or `assertNumQueries` to confirm the query count.

---
