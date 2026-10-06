#### Python > Django > Authenticated Users
# Extending users

---

If your project needs to show **User Profile** on the application front-end, or even a simple user creation form also on the application front-end, you must use these roadmap.

---
## Before:

1. [ ] Make sure you DON'T need a simpler user management approach: [/python/web-development/django/3-1-models-database/3-users/0-users-setup](/python/web-development/django/3-1-models-database/3-users/0-users-setup.md)
2. [ ] Make sure you know how to import a user: [/python/web-development/django/3-1-models-database/3-users/importing-users](/python/web-development/django/3-1-models-database/3-users/importing-users.md)

---
## 1) Create a sub-app called `accounts`:
 [/python/web-development/django/2-creating-and-deleting-apps/creating](/python/web-development/django/2-creating-and-deleting-apps/creating.md)

---   
## 2) Create Custom User Model (Extending the original one):

Create the `/accounts/validators.py` file:

```python
from django.core.exceptions import ValidationError

def validate_user_agreement(instance):
	"""Server-side validation for ordinary users to accept the app's terms."""
	if not instance.is_superuser and not instance.accepted_terms:
		raise ValidationError(
			"To use our services, you must read and accept our terms.",
			code="required",
		)
```

The built-in class `User` is a child of `AbstractUser` class where all original fields are.  
        
Create your custom User class:

Highly recommended to set in here: `/accounts/models.py`

```python
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from . import validators

class CustomUserManager(UserManager):
	"""Built-in class to customize the user creation."""
	def create_user(self, username, email=None, password=None, **extra_fields):
		if not extra_fields.get("accepted_terms", False):
			raise ValueError("Users must accept the Privacy Policy.")
		return super().create_user(username, email, password, **extra_fields)

	def create_superuser(self, username, email=None, password=None, **extra_fields):
		extra_fields["accepted_terms"] = True
		return super().create_superuser(username, email, password, **extra_fields)

class User(AbstractUser):
	"""Overriding the original fields just to custom them (as translating, for example)."""
	first_name = models.CharField(
		max_length=150,
		blank=True,
	)
	last_name = models.CharField(
		max_length=150,
		blank=True,
	)
	email = models.EmailField(
		blank=True,
	)
	# Above, those original fields (from AbstractUser) that are not overridden, they'll be working normally!
	# Below, new fields to extending the User features:
	accepted_terms = models.BooleanField(
		default=False,
		# verbose_name=...,
		# help_text=...,
		# error_messages in validators.py
	)
	# created_at = 'date_joined' from AbstractUser
	
	# Model Managers:
	# Reserved space...
	
	objects = CustomUserManager()
	
	class Meta:
		db_table = "auth_user" # I like to keep the original name!
		ordering = ["username"]
		verbose_name = "User"
		verbose_name_plural = "Users"
	
	def __str__(self):
		return self.username
		
	def clean(self):
		"""Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
		super().clean() # preserves Django’s built-in model cleaning!
		validators.validate_user_agreement(self)

class UserProfile(models.Model):
	"""This provides a reusable one-to-one profile model. A profile wont be created automatically by this model. To create one during registration or when the front end first needs it, such as with UserProfile.objects.get_or_create(user=user)."""
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name="profile",
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"Profile for {self.user.username}"
```

---
## 3) In `settings.py`, say Django needs to look for users in the new extended class:

```python
# App Essential Settings:
# ...
AUTH_USER_MODEL = 'accounts.User'  # '<my_subapp>.<user_model_class>'
```

---
## 4) Run `makemigrations` and `migrate` commands!

---
## 5) In `/apps/accounts/forms.py`:

```python
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
	"""Customizing the Django User Registration form for front-end."""
	class Meta:
		# Model tied used to populate it:
		model = User
		# Ordering fields on the form:
		fields = (
			"username",
			"email",
			"password1",
			"password2",
			"accepted_terms",
		)

	# Extra fields:
	# Important: signals.py: should the extra fields be declared over there? Check it!
	# Reserved space...
```

Check this out too: [/python/web-development/django/10-login-and-logout/0-registering-by-frontend](/python/web-development/django/10-login-and-logout/0-registering-by-frontend.md)

---
## 6) In `/apps/accounts/admin.py`, customize the CMS User list-view and detail-view:

In `/apps/accounts/admin.py`:
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import User, UserProfile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
	"""Defining how the User Model class will exclusively be shown on the CMS."""
	# Specify the custom form for creating users:
	add_form = CustomUserCreationForm
	list_display = (
		"username",
		"email",
		"last_login",
		"is_staff",
		# List_display accept imported fields using prefix and imported method (prefix recommended):
		# Reserved space...
	)
	
	# All fields exclusively for the CMS Adding New object:
	add_fieldsets = (
		(
			None,
			{
				# "classes": ("wide",),
				"fields": (
					"username",
					"email",
					"password1",
					"password2",
					"accepted_terms",
				)
			},
		),
	)
	
	# All fields exclusively for the CMS Visualizing an object:
	fieldsets = (
		(
			None,
			{
				# "classes": ("wide",),
				"fields": (
					"username",
					"password",
					# "profile_link", # Adding the UserProfile link in the User Detail-view!
					"accepted_terms",
				)
			},
		),
		(
			"Personal info",
			{
				# "classes": ("wide",),
				"fields": (
					"email",
					# "language",
				)
			},
		),
		(
			"Permissions",
			{
				# "classes": ("wide",),
				"fields": (
					"is_active",
					"is_staff",
					"is_superuser",
					"groups",
					"user_permissions",
				)
			},
		),
		(
			"Audit",
			{
				# "classes": ("wide",),
				"fields": (
					"date_joined",
					"last_login",
					# "last_pwd_update",
					"updated_at",
					"updated_by",
				)
			},
		),
	)
	
	list_filter = (
		"is_active",
		"is_staff",
		"is_superuser",
		# List_filter only accepts imported fields using prefix:
		# Reserved space...
	)
	
	search_fields = (
		"username",
		"email",
		"date_joined",
		# Search_fields accept imported fields using prefix & imported method (prefix recommended):
		# Reserved space...
	)
	
	readonly_fields = (
		# 'username', # Dynamically included!
		# 'accepted_terms', # Dynamically included!
		"date_joined",
		"last_login",
		"updated_at",
		"updated_by",
		# Readonly_fields only accept imported method, never with prefix:
		# Reserved space...
	)
	
	# Use this in case error trying to include or editing the object:
	"""
	def get_fieldsets(self, request, obj=None):
	'''Brings all data from fieldsets of the admin class.'''
	if not obj: # Adding a new object
	return self.add_fieldsets
	return self.fieldsets # Editing an existing object
	"""
	
	def get_readonly_fields(self, request, obj=None):
		"""Built-in method to extend the 'readonly_fields' power."""
		if obj:
			# If the user exists (obj), make some fields field read-only on detail-view,
			# but still editable on the CMS Add User form:
			return self.readonly_fields + (
				"username",
				"accepted_terms",
			)
		return self.readonly_fields
		
	def save_model(self, request, obj, form, change):
		"""Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
		obj.updated_by = request.user
		super().save_model(request, obj, form, change)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "created_at", "updated_at")
	list_select_related = ("user",)
	
	def has_add_permission(self, request):
		"""This built-in method should return True if adding obj's allowed."""
		return False
	
	def get_actions(self, request):
		"""This built-in method can conditionally enable or disable CMS actions, returning a dictionary of actions allowed."""
		# Remove the delete action from the list-view:
		actions = super().get_actions(request)
		if "delete_selected" in actions:
			del actions["delete_selected"]
		return actions
	
	def has_delete_permission(self, request, obj=None):
		"""This built-in method should return True if deleting obj is permitted."""
		# Prevent deletion of profile from the CMS, except when User is deleted:
		if request.path.startswith("/admin/auth/user/"): # or '/admin/accounts/user/'
			return request.user.is_superuser # True if superuser!
		return False
```

---
## 7) Test it!

---
## 8) (If applicable) User profile page (front-end):
[/python/web-development/django/3-1-models-database/3-users/3-extending-users-with-profile](/python/web-development/django/3-1-models-database/3-users/3-extending-users-with-profile.md)

---

