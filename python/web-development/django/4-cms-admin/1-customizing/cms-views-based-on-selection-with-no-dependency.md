#### Python > Django > Admin (CMS) > Form soluctions
# Adding an instance with multi-step form (with no dependency usage)

---

**What kind of form do you need (summary):** 
- [/python/web-development/django/4-cms-admin/\_what-kind-of-cms-ux-do-you-need](/python/web-development/django/4-cms-admin/_what-kind-of-cms-ux-do-you-need.md)

For new objects, through the adding detail-view, select options that will define the next form screen, and then Django loads the specific form (still in detail-view) based on the previous selection. For existing entries through the list-view, each listed entry, if clicked, loads fields as expected, preserving those `readonly_fields` if they exist.

**Example:**

Screen 1/2:
![](/python/web-development/django/4-cms-admin/z_imgs/adding-form-using-steps_step-1.png)

Screen 2/2:
![](/python/web-development/django/4-cms-admin/z_imgs/adding-form-using-steps_step-2.png)

---
## 1) In `/apps/subapp/consts.py`:
```python
# OTHERS
TPL_STEP_COMMON_READONLY_FIELDS = (
	# About forms.py StepCommonStartForm fields:
	# Once the screen 1 is completed, these fields below cannot be changed!
	"platform",
	"language",
	"procedure",
	"step_type",
	"step_hierarchy",
)
STR_STEP_SESSION_KEY = "step_common_session"  # It must be unique for each multi-step form feature.
STR_STEP_PARAM = "screen" # <adding-step-form-url>?screen=2
```
---
## 2) In `/apps/subapp/forms.py`:
If you don't have a `forms.py` file in the same sub-app of the `models.py`, create it and, then, use this template below:
```python
from typing import Any
from django import forms
from . import consts, models


def build_multi_step_instance(data: dict[str, Any]):
	"""Unsaved StepCommon prefilled with the screen 1 data (field name -> pk/value)."""
	common_opts = models.StepCommon._meta
	return models.StepCommon(
		**{common_opts.get_field(name).attname: value for name, value in data.items()}  # type: ignore[union-attr]
	)

class StepCommonStartForm(forms.ModelForm):
    """Screen 1. Never saved; only validated and stored in the session."""

    class Meta:
        model = models.StepCommon
        fields = consts.TPL_STEP_COMMON_READONLY_FIELDS
```

---
## 3) In `/apps/subapp/admin.py`:

```python
from django.contrib import admin, messages
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _

from . import consts, forms, models


@admin.register(models.StepCommon)
class StepCommonAdmin(SaveUserMixin, admin.ModelAdmin):
    """xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""
    
    # ... If applicable, keep your list_display, list_filter, filter_horizontal, search_fields, readonly_fields.
    
    # All fields exclusively for the CMS' EXISTING object detail-view:
    fieldsets = (
        (
	        "Context",
	        {"fields": consts.TPL_STEP_COMMON_READONLY_FIELDS},
        ),
        (
	        "Step details",
	        {
	            "fields": (
	                "proc_type_group",
					"sub_step_of",
					"comp_loc_area",
					"component",
					"what_to_do",
					"plane_seat",
					"applicabilities",
					"is_shareable",
					"is_active",
	            ),
	        },
        ),
    )


    def get_readonly_fields(self, request, obj=None):
		"""Built-in CMS method that allows you to dynamically specify which fields are read-only ('readonly_fields') based on the request or object."""
		readonly = [
			*super().get_readonly_fields(request, obj),
			*consts.TPL_STEP_COMMON_READONLY_FIELDS,
		]

		# Defining which fields define the next form screen behavior:
		if obj is not None:
			step_type = obj.step_type
			step_hierarchy = obj.step_hierarchy
		else:
			step_type = request.session.get(consts.STR_STEP_SESSION_KEY, {}).get("step_type")
			step_hierarchy = request.session.get(consts.STR_STEP_SESSION_KEY, {}).get("step_hierarchy")
		
		# Conditions based on what was selected in the screen 1:
		if (
			step_type == consts.INT_STEP_TYPE_ACTION and
			step_hierarchy == consts.INT_STEP_COMMON_HIER_NORMAL
		):
			readonly.append("comp_loc_area")
		if (
			step_type == consts.INT_STEP_TYPE_ACTION and
			step_hierarchy == consts.INT_STEP_COMMON_HIER_GROUP
		):
			readonly.extend(["sub_step_of", "what_to_do", "plane_seat", "applicabilities"])
		if (
			step_type == consts.INT_INT_TYPE_INFO and
			step_hierarchy == consts.INT_STEP_COMMON_HIER_NORMAL
		):
			readonly.extend(["comp_loc_area", "component", "plane_seat"])
		if (
			step_type == consts.INT_STEP_TYPE_INFO and
			step_hierarchy == consts.INT_STEP_COMMON_HIER_GROUP
		):
			readonly.extend(["sub_step_of", "comp_loc_area", "component", "plane_seat"])
		return tuple(readonly)
		
		
    def get_urls(self):
	    """Built-in CMS method that allows you to add or customize URL patterns."""
        custom = [
            path(
                "add/stepcommon/",
                self.admin_site.admin_view(self.adding_step_screen_1_view),
                name=f"{self.opts.app_label}_{self.opts.model_name}_adding_step_screen_1",
            ),
        ]
        # Custom URLs must come first, or "<path:object_id>/" swallows them.
        return custom + super().get_urls()


    # Screen 1:
    def adding_step_screen_1_view(self, request: HttpRequest) -> HttpResponse:
	    '''Custom xxxxxxxxx'''
        if not self.has_add_permission(request):
            raise PermissionDenied

        if request.method == "POST":
            form = forms.StepCommonStartForm(request.POST)
            if form.is_valid():
                # Model instances -> pks, so the session stays JSON-serializable.
                request.session[consts.STR_STEP_SESSION_KEY] = {
                    name: getattr(value, "pk", value)
                    for name, value in form.cleaned_data.items()
                }
                add_url = reverse(
                    f"admin:{self.opts.app_label}_{self.opts.model_name}_add"
                )
                return HttpResponseRedirect(f"{add_url}?{consts.STR_STEP_PARAM}=2")
        else:
            # Prefills when coming back from screen 2.
            form = forms.StepCommonStartForm(
                initial=request.session.get(consts.STR_STEP_SESSION_KEY)
            )

        context = {
            **self.admin_site.each_context(request),
            "opts": self.opts,
            "title": "Adding Step Common (1 of 2)",
            "form": form,
        }
        return TemplateResponse(
            request, "admin/procedures/stepcommon/wizard_start.html", context
        )


    # Screen 2 (Native Django adding detail-view):
    def add_view(self, request, form_url="", extra_context=None):
		'''Built-in Django admin method that handles the view logic and form processing for adding a new model instance in the admin interface.'''
        has_data = consts.STR_STEP_SESSION_KEY in request.session
        if request.GET.get(consts.STR_STEP_PARAM) != "2" or not has_data:
            if request.GET.get(consts.STR_STEP_PARAM) == "2":
                messages.info(request, "Choose the Step Common basics first.")
            return HttpResponseRedirect(
				reverse(f"admin:{self.opts.app_label}_{self.opts.model_name}_adding_step_screen_1")
			)
        return super().add_view(request, form_url, extra_context)


    def get_form(self, request, obj=None, change=False, **kwargs):
	    '''Built-in CMS method to customize the form that's displayed in the interface.'''
        form_class = super().get_form(request, obj, change=change, **kwargs)
        if obj is not None:
            return form_class

        locked = request.session.get(consts.STR_STEP_SESSION_KEY, {})

        class MultiStepForm(form_class):  # type: ignore[valid-type, misc]
            def __init__(self, *args, **kw):
                # Admin passes no instance on add (GET or POST).
                if kw.get("instance") is None:
	                kw["instance"] = forms.build_multi_step_instance(locked)
				super().__init__(*args, **kw)

        return MultiStepForm


    def response_add(self, request, obj, post_url_continue=None):
	    '''Built-in CMS method that determines the HTTP response after a new model instance is successfully added.'''
        request.session.pop(consts.STR_STEP_SESSION_KEY, None)
        return super().response_add(request, obj, post_url_continue)
```

---
## 4) Template matters:
4.1) Create the first step of your adding form, e.g., `/apps/procedures/templates/admin/procedures/stepcommon/wizard_start.html:`
```html
{% extends "admin/base_site.html" %}
{% load i18n admin_urls %}

{% block breadcrumbs %}
<div class="breadcrumbs">
  <a href="{% url 'admin:index' %}">Home</a>
  &rsaquo; <a href="{% url 'admin:app_list' app_label=opts.app_label %}">{{ opts.app_config.verbose_name }}</a>
  &rsaquo; <a href="{% url opts|admin_urlname:'changelist' %}">{{ opts.verbose_name_plural|capfirst }}</a>
  &rsaquo; {{ title }}
</div>
{% endblock %}

{% block content %}
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" class="default" value="Next">
</form>
{% endblock %}
```

4.2) In the same folder, create the `change_form.html` as well, which Django picks up automatically for this model. It adds a “back" link on screen 2:
```html
{% extends "admin/change_form.html" %}
{% load i18n %}

{% block form_top %}
  {% if not original %}
    <p>
      Screen: 2 of 2 —
      <a href="{% url 'admin:procedures_stepcommon_wizard_start' %}">Back to previous screen</a>
    </p>
  {% endif %}
{% endblock %}
```

---
## CSS customization in Django Admin:
[/python/web-development/django/4-cms-admin/1-customizing/css-customization-in-admin](/python/web-development/django/4-cms-admin/1-customizing/css-customization-in-admin.md)

