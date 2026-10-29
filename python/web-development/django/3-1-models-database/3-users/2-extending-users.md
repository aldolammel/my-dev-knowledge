#### Python > Django > Authenticated Users
# Extending users

---

If your project needs to show *User Profile* on the app's front-end, or even a simple user creation form also on the app front-end, you must use these roadmap. Let's create another model/table in order to isolate extra data associate with each user. That's why here you'll create a `UserProfile` class.

---
## Before:

1. [ ] Make sure you DON'T need a simpler user management approach: [/python/web-development/django/3-1-models-database/3-users/0-users-setup](/python/web-development/django/3-1-models-database/3-users/0-users-setup.md)
2. [ ] Make sure you know how to import a user: [/python/web-development/django/3-1-models-database/3-users/importing-users](/python/web-development/django/3-1-models-database/3-users/importing-users.md)

---
## 1) Create a sub-app called `accounts`:
 [/python/web-development/django/2-creating-and-deleting-apps/creating](/python/web-development/django/2-creating-and-deleting-apps/creating.md)

---
## X) In `/apps/accounts/validators.py`:

At first, create it in `validators.py` file:
```python
from django.core.exceptions import ValidationError

def validate_user_agreement(is_superuser: bool = False, accepted_terms: bool = False):
	"""Server-side validation for ordinary users to accept the app's terms."""
	if not is_superuser and not accepted_terms:
		raise ValidationError(
			{"accepted_terms": "To use our services, you must read and accept our terms."}
		)
```

---   
## X) In `/apps/accounts/models.py`:
The built-in class `User` is a child of `AbstractUser` class where all original fields are.  That said, let's extend the original class with the fields we need. Go to `models.py`:
```python
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower
from . import validators


class User(AbstractUser):
	"""Overriding the original fields just to custom them (as translating, for example)."""
	
	email = models.EmailField(
		max_length=255,
		unique=True,
		blank=False,
		verbose_name="E-mail",
		help_text="",
	)
	# Except fields right above, those original fields from AbstractUser are not been overridden, so they're working as expected!
	
	# Below, new fields to extending the User features:
	profile_type = models.PositiveSmallIntegerField(
		# This attr can be ignored in CMS and front-end case you don't need, but keep its value 1!
		default=1,
		blank=False,
		# verbose_name="Profile Type",
		# help_text="",
	)
	# This attribute can be invisible once the reason behind the hood is to make this more flexible, depending the project:
	accepted_terms = models.BooleanField(
		default=False,
		verbose_name="Accepted Terms",
		help_text="",
		# error_messages in validators.py
	)
	# created_at = 'date_joined' from AbstractUser
	
	class Meta:
		db_table = "auth_user" # I like to keep the original name!
		ordering = ["username"]
		verbose_name = "User"
		verbose_name_plural = "Users"
		constraints = [
			models.UniqueConstraint(
				Lower("email"),
				name="user_unique_email_lowered",
			),
		]
	
	def __str__(self):
		return self.username
		
	def clean(self):
		"""Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
		super().clean()
		validators.validate_user_agreement(self.is_superuser, self.accepted_terms)


class UserProfile(models.Model):
	"""A reusable one-to-one profile model. A profile isn't auto-created by this model. To create an instance in registration: UserProfile.objects.get_or_create(user=user)."""
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,  # Del the UserProfile if the User is deleted.
		related_name="profile",
	)
	platform = models.ForeignKey(
		Platform,
		related_name="user_profile",
		on_delete=models.SET_NULL,
		null=True,
		blank=False,
		verbose_name="Favorite Platform",
		help_text="",
	)
	lang_writing = models.ForeignKey(
		Language,
		related_name="user_profile",
		on_delete=models.SET_NULL,
		null=True,
		blank=False,
		verbose_name="Favorite Language",
		help_text="",
	)
	bio = models.TextField(
		max_length=255,
		default="",
		blank=True,
		verbose_name="Bio",
		help_text="",
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"{self.user.username}'s profile"
```

---
## X) Create `/apps/accounts/signals.py`:
Create a signal to automatically create a `UserProfile` instance once a `User` is created from the app front-end or CMS. Users get created from several places (admin, front-end registration, `createsuperuser`, shell, tests). A `post_save()` signal on `User` is the one spot that guarantees “every user has a profile” without repeating logic everywhere.
```python
from django.dispatch import receiver
from django.db.models.signals import post_save
from . import models

# Creates and associates one of UserProfile types to the new User:
@receiver(post_save, sender=models.User)
def create_user_profile(sender, instance, created, raw, **kwargs):
	if created and not raw:  # 'raw' skips fixture loading!
		if instance.profile_type == 1:
			models.UserProfile.objects.get_or_create(
				user=instance,
				# defaults={"lang_writing": instance.lang_ui},  # If needed...
			)
		else:
			# Reserved space in case more profile types available.
			pass
```

---
## x) Edit `/apps/accounts/apps.py`:
Register the `signals` file in there:
```python
from django.apps import AppConfig

class AccountsConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'apps.accounts'

	def ready(self):
		from . import signals  # noqa: F401
```

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
LOGIN_REDIRECT_URL = 'accounts:profile'
LOGOUT_REDIRECT_URL = 'accounts:login'
```

---
## X) In `/core/urls.py`:
```python
# SUB-APPs, APIs:
path("accounts/", include("apps.accounts.urls")),
```

---
## X) Run `makemigrations` and `migrate` commands!

---
## X) In `/apps/accounts/forms.py`:
```python
from django import forms
from django.contrib.auth.forms import (
    AdminUserCreationForm as BaseAdminUserCreationForm,
    UserChangeForm as BaseUserChangeForm,
    UserCreationForm,
)
from . import models

class UniqueEmailMixin:
    """Case-insensitive unique email; safe for both create and edit forms."""

    def clean_email(self):
        email = self.cleaned_data["email"]
        duplicates = models.User.objects.filter(email__iexact=email)
        if self.instance.pk:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
        
class RegistrationForm(UniqueEmailMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
	    # Model tied used to populate it:
        model = models.User
        # Ordering fields on the form:
        fields = (
	        # "profile_type",
	        "username",
	        "email",
	        "accepted_terms",
	    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if models.User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError({"email": "A user with this email already exists."})
        return email
        
    # Extra fields:
    # Reserved space...

class ProfileForm(forms.ModelForm):
	"""Customizing the User Profile form."""
    
    class Meta:
	    # Model tied used to populate it:
        model = models.UserProfile
        # Ordering fields on the form:
        fields = (
	        "platform",
	        "lang_writing",
	        "bio",
	    )
	
	# Extra fields:
	# Important: don't forget sometimes you need to add your extra fields in signals.py!
	# Reserved space...


class AdminUserCreationForm(UniqueEmailMixin, BaseAdminUserCreationForm):
    class Meta(BaseAdminUserCreationForm.Meta):
	    # Model tied used to populate it:
        model = models.User
        # Ordering fields on the form:
        fields = ("username", "email", "accepted_terms")

class AdminUserChangeForm(UniqueEmailMixin, BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
	    # Model tied used to populate it:
        model = models.User
```

---
## X) Create the Account template folders and its html files:
Create these folders and the html files: `/apps/accounts/templates/user/`
- [register.html](/python/web-development/django/9-forms/user-register-form.md)
- [profile.html](/python/web-development/django/9-forms/user-profile-form.md)
- [login.html](/python/web-development/django/9-forms/user-login.md)
- [logout.html](/python/web-development/django/10-login-and-logout/3-logout-in-django.md)
- all password html files to organized here soon: `/python/web-development/django/9-forms/registration/`

And apparently this is important to be overridden the original one:
create in there: `password_reset_email.html`
```html
{% autoescape off %}
{{ protocol }}://{{ domain }}{% url 'accounts:password_reset_confirm' uidb64=uid token=token %}
{% endautoescape %}
```
Why: Reset email template - django’s default email template reverses `password_reset_confirm` without the namespace and would fail with `NoReverseMatch`. That’s why `email_template_name` is overridden (==I NEVER CONFIRMED THAT==)

---
## X) In `/apps/accounts/admin.py`:

In `/apps/accounts/admin.py`:
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
#from django.utils.translation import gettext_lazy as _

from . import forms, models


class UserProfileInline(admin.StackedInline):
	'''xxxxxxxxxxxxxxxxxxxxxxxx'''
    model = models.UserProfile
    fk_name = "user"  # required: UserProfile has two FKs to User (user and updated_by)
    can_delete = False  # the profile lives and dies with its user
    extra = 0
    max_num = 1
    fields = (
	    "platform",
		"lang_writing",
		"bio",
		"created_at",
		"updated_at",
		"updated_by",
	)
    readonly_fields = (
	    "created_at",
	    "updated_at",
	    "updated_by",
	)


@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):
	'''xxxxxxxxxxxxxxxxxxxxxxxx'''
    form = forms.AdminUserChangeForm
    add_form = forms.AdminUserCreationForm
    inlines = [UserProfileInline]

    list_display = (
        "username",
        "email",
        "lang_ui",
        # "profile_type",
        "accepted_terms",
        "is_staff",
        "is_active",
        "date_joined",
    )
    list_filter = (
	    *DjangoUserAdmin.list_filter,
	    "lang_ui",
	    "profile_type",
	    "accepted_terms",
	)
    list_select_related = ("lang_ui",)
    search_fields = (
	    "username",
	    "email",
	    "first_name",
	    "last_name",
	)
    readonly_fields = (
	    "profile_type",
	    "updated_at",
	    "updated_by",
	)

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "lang_ui",
                    "accepted_terms",
                    "usable_password",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    
    fieldsets = tuple(DjangoUserAdmin.fieldsets or ()) + (
        (
	        "Service", {
		        "fields": (
			        "profile_type",
			        "lang_ui",
			        "accepted_terms",
				)
			}
		),
        (
	        "Audit", {
				"fields": (
					"updated_at",
					"updated_by",
				)
			}
		),
    )

    def get_inline_instances(self, request, obj=None):
	    '''Built-in admin method that returns the inline model admin instances to be displayed on the model's admin page.'''
        # On the add page there is no user yet. The post_save signal creates the profile, so showing the inline here would try to create a second one (unique violation).
        if obj is None:
            return []
        return super().get_inline_instances(request, obj)

    def save_model(self, request, obj, form, change):
	    '''Built-in admin method that allows you to customize what happens when a model is saved through the Django CMS interface.'''
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
	    '''Built-in admin method that customizes the saving objs submitted via inline formset.'''
        instances = formset.save(commit=False)
        for instance in instances:
            instance.updated_by = request.user
            instance.save()
        formset.save_m2m()


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	'''xxxxxxxxxxxxxxxxxxxxxxxx'''
    list_display = (
	    "user",
	    # "profile_type",
	    "platform",
	    "lang_writing",
	    "created_at",
	    "updated_at",
	)
    list_filter = (
		# "profile_type",
		"platform",
		"lang_writing",
	)
    list_select_related = ("user", "platform", "lang_writing")
    search_fields = (
	    "user__username",
	    "user__email",
	    "bio",
	)
    fields = (
	    "user",
	    # "profile_type",
	    "platform",
	    "lang_writing",
	    "bio",
	    "created_at",
	    "updated_at",
	    "updated_by",
	)
    readonly_fields = (
	    "user",
	    "created_at",
	    "updated_at",
	    "updated_by",
	)
		
    def has_add_permission(self, request):
	    """This built-in method should return True if adding obj's allowed."""
        return False  # profiles are created by the signal, never by hand.

    def has_delete_permission(self, request, obj=None):
		"""This built-in method should return True if deleting obj is permitted."""
		# If no superuser or if in the userprofile list-view/detail-view, don't allow deletion:
		if not request.user.is_superuser or request.path.startswith(
			"/admin/accounts/userprofile/" # or '/admin/auth/userprofile/'
		):
			return False
		# Otherwise, if through other sections like deleting the user itself, it's okay:
		return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
	    """Built-in admin method that allows you to customize what happens when a model is saved through the Django CMS interface."""
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
```

---
## X) In `/apps/accounts/views.py`:
```python
from django.contrib.auth import login, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from . import forms
from . import models

class RegisterView(CreateView):
    form_class = forms.RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:profile")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("accounts:profile")
        return super().dispatch(request, *args, **kwargs)

    @transaction.atomic
    def form_valid(self, form):
        response = super().form_valid(form)  # saves the user; the post_save signal creates the profile
        login(self.request, self.object)
        return response

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

class LogoutView(auth_views.LogoutView):
    # POST only since Django 5.0, so the template needs a <form method="post">
    pass

class PasswordChangeView(SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("accounts:profile")
    success_message = "Your password was changed."

class PasswordResetView(auth_views.PasswordResetView):
    template_name = "accounts/password_reset.html"
    email_template_name = "accounts/password_reset_email.html"
    subject_template_name = "accounts/password_reset_subject.txt"
    success_url = reverse_lazy("accounts:password_reset_done")

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"

class OwnProfileMixin(LoginRequiredMixin):
    """Always resolves to the logged-in user's profile, never one picked via the URL."""

    model = models.UserProfile

    def get_object(self, queryset=None):
        return get_object_or_404(
	        # TODO Should you include profile_type?
            models.UserProfile.objects.select_related("user", "platform", "lang_writing", "bio"),
            user=self.request.user,
        )

class ProfileView(OwnProfileMixin, DetailView):
    template_name = "accounts/profile.html"
    context_object_name = "profile"

class ProfileUpdateView(OwnProfileMixin, SuccessMessageMixin, UpdateView):
    form_class = forms.ProfileForm
    template_name = "accounts/profile_form.html"
    success_url = reverse_lazy("accounts:profile")
    success_message = "Profile updated."

    def form_valid(self, form):
        form.instance.updated_by = self.request.user  # AuditMixin field, not editable in the form
        return super().form_valid(form)
```

---
## X) In `/apps/accounts/urls.py`:

```python
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("password-change/", views.PasswordChangeView.as_view(), name="password_change"),
    path("password-reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path(
        "password-reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/edit/", views.ProfileUpdateView.as_view(), name="profile_edit"),
]
```

---
## X) In `/apps/accounts/serializers.py`:
`clean()` isn’t called by `create_user()` or serializers. The `accepted_terms` rule works in the admin (ModelForm) but not in the API, so the registration serializer must enforce it explicitly:
```python
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError as DRFValidationError

from . import models, validators

class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ["username", "email", "password", "accepted_terms"]
		extra_kwargs = {"password": {"write_only": True}}
		
		def validate(self, attrs):
			attrs = super().validate(attrs)
			try:
				validators.validate_user_agreement(
					is_superuser=False,  # self-register never creates superusers!
					accepted_terms=attrs.get("accepted_terms", False),
				)
		
			except ValidationError as except_:
				# except_.message_dict is {"accepted_terms": ["..."]}, which is the shape DRF expects
				raise DRFValidationError(except_.message_dict)
			return attrs
		
		def create(self, validated_data):
			return models.User.objects.create_user(**validated_data)
```

---
## X) Test it:
[/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing](/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing.md)

---

