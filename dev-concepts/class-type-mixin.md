#### Dev concepts > Object classes
# Mixin

---

It's a class that provides a specific set of methods and properties to be inherited or composed by other classes, without being a standalone base class itself. It is designed to add reusable functionality through inheritance or composition, promoting code reuse without forcing a rigid hierarchical structure.

---
## Programming Context (Python & General OOP):

In languages supporting multiple inheritance (like Python), mixins allow a class to inherit features from multiple orthogonal sources.

E.g. using Python: 

[/python/web-development/django/4-cms-admin/model-type-mixin.py](/python/web-development/django/4-cms-admin/model-type-mixin.py)

---
## Database Context:

In modern ORMs (like Django's ORM or SQLAlchemy), mixins are used to share common database fields, behaviors, or constraints across multiple models.

E.g. using Python:
```
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