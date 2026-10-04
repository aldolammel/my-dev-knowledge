#### Python > Django > Templates
# Bootstrap: Installed version and recommended HTML (using template tags)

---

Case you prefer a CDN version: [/web-development/frontend/css/css-libraries-frameworks/bootstrap/no-install-version-cdn](/web-development/frontend/css/css-libraries-frameworks/bootstrap/no-install-version-cdn.md)

---
## 1) Installing the Bootstrap in virtual environment:

Linux/Ubuntu: 
```bash
# Using UV:
uv add django-bootstrap5
# Or using PIP:
python3 -m pip install django-bootstrap5
```
Win:
```
$ xxxx
```
Mac:
```
xxxx
```

---     
## 2) Installing the bootstrap in the Django Project:
      
In config-folder, open the `settings.py` and include it in installed application list:
```python
# INSTALLED_APPS
	# DJANGO DEFAULT SUB-APPS:
	# ...
	# DJANGO ADDITIONAL SUB-APPS:
	'django_bootstrap5',
	# ...
```

---
## 3) Load the bootstrap in your base html file:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Bootstrap demo</title>

    {# Load the tag library #} {% load django_bootstrap5 %} {% bootstrap_css %}
  </head>
  <body>
    {# Display django.contrib.messages as Bootstrap alerts #} {% bootstrap_messages %}

    <h1>Hello, world!</h1>
    <p>text text text text text</p>

    {% bootstrap_form form %} {% bootstrap_button button_type="submit" content="My button text" %}
    {% bootstrap_javascript %}
  </body>
</html>
```


---
