VIEW WHERE YOU HAVE MANY-TO-MANY FIELDS:

Without this `.save_m2m()`, your form in front-end will NOT save the [many-to-many](/python/web-development/django/3-1-models-database/model-attr-field-many-to-many.md) fields if they are, for example, a select-multiple field.
```python
if request.method == "POST":
	# ...
	if form.is_valid():
		# ...
		instance.save(user=user)  # Pass the user to the Form (and then to the model)!
		form.save_m2m()  # Crucial: saving many-to-many relationships!
		# ...
```
