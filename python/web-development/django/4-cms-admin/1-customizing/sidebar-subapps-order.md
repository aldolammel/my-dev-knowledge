#### Python > Django > CMS > Customization
# CMS sidebar: changing sub-apps ordering

---

==Tradeoff==
Only one custom `default_site` is allowed, so if you later adopt a theme or package that also wants to own the admin site (some ship their own `AdminConfig`/`AdminSite`), you’ll have to merge the two, or move the ordering into the theme’s own config.

---
## 1) In `/core/consts.py`:
```python
# CMS CUSTOMIZATION:
CMS_SIDEBAR_APPS_ORDER = ["subapp1", "subapp2", "subapp3", "subapp4"]  # more in /core/admin.py
```
---
## 2) In `/core/admin.py`:
If this file doesn't exist, create it:
```python
from django.contrib import admin
from . import consts

class OrderedAdminSite(admin.AdminSite):
	"""Customizing the CMS left-sidebar's apps ordering."""
	
	def get_app_list(self, request, app_label=None):
		app_list = super().get_app_list(request, app_label)
		order = {label: i for i, label in enumerate(consts.CMS_SIDEBAR_APPS_ORDER)}
		return sorted(app_list, key=lambda app: order.get(app["app_label"], len(order)))
```

---
## 3) In `/core/apps.py`:
If this file doesn't exist, create it:
```python
from django.contrib.admin.apps import AdminConfig

class OrderedAdminConfig(AdminConfig):
	"""Customizing the CMS sidebar's apps ordering."""
	default_site = "core.admin.OrderedAdminSite"
```

---
## 4) In `/core/settings.py`:
```python
INSTALLED_APPS = [
	# DJANGO DEFAULT SUB-APPS:
	"core.apps.OrderedAdminConfig", # replaced "django.contrib.admin" (sidebar ordering)
	# ...
]
```

---

