

"""
    DJANGO FORMS > METHODS: SAVE()

    In short, the save() method in Django forms.py persists form data to the database. So it does:

    - Takes cleaned/form-validated data from the form.
    - Creates or updates a model instance.
    - Commits the changes to the database.

    >> Where does save() method is available:
        As save() method is a core part of Django's form handling, it's available in all Django forms (ModelForms and regular forms with custom save logic). The Admin interface uses forms internally, but you use save() in your own views too.

    >> Keep in mind:
    - Use save_model() for admin-specific logic that needs request context.
    - Use model's save() for business logic that should apply everywhere.
    - Use form's save() for form-specific data processing.

    >> The save() for Django Forms is NOT the same of save() for Django Models:
        /Python/Web-development/django/3-1-models-database/method-save.py

    >> The save() for Django Admin Models is the save_model() method:
        /Python/Web-development/django/4-cms-admin/method-save_model.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# forms.py
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

    
    def save(self, commit=True):
        """Built-in Form method persists form data to the db."""
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance  # In forms, the save() always MUST return the instance/obj!


# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Django automatically provides this save() method, but you can customized it:

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

    # Custom save method
    def save(self, commit=True):
        """Built-in Form method persists form data to the db."""

        # Get the instance but don't save to DB yet:
        user = super().save(commit=False)
        
        # Custom logic:
        user.name = user.name.title()  # Capitalize name
        user.set_password('default123')  # Set default password
        
        if commit:
            user.save()  # Now save to database. This 'user.save()' calls automatically the full_clean() on models.
        
        return user  # In forms, the save() always MUST return the instance/obj!

    
# Save method in a View - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# METHOD IN A VIEW <------
def blabla_view(request):  #  <---- Exactly, for VIEWS we use only '.save()' through other methods!
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():  # To run a form clean(), its MANDATORY to call the VIEW '.is_valid()' method that will run the FORM clean() only, never running the clean() in models. There is NO full_clean() for forms!
            user = form.save()  # Using '.save()' now it calls MODEL clean() and save() where the full_clean() must be automatically called, validating the model attributes/constraints, and finally saving the user in the db!