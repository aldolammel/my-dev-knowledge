#### Python > Django > CMS > Methods
# `response_add()` admin model method

---
    
PROMPT: In the Python Django context, what does the XXXXXXXXX method do in short terms? Is it exclusive usage for Admin (CMS)?

xxxxx. So it does:

- xxxxx

---
## Structure:
```python
def response_add(self, request, obj, post_url_continue=None):
	'''Built-in CMS method that determines the HTTP response after a new model instance is successfully added.'''
	xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---
## Common example:
```python

# Out of the admin class scope:
WIZARD_SESSION_KEY = "step_common_wizard"

# As a method of a admin model class:
def response_add(self, request, obj, post_url_continue=None):
	'''Built-in CMS method that determines the HTTP response after a new model instance is successfully added.'''
	request.session.pop(WIZARD_SESSION_KEY, None)
	return super().response_add(request, obj, post_url_continue)
```

---
