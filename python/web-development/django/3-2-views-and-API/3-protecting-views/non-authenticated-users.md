PROTECTING VIEW: NON-AUTHENTICATED USERS

Check these examples:

[/python/web-development/django/3-2-views-and-API/3-protecting-views/authenticated-users](/python/web-development/django/3-2-views-and-API/3-protecting-views/authenticated-users.md)


Checking whether the visitor is NOT logged-in/authenticated:

E.g. (Django recommends!)
```
if not request.user.is_authenticated:
	pass
```


E.g.
```
if request.user.is_anonymous:
	pass
```



>> NEED A UNAUTHORIZED PAGE (401)? CHECK THIS OUT:

Folder: /python/web-development/django/12-error-pages/401/
