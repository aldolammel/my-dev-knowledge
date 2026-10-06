#### Python > Django > Authenticated Users
# Importing users

---
## Before:

Both methods access Django's user model, but there's an important architectural difference:

```python
# Not recommended:
from django.contrib.auth.models import User

# Recommended:
from django.contrib.auth import get_user_model
User = get_user_model()
```

- When you `import User`, you're importing the Django default model that has no potential project customizations within.
- When you `import get_user_model`, you dynamically retrieve whatever user model is configured in the core settings, much more future-proof.

---

You want to connect all authenticated users from your app in another table:

## 1) import the django User table:
In app models.py, import the django User table, and build up the new table with the attribute that connect with your users:
            
```python
from django.conf import settings as stgs

Class Team(models.Model):
	name = models.CharField(max_length=40)
	users = models.ManyToMany(stgs.AUTH_USER_MODEL)
```

More about ManyToMany relationship: [relation-many-to-many](/python/web-development/django/3-1-models-database/relation-many-to-many.md)

---
## 2) import the Team class created recently
In app admin.py, import the Team class created recently, and register this in the CMS:

```python
from .models import Team
admin.site.register(Team)
```

---   
## 3) Run `makemigrations`:
Execute the `makemigrations` in the specific app and check the CMS to see the result.

---
## Basic about users:
[/python/web-development/django/3-1-models-database/3-users/0-users-setup](/python/web-development/django/3-1-models-database/3-users/0-users-setup.md)
## If you're looking for about register and login forms:
- [user-profile-form](/python/web-development/django/9-forms/user-profile-form.md)
- [user-register-form](/python/web-development/django/9-forms/user-register-form.md)
- [user-change-password](/python/web-development/django/9-forms/user-change-password.md)
- [user-login](/python/web-development/django/9-forms/user-login.md)
- [user-logout](/python/web-development/django/9-forms/user-logout.md)





        