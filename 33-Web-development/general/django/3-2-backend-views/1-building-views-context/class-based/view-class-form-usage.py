# IN VIEWS.PY FILE:

from django.views.generic.edit import FormView
from .forms import ProfileForm


# Creating a class that inherits pre-defined features from one of the generic classes brought
# by Django. In this case, 'FormView' class:
class ProfileView(FormView):  # This 'View' in classname is a convention.
    # Attaching the formulary (defined in some forms.py) will feed this view-class:
    form_class = ProfileForm

    # Defining with template must be used to show the form:
    template_name = 'accounts/profile.html'

    # Defining address that Django must send the user right after a flawless form submition:
    success_url = '/'

    # Define that Django must do with that data just sent by the form:
    def form_valid(self, form):
        # Save the data in the database:
        form.save()
        return super().form_valid(form)

    # Django automatically replace this get() method below, so don't use it:
    # def get(self, request)
    # pass

    # Django automatically handle the form submitions here, so don't use it:
    # def post(self, request)
    # pass
