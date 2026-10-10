    LOGOUT IN DJANGO:

---

==Crucial:==
It's mandatory to use the POST method to execute the logout through Django:

In `/accounts/templates/registration/logout.html`:
```html
<form action="{% url 'accounts:logout' %}" method="post">

	{% csrf_token %}

	<button type="submit">
		Log out
	</button>

</form>
```


---
