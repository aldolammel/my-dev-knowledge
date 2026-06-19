#### Python > Django > Admin (CMS)
# CSS customization in Django Admin

---
## 1) Create your CSS file:

Create the CSS file here:
```
/<your-django-app>/static/<your-subapp>/css/admin_<scope-of-this>.css
```
E.g.
```
/senna_website/static/pagex/css/admin_content_inline.css
```

---
## 2) Add the Media class in your admin class:

Add this class inside your admin class that will use that CSS customization:
```
class Media:
	css = {"all": ("<your-subapp>/css/admin_<scope-of-this>.css",)}
```
E.g.
```
class PagexPageContentInline(admin.StackedInline):
	model = ...
	form = ...
	...
	
	class Media:
		css = {"all": ("pagex/css/admin_content_inline.css",)}
```
"admin_content_inline.css" content: [python/web-development/django/z-project-examples/proj-aldolammel-style/static/subapp_name/css/admin_zebra_striping_inline.css](python/web-development/django/z-project-examples/proj-aldolammel-style/static/subapp_name/css/admin_zebra_striping_inline.css)

---
## 3) (If applicable) Run collectstatic on prod:

If your app is in development phase (`DEBUG = True` in *settings.py*), just ignore it, but if it's already on production, you should run:
```
python manage.py collectstatic
# or with UV:
uv run manage.py collectstatic
```
The *collectstatic* is only needed for production, where static files must be gathered into a single directory for the web server (nginx, etc.) to serve.


---
