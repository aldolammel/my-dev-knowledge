# IN VIEWS.PY FILE:

from django.views.generic.edit import CreateView
from .models import Recipe  # hypothetical class just for example purposes.
from .forms import RecipeForm  # hypothetical class just for example purposes.


# Creating a view-class that inherits its features from an existent model-class in models.py file,
# and, maybe, an existent form-class in forms.py file too.
# Besides being able to create a view associated with a model-class and a form-class simultaneously,
# this 'CreateView' view-class also may allow us to avoid the need to create a form-class and
# the forms.py file creation:


# SIMPLEST WAY (AVOIDING FORMS.PY): if you'd need only form fields config from forms.py, look this:
class RecipeAView(CreateView):  # This 'View' in classname is a convention.
    # Linking a model-class to the view:
    model = Recipe

    fields = '__all__'  # Avoid to use '__all__', so prefer to use ['field1', 'field2', ...]!
    template_name = 'recipes/detail.html'
    success_url = '/recipe-list'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# FLEXIBLE WAY (USING MODELS.PY AND FORMS.PY TOGETHER): if you'd need more then form fields configs:
class RecipeBView(CreateView):
    model = Recipe
    # Also, linking a form-class to the view. It gives you more than just 'form fields' configs:
    form_class = RecipeForm

    # fields = '__all__'  # when defining some 'form_class' here, 'fields' ISN'T supported anymore!
    template_name = 'recipes/detail.html'
    success_url = '/recipe-list'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
