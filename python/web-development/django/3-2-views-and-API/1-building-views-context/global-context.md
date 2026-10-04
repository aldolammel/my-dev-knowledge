#### Python > Django > Views
# Global context:

---

If you are NOT using an external front-end solution and need a CONTEXT callable on the entire app, you want a 'Global Context'! Even for external front-end solution, something you would want to pass via Django context to the front-end. So probably you wanna use it:

==PAGEX==
If you are using Pagex in your Django, you don't need this roadmap once the Pagex already manage it for you.

---
## 1) Create a `consts.py` file in your core-folder (Recommended):
[/python/web-development/django/z-project-examples/proj-aldolammel-style/core/consts.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/consts.py)

---
## 2) In a core-folder, create a file called `context_processors.py`:
[/python/web-development/django/z-project-examples/proj-aldolammel-style/core/context_processors.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/context_processors.py)

---
## 3) (Skip it if you'll use an existent `settings.py` model later)

In `settings.py` file, find 'TEMPLATES' section and add:
```python
TEMPLATES = [
	{
		# ...
		'OPTIONS': {
			'context_processors': [
				# DJANGO DEFAULT GLOBAL CONTEXTS:
				# ...
				# DJANGO ADDITIONAL GLOBAL CONTEXTS:
				# ...
				# THIRD-PARTY GLOBAL CONTEXTS:
				# ...
				# APP CUSTOM GLOBAL CONTEXTS:
				"core.context_processors.app_info",
			],
		},
	},
]
```


---

## 4) Now, call your global context wherever you want on templates:

E.g. 
```html
<a href="mailto:{{ BRAND_EMAIL }}?subject={{ BRAND_NAME }}: Contact from website" target="_blank">Contact us</a>
```

---
