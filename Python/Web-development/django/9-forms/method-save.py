

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

    # Django automatically provides this save() method:
    # def save(self, commit=True):
    #     """Built-in Form method persists form data to the db."""
    #     instance = super().save(commit=False)
    #     if commit:
    #         instance.save()
    #     return instance

# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

    # Custom save method
    def save(self, commit=True):
        """Built-in Form method persists form data to the db."""
        # Get the instance but don't save to DB yet
        user = super().save(commit=False)
        
        # Custom logic
        user.name = user.name.title()  # Capitalize name
        user.set_password('default123')  # Set default password
        
        if commit:
            user.save()  # Now save to database
        
        return user

    
# Save method in a View - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Calls either default or custom save()
            # user is now saved to database