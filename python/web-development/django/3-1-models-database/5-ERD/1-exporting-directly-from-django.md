#### Python > Django > Models > ERD
# Exporting directly from Django

---
## Before:

**1) Make sure you got GraphViz installed (not-in-virtual-env):**
Windows:
```
xxxxx
```
Linux:
```
sudo apt install graphviz
```
Mac:
```
xxxxx
```

**2) Assuming you already activated the project venv!**

---
## 1) Install django-extensions:

[python/web-development/django/component-libraries/django-extensions/0-django-extensions](python/web-development/django/component-libraries/django-extensions/0-django-extensions.md)

---
## 2) Now, install the PyDotPlus for graph generation:
Using UV:
```
uv add --optional dev pydotplus
```
Or use pip:
```
python3 -m pip install pydotplus
```
And then add manually this to the dev sub-group in pyproject.toml file!

---
## 3) Generate ERD:

For all your DB tables:
```
python manage.py graph_models -a -o myapp_models.png
```
For specific apps:
```
python manage.py graph_models <app_name_1> <app_name_2> -o myapp_models.png
```
E.g.
```
python manage.py graph_models auth -o myapp_models.png
```
myapp_models.png example:
![python/web-development/django/3-1-models-database/5-ERD/myapp_models.png](python/web-development/django/3-1-models-database/5-ERD/myapp_models.png)