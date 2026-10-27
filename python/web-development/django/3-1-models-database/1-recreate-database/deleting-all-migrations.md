#### Python > Django > Models
# Deleting all `migrations` files

---

==I never test it!==

Important: assuming you got all subapps in your application `/apps/` folder:

```bash
# delete all migration files except __init__.py, in every app
find apps -path "*/migrations/*.py" ! -name "__init__.py" -delete
```