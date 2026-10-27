#### Python > Django > CMS > Methods
# `save_formset()` admin model method

---
    
The `save_formset()` is a built-in admin method that allows you to customize how Django saves objects submitted through an inline formset.

So it does:
- Purpose: Customizes how Django Admin saves objects submitted through an inline formset.
- When called: When saving a parent model's admin form and its inline formsets.
- Default behavior: Calls `formset.save()`, saving new, modified, and deleted inline objects.
- Common use: Customize inline object saving, such as assigning additional fields or handling related data.

---
## Structure:
```python
def save_formset(self, request, form, formset, change):
    '''Built-in admin method that customizes the saving objs submitted via inline formset.'''

    # Some logic:
	for inline_form in formset.forms:
		# Considering only existing obj that was changed:
		if inline_form.instance.pk and inline_form.has_changed():
			inline_form.instance.updated_by = request.user

	# Save instances and many-to-many relationships:
	formset.save()
```
Use `formset.save()` to finish the saving only when you don't need `commit=False` to customize individual instances before saving them. In that case using `commit=False`, use `formset.save_m2m()`.

---
## Common example:
```python
@admin.register(Something)
class SomethingInline(...):
	# ...

class SomethingAdmin(admin.ModelAdmin):
    inlines = [SomethingInline]
    # ...

    def save_formset(self, request, form, formset, change):
	    '''Built-in admin method that customizes the saving objs submitted via inline formset.'''
        
        # Creates instances without saving them yet:
        instances = formset.save(commit=False)
        
        # Delete objects marked for deletion:
        for obj in formset.deleted_objects:
            obj.delete()
		
		# Loop to save new and modified objects:
        for instance in instances:
            # For new instance, do it:
            if not instance.pk:
                instance.created_by = request.user
            # For all of them, just save:
            instance.save()
		
		# Saves many-to-many relationships:
        formset.save_m2m()
```

---




