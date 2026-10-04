
#### Python > Components & Libraries
# Psycopg

---

Psycopg is a Python library that acts as an adapter (connector) between Python apps and PostgreSQL databases. It's the most popular and mature PostgreSQL adapter for Python, allowing Python code to communicate with PostgreSQL databases.

---
## 1) Installation:

**Before:**
1. Assuming you're in the project environment.

**1.1) Install it:**

https://www.psycopg.org
        
Using UV:
```bash
uv add psycopg[binary]         # It will automatically update your pyproject.toml file!
```

Or using PIP:
```bash
python3 -m pip install psycopg
```
You should manually update the `pyproject.toml` file or the `requirements.txt`!

---
## 2) Integration:

In `/core/settings.py` file:
```python
INSTALLED_APPS = [
	# DJANGO DEFAULT SUB-APPS:
	# ...
	# DJANGO ADDITIONAL SUB-APPS:
	"django.contrib.postgres",  # Expands the postgres options.
	# ...
	# APP ORIGINAL SUB-APPS:
	# ...
]
```

---
