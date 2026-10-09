#### Python > Django > Views
# Global context:

---

If you are NOT using an external front-end solution and need a CONTEXT callable on the entire app, you want a 'Global Context'! Even for external front-end solution, something you would want to pass via Django context to the front-end. So probably you wanna use it:

==PAGEX==
If you are using Pagex in your Django, you don't need this roadmap once the Pagex already manage it for you.

---
## 1) Create `/core/consts.py` file:
[/python/web-development/django/z-project-examples/proj-aldolammel-style/core/consts.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/consts.py)

---
## 2) Create `/core/context_processors.py` file:
[/python/web-development/django/z-project-examples/proj-aldolammel-style/core/context_processors.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/context_processors.py)

---
## 3) In `/core/settings.py`:
```python
TEMPLATES = [
	{
		# ...
		'OPTIONS': {
			'context_processors': [
				# DJANGO DEFAULT GLOBAL CONTEXTS:
				# ...
				# DJANGO ADDITIONAL GLOBAL CONTEXTS:
				"core.context_processors.data_to_cms_template_only",  # <-------- add this!
				# THIRD-PARTY GLOBAL CONTEXTS:
				# Reserved space...
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

Remember: in case you are using Pagex, use the `/core/context_processors.py` limited to the CMS interface once the [Pagex](/python/web-development/django/useful-sub-apps/pagex/_install-and-integration.md) has a wide and easier support to app front-end information.

---
