#### Python > Django > Models
# Deleting all `migrations` files

---

Important: assuming you got all sub-apps in your application `/apps/` folder:

```bash
# delete all migration files except __init__.py, in every app
find apps -path "*/migrations/*.py" ! -name "__init__.py" -delete
```