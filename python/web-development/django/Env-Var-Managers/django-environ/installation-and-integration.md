#### Python > Django > Environment variable managers
# Django-Environ install & integration

---

To seamlessly integrate environment-based configuration with the Django framework. It builds upon the ideas of `python-dotenv` but adds Django-specific features, type casting, and URL parsing that are indispensable for Django projects.

---
## Before:
1. Defining the back-end environment variables with `.env` file: [/environment-variables/env-for-local/in-backend/.env](/environment-variables/env-for-local/in-backend/.env)

---
## 1) Installation:

Include the manager as a mandatory project's dependency:

Using UV:
```
uv add django-environ
```

Or using PIP:
```
python3 -m pip install django-environ
```

---
## 2) Integration:

2.1) Calling those env vars in Django `settings.py` like this example: [/python/web-development/django/Env-Var-Managers/django-environ/examples/settings.py](/python/web-development/django/Env-Var-Managers/django-environ/examples/settings.py)

2.2) Make sure your `.env` vars are already configured with the real project db values (db name, user name, etc).

2.3) (If applicable) Make sure `.gitignore` file is ignoring the back-end `.env` file.

---
