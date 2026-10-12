#### Dev concepts > Object classes
# Mixin

---

Use a Model Mixin for an independent, reusable capability that multiple models can incorporate. It's a class that provides a specific set of methods and properties to be inherited or composed by other classes, without being a standalone base class itself. It is designed to add reusable functionality through inheritance or composition, promoting code reuse without forcing a rigid hierarchical structure.

### Mixin class is not a Base class:

| Aspect         | Mixin class                               | **[Base Model class](/dev-concepts/class-type-base.md)**                                                    |
| -------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Purpose        | Provides reusable fields or functionality | Establishes a common foundation for a model hierarchy                                                       |
| Inheritance    | Often shared across unrelated models      | Usually inherited by models within the same hierarchy                                                       |
| Abstract?      | Typically yes                             | Can be [abstract](/dev-concepts/class-type-abstract.md) or [concrete](/dev-concepts/class-type-concrete.md) |
| Database table | Usually none                              | Depends on whether it is abstract                                                                           |
| Example        | `AuditMixin`, `TimestampMixin`            | `VehicleBase`, `PersonBase`                                                                                 |

---
## Python example:
[python/web-development/django/3-1-models-database/model-type-mixin](python/web-development/django/3-1-models-database/model-type-mixin.md)

---
## Database Context:

In modern ORMs (like Django's ORM or SQLAlchemy), mixins are used to share common database fields, behaviors, or constraints across multiple models.

E.g. using Python:
```python
from datetime import datetime
from sqlalchemy import Column, DateTime


class TimestampMixin:
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(
      DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
  )


# Usage in a model
class User(Base, TimestampMixin):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  name = Column(String)
```