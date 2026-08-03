#### Python > Django > CMS:
# Creating the super admin user

---
## Before:
1. After to install the desired database: [/python/web-development/django/3-1-models-database/0-installing-and-adminUser/\_define-the-database](/python/web-development/django/3-1-models-database/0-installing-and-adminUser/_define-the-database.md)

---
## 1) Let's perform the database basic tasks:
It creates the database with basic tables:
```
python manage.py migrate
```
Or:
```
uv run manage.py migrate
```

---
## 2) Creating the admin user:
```
python manage.py createsuperuser
```
Or:
```
uv run manage.py createsuperuser
```

---       
# 3) Now, try to login, making sure the application is running:
[http://localhost:8000/admin/](http://localhost:8000/admin/)

---
