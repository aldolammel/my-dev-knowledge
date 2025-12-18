"""
    DJANGO > MODEL/CLASS: MIXIN

    In Django, a model mixin is an abstract base class that provides reusable fields and methods to other models via multiple inheritance, promoting the "Don't Repeat Yourself" (DRY) principle. Mixins are typically used to inject common functionalities without forcing a strict "is-a" relationship (unlike typical inheritance). 
"""

# admin.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class SaveUserMixin:
    """Automatically passes the current user to the model's save method."""

    def save_model(self, request, obj, form, change):
        """Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)


@admin.register(models.ExampleModelOne)
class ExampleModelOneAdmin(SaveUserMixin):
    ...
    # the save_model() method is here by inheritance (from SaveUserMixin class)


@admin.register(models.ExampleModelTwo)
class ExampleModelTwoAdmin(SaveUserMixin):
    ...
    # the save_model() method is here by inheritance (from SaveUserMixin class)




# models.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Same logic!




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Of course, if you wanna customize the save_model() method in a Admin class, you cannot use that same SaveUserMixin inheritance, making a better approach to declare the save_model into the Admin class instead of to use a mixin class.