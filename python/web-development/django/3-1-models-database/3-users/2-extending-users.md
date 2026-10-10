#### Python > Django > Authenticated Users
# Extending users

---

.
.
.
.
==THIS ROADMAP IS NOT DONE YET!== 
.
.
.
.
If your project needs to show *User Profile* on the app's front-end, or even a simple user creation form also on the app front-end, you must use these roadmap. Let's create another model/table in order to isolate extra data associate with each user. That's why here you'll create a `UserProfile` class.

---
## Before:

1. [ ] Make sure you DON'T need a simpler user management approach: [/python/web-development/django/3-1-models-database/3-users/0-users-setup](/python/web-development/django/3-1-models-database/3-users/0-users-setup.md)
2. [ ] Make sure you know how to import a user: [/python/web-development/django/3-1-models-database/3-users/importing-users](/python/web-development/django/3-1-models-database/3-users/importing-users.md)

---
## 1) Create a sub-app called `accounts`:
 [/python/web-development/django/2-creating-and-deleting-apps/creating](/python/web-development/django/2-creating-and-deleting-apps/creating.md)

---   
## X) In `/accounts/validators.py`:

At first, create it in `validators.py` file:
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

---   
## X) In `/accounts/models.py`:
The built-in class `User` is a child of `AbstractUser` class where all original fields are.  That said, let's extend the original class with the fields we need. Go to `models.py`:
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
		on_delete=models.CASCADE,  # Del the UserProfile if the User is deleted.
		related_name="profile",
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"Profile for {self.user.username}"
```

---
## X) In `/accounts/signals.py`:
Create a signal to automatically create a `UserProfile` instance once a `User` is created from the app front-end or CMS: [/python/web-development/django/7-middlewares-and-signals/signals/signals-user-extended](/python/web-development/django/7-middlewares-and-signals/signals/signals-user-extended.md)

---
## X) In `/core/settings.py`:
Let's say to Django to look for users in the new extended class:
```python
# App Essential Settings:
# ...
AUTH_USER_MODEL = 'accounts.User'  # '<my_subapp>.<user_model_class>'
```

```python
SESSION_COOKIE_AGE = 2419200  # a month
LOGIN_URL = 'accounts:login'  # It's built-in.
LOGIN_REDIRECT_URL = '<subapp_namespace>:<url_pattern_name>'
# E.g. 'in:home_view'
LOGOUT_REDIRECT_URL = '<subapp_namespace>:<url_pattern_name>'
# E.g. 'general:home_view'
```

---
## X) Run `makemigrations` and `migrate` commands!

---
## X) In `/apps/accounts/forms.py`:
[/python/web-development/django/10-login-and-logout/1-registering-custom-form](/python/web-development/django/10-login-and-logout/1-registering-custom-form.md)

---
## X) Create the Account template folders and its html files:

x.1) Create these folders and the html files: `/accounts/templates/user/`
- [register.html](/python/web-development/django/9-forms/user-register-form.md)
- [login.html](/python/web-development/django/9-forms/user-login.md)
- [logout.html](/python/web-development/django/10-login-and-logout/3-logout-in-django.md)
- all password html files to organized here soon: `/python/web-development/django/9-forms/registration/`


---
## X) In `/apps/accounts/admin.py`, customize the CMS User list-view and detail-view:

In `/apps/accounts/admin.py`:
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import forms, models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
	"""Defining how the User Model class will exclusively be shown on the CMS."""
	# Specify the custom form for creating users:
	add_form = forms.CustomUserCreationForm
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

@admin.register(models.UserProfile)
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
## X) In `/accounts/views.py`:

```python
from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
	# Escape if logged-in:
	if request.user.is_authenticated:
		# There the user will be filtered in Personal or Business:
		return redirect('in:home_view')
	# Otherwise:
	else:
		if request.method == 'POST':
			form = CustomUserCreationForm(request.POST)
			if form.is_valid():
				new_user = form.save()
				# Automatic log-in after registration:
				login(request, new_user)
				return redirect('in:home_view')
		else:
			form = CustomUserCreationForm()
		# Defining what send to the template:
		context = {
			'page_title': lng.S_G_REG_TTL,
			'form': form,
			'bt_have_account': lng.BT_REG_HAVE_ACCOUNT,
			'bt_submit': lng.BT_REG_SUBMIT,
			'bt_back': lng.BT_BACK,
		}
		# Load template:
		return render(request, 'registration/register.html', context)


class CustomPasswordChangeView(PasswordChangeView):
	template_name = 'accounts/pwd_change.html'

	def form_valid(self, form):
		messages.success(self.request, lng.TX_FDBK_PROFILE_SUCC_PWD_UPDATED)
		return redirect('accounts:profile_view', username=self.request.user.username)  # type: ignore

	def get_context_data(self, **kwargs):
		# Definitions:
		user = self.request.user
		profile_type = TX_PROFILE_1 if user.profile_type == '1' else TX_PROFILE_2  # type: ignore
		context = super().get_context_data(**kwargs)
		# Building context:
		context['page_title'] = f'{S_I_PROFILE_PWD_TTL}: {user.username} ({profile_type})'  # type: ignore
		context['header'] = lng.S_I_PROFILE_PWD_TTL
		context['bt_back'] = lng.BT_BACK
		context['bt_submit'] = lng.BT_PROFILE_PWD_SUBMIT
		return context
```

---
## X) In `/accounts/urls.py`:

```python
from django.urls import path, include
from . import views

# Namespace:
app_name = 'accounts'

urlpatterns = [
	# http://127.0.0.1:8000/accounts/...
	path('register/',
		views.register,
		name="register_view"),
	path('login/',
		views.CustomLoginView.as_view(),
		name="login"),
	path('password/',
		views.CustomPasswordChangeView.as_view(),
		name="password_change_view"),
	path('password_reset/',
		views.CustomPasswordResetView.as_view(),
		name="password_reset"),
	path('password_reset/done/',
		views.CustomPasswordResetDoneView.as_view(),
		name="password_reset_done"),
	path('reset/<uidb64>/<token>/',
		views.CustomPasswordResetConfirmView.as_view(),
		name="password_reset_confirm"),
	path('reset/done/',
		views.CustomPasswordResetCompleteView.as_view(),
		name="password_reset_complete"),
	path('logout/',
		views.custom_logout_view,
		name="logout"),
	path('<str:username>',
		views.profile_view,
		name="profile_view"),
]
```



---
## X) Test it:
[/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing](/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing.md)

---
## X) (If applicable) User profile page (front-end):
[python/web-development/django/3-1-models-database/3-users/3-extending-users-with-profile-DELETE](python/web-development/django/3-1-models-database/3-users/3-extending-users-with-profile-DELETE.md)

---

