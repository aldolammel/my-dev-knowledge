#### Python > Django > CMS > Methods
# `get_actions()` admin model method

---

The `get_actions()` is a built-in admin method that returns actions available for a particular context, typically a list of actions that can be executed on selected objects.

So, it does:
- xxxxx

---
## Structure:
```python
xxxxxxxxxxxxxxxxxxxxxxxx


```

---
## Common example:
```python
class ProcedureAdmin(admin.ModelAdmin):
    # ...
    
    def get_actions(self, request):
	    '''Built-in admin method that returns actions available for a particular context.'''
        actions = super().get_actions(request)

        # Removes the bulk-delete action for users who are not superusers:
        if not request.user.is_superuser:
            actions.pop("delete_selected", None)

        return actions
```

---
## Same method but for Model Class:
When you see `get_actions()` in a Django `ModelAdmin` class, it refers to the Admin action system. Outside that context, its behavior depends entirely on its implementation.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx