FRONT-END: USER LOGIN FORM

---

In `/apps/accounts/templates/registration/login.html`:
```html
<!-- LOGIN FORM - START -->
<form method="post">
	{% csrf_token %}

	{% for field in form.fields %}

		{{ field.label }}
		{{ field }}

	{% endfor %}

	<button type="submit">Login</button>
	<a href="{% url 'accounts:password_reset' %}">I forgot my password</a>
	<a href="{% url 'accounts:register_view' %}">Create a new account</a>
</form>
<!-- LOGIN FORM - END -->

```

TIP:
If you want to print the user (username or first_name or last_name) on the template, you DON'T need bring some in your views.py CONTEXT. Just call `user.username` on the template:
```html
{{ user.username }}
```
