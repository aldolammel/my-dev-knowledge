# IN VIEWS.PY FILE:

from django.views.generic.base import TemplateView
from .models import Recipe


# Creating another class that also inherits pre-defined features brought by Django.
# In this case, 'TemplateView' class:
class RecipeListView(TemplateView):  # This 'View' in classname is a convention.
    # Defining with template must be used to show the data:
    template_name = 'recipes/list.html'
    
    # When using 'TemplateView' this built-in function is avaliable to work with context concept:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding to context:
        context['recipes'] = Recipe.objects.all()
        return context
    
    
class RecipeDetailView(TemplateView):
    template_name = 'recipes/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_id = kwargs['id']
        # Adding to context:
        context['recipe'] = Recipe.objects.get(id=recipe_id)
        return context



# IN URLS.PY FILE: ---------------------------------------------------------------------------------

from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    # http://127.0.0.1:8000/recipes/
    path('', views.RecipeListView.as_view(), name='list-view'),
    # http://127.0.0.1:8000/recipes/12
    path('<int:id>', views.RecipeDetailView.as_view(), name='detail-view'),
    # Crucial: this 'name' argument above is the 'pattern name' you'll use to build URL's in templates.
]



    
# IN THE LIST-TEMPLATE (list.html): ----------------------------------------------------------------

<html>
    <body>
    
        # checking if there's some recipe in the View Context of this URL:
        {% if recipes %}
        
            {% for recipe in recipes %}
            
                <p><a href="{% url 'recipes:detail_view' recipe.id %}">{{ recipe }}</a></p>
                
            {% endfor %}
            
        {% else %}
        
            <p>There is no any recipe recorded yet!</p>
        
        {% endif %}
        
    </body>
</html>



# IN THE DETAIL-TEMPLATE (detail.html): ------------------------------------------------------------

<html>
    <body>
    
        <h1>{{ recipe.title }}</h1>
        <small>{{ recipe.author }}</small>
        
        {{ recipe.description }}
        
        <a href="{% url 'recipes:list_view' %}">Back to recipe list</a>
    
    </body>
</html>
