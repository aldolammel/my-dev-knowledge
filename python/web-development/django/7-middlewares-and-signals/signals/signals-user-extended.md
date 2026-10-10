#### Python > Django > Signals
# Extending Django user data

---
## 1) Extending Django built-in user features:

Very basic to use: [/python/web-development/django/3-1-models-database/3-users/2-extending-users](/python/web-development/django/3-1-models-database/3-users/2-extending-users.md)

Way where signals are needed: [python/web-development/django/3-1-models-database/3-users/3-extending-users-with-profile-DELETE](python/web-development/django/3-1-models-database/3-users/3-extending-users-with-profile-DELETE.md)

---
## 2) Create a `signals.py` file into the `accounts` sub-app if not available yet, and:

```python
from django.dispatch import receiver
from django.db.models.signals import post_save
from . import models


# Creates and associates one of UserProfile types to the new User:
@receiver(post_save, sender=models.User)
def user_profile_auto_creation(sender, instance, created, **kwargs):
	if created:
		if instance.profile_type == '1':
			models.UserProfileOne.objects.create(user=instance)
		else:
			models.UserProfileTwo.objects.create(user=instance)
```

---
## 3) Register the `signals.py` file in the `app.py` file:

```python
from django.apps import AppConfig

class AccountsConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'accounts'

	def ready(self):
		from . import signals
```

---
