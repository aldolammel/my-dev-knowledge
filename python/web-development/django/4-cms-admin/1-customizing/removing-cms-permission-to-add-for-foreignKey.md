#### Python > Django > Admin (CMS)
# Customizing: Removing permissions to show ForeignKey field buttons

---
## Basic solution for Django <5.2.7

admin.py:
```
@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):
	...
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		"""Built-in method that allows to override the default formfield for a foreignkeys field."""
		if db_field.name == "blog":  # The foreignkey attr/field in the "Example" model class!
			...
			# Customizing permissions:
			kwargs["can_add_related"] = False
			kwargs["can_change_related"] = False
			kwargs["can_delete_related"] = False
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
```

---
## Basic solution for Django >=5.2.7

==Attention!==
If you are using *formfield_for_foreignkey()* method, in the admin model targeted, make sure that method is not customizing any query-set. If so, transfer that to the *get_form()* method as shown below!

admin.py:
```
@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):
	...
	
	def get_form(self, request, obj=None, change=False, **kwargs):
		"""Built-in method to customize the form that's displayed in the interface."""
		form = super().get_form(request, obj, change, **kwargs)
		...
		# Customizing the dropdown-menu foreignkey field:
		# ("blog" is the foreignkey attr/field in the "Example" model class)
		if "blog" in form.base_fields:
			# Removing default add/remove buttons, applying the simple ModelChoiceField:
			form.base_fields["blog"] = f.ModelChoiceField(
				queryset=models.PagexPage.objects.filter(is_blog=True),
				required=True,  # is it correct for your model?
				label="xxxx",
				help_text="xxxxxxxx.",
			)
		return form
```

---
## Special cases

The admin class is using a custom form with a custom dunder *\_\_init\_\_()*, so the other solutions won't work properly. Try this one directly in the class init:
```
# admin.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class PagexPageContentInline(admin.StackedInline):
	
	# Custom form:
	form = forms.PagexContentForm
	
	...

# forms.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class PagexContentForm(forms.ModelForm):
	...
	
	def __init__(self, *args, **kwargs):
		"""Dunder method called 'constructor' that runs automatically when a class instance is created."""
		super().__init__(*args, **kwargs)
		
		# Simplest option - Remove the add icon from the 'element' ForeignKey widget:
		if hasattr(self.fields["element"].widget, "can_add_related"):
			self.fields["element"].widget.can_add_related = False
			
		# Smarter option - Remove more than one icon:
		widget = self.fields["element_content"].widget
		for attr in ("can_delete_related", "can_add_related", "can_change_related"):
			if hasattr(widget, attr):
				setattr(widget, attr, False)
		...
```