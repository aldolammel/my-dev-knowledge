#### Python > Django > Models
# Importing a model from another sub-app

---

You are in `/apps/planes/models.py` and wanna call a model front other sub-app:
```python
apps.<subapp_name>.models import <ModelYouWannaImport>
# E.g. apps.platforms.model import Platform
```

---
