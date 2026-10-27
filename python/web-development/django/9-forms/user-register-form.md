#### Python > Django > Forms > Front-end
# User register form

---

In a template (e.g. `register.html`) customize this:
```html
<!-- REGISTER FORM - START -->
<form method="post">
	{% csrf_token %}

	{% for field in form.fields %}

		{{ field.label }}
		{{ field }}

	{% endfor %}

	<a href="{% url 'accounts:login' %}">
		I already have an account
	</a>
	<button type="submit" name="register_account">
		Create account
	</button>

</form>
<!-- REGISTER FORM - END -->
```

TIP:
If you want to print the user (`username` or `first_name` or `last_name`) on the template, you DON'T need bring some in your `views.py` CONTEXT. Just call `user.username` on the template:
```html
{{ user.username }}
```


---
## MORE ABOUT USER:
- If you want to build the entire registering flow, including Django configs, look this: [/python/web-development/django/3-1-models-database/3-users/2-extending-users](/python/web-development/django/3-1-models-database/3-users/2-extending-users.md)
- For customize the User Register Form:  same link as above.
- If you're looking for how to import users in your models.py classes: [/python/web-development/django/3-1-models-database/3-users/importing-users](/python/web-development/django/3-1-models-database/3-users/importing-users.md)


