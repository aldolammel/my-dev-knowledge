#### Python > Django > Models
# Changing the field order in the back-office (CMS)

---

To change the order of the entries are listed in the CMS listing, add the class Meta into the class you want to reorder:
```python
Class Blablabla(models.Model):
	first_name = ...
	second_name = ...

	class Meta:
		# A-Z order:
		ordering = ['first_name',]
		# Z-A order:
		#ordering = ['-first_name',]

	def __str__(self):
		return self.second_name
```

==Important==
The `views.py` will use the same order defined in the `models.py` class.

---

