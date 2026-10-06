#### Python > Django > Sub-apps
# Creating app (sub-app)

---

MODEL FIELD REFERENCE:
https://docs.djangoproject.com/en/5.1/ref/models/fields/

---

==Personal statement==
I (@aldolammel) call `app` as `sub-app` once I consider the Django itself the only "app" in here, where its modules/features, that I am developing for this project, are sub-apps.

---
## Before:

1. Make sure the project already has its `apps` package folder: [apps-package-creation](/python/web-development/django/2-creating-and-deleting-apps/apps-package-creation.md)
2. Make sure you are using the terminal in the project root.

---
## 1) Create the sub-app folder:

The convention for Django sub-app name is based in this logic:
- A sub-app is a collection of things, so it should be always plural (e.g. procedures, accounts, exams, etc).

```bash
cd apps
mkdir -p <subapp_name>
# E.g. mkdir -p accounts
```

---
## 2) Ask Django to create the basic files for the new sub-app:

2.1) Return to the project root folder.

2.2) Run the `startapp` command:
```bash
# Using UV:
uv run manage.py startapp <subapp_name> <destination_path>
# E.g. uv run manage.py startapp account apps/accounts

# Or using PIP:
python manage.py startapp <subapp_name> <destination_path>
# E.g. python manage.py startapp account apps/accounts
```

---
## 3) In the `/apps/sub-app/apps.py` file:

Add the `apps` package folder in the name, otherwise Django won't find this sub-app:
```python
class AccountConfig(AppConfig):
    default_auto_field = ...
    name = 'apps.<subapp_name>'  # E.g. 'apps.accounts'
```

---
## 4) In the `/apps/sub-app/views.py` file:

Through the `new-sub-app/views.py` just created, add a function for the index page to that sub-app:
```python
from django.http import HttpResponse
def index(request):
	return HttpResponse("It is just a test!") # Test it later: http://127.0.0.1:8000/<subapp_name>
```

---
## 5) Create the `/apps/sub-app/urls.py` file:

Create the `new-sub-app/urls.py` file, and add the `urlpatterns` list in each sub-app path/endpoint:
```python
from django.urls import path
from . import views

# NAMESPACE
app_name = '<subapp_name>'  # E.g. 'accounts'

urlpatterns = [
	path('', views.index),
]
```

---
## 6) In `/core/urls.py` file, include the sub-app URL reference:

```python
from django.contrib import admin
from django.urls import path, include

# DJANGO BASIC:
urlpatterns = [
	# CMS:
	path('admin/', admin.site.urls),
	# SUB-APPs, APIs:
	path('<subapp_name>/', include('apps.<subapp_name>.urls')),
]
```

---
## 7) (Optional) Only for Django template as front-end solution:

If your front-end solution will be Django, create these folders and file into the new sub-app folder:
```
/<subapp_name>/templates/
/<subapp_name>/templates/<subapp_name>/           <- It's a convention to repeat the sub-app name.
/<subapp_name>/templates/<subapp_name>/temp.html  <- only for GitHub to create the folder.
```

---
## 8) In core folder, go to `settings.py` file and add the sub-app name in the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
	# DJANGO DEFAULT SUB-APPS:
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# DJANGO ADDITIONAL SUB-APPS:
	# Reserved space...
	# APP ORIGINAL SUB-APPS:
	'apps.<project_subapp_name>',  # E.g. 'apps.accounts'
]
```

---
## 9) (If applicable) In case this new sub-app has included content in `models.py`:

**Basic to know:**
- `models.py` is the file that represents through classes each table and its columns to be created for a specific sub-app. Most part of tweaks here will result a `makemigrations` command necessity followed by `migrate` one.
	- `makemigrations` = it's responsible for planning the new features on the db based on the changes you have made to your models.
	- `migrate` = it's responsible for applying and/or unapplying migrations already planned by `makemigrations` command.
.

- [ ] **9.1) Ask to Django convert the objects in models to db instructions:**

Convert for all new sub-apps:
```bash
# Using UV:
uv run manage.py makemigrations

# Or using default command:
python manage.py makemigrations
```

Or for a specific sub-app only:
```bash
# Using UV:
uv run manage.py makemigrations apps.<subapp_name>

# Or using default command:
python manage.py makemigrations apps.<subapp_name>
```

- [ ] **9.2) Next, ask Django to execute the instructions:**

```bash
# Using UV:
uv run manage.py migrate

# Or using default command:
python manage.py migrate
```

---
## 10) Test it:

10.1) Run the app: [\_running-app](/python/web-development/django/_running-app.md)

10.2) And test the new sub-app: `http://127.0.0.1:8000/<subapp_name>`

---
