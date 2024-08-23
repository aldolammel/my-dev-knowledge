# IN VIEWS.PY FILE:

from django.views.generic import ListView, DetailView
from .models import Recipe


# Creating a class that inherits pre-defined features from one of the generic classes brought
# by Django. In this case, 'ListView' class:
class RecipesListView(ListView):  # This 'View' in classname is a convention.
    # Attaching the table (defined in some models.py) will feed this view-class:
    model = Recipe
    # Defining with template must be used to show the data:
    template_name = 'recipes/list.html'
    # Defining the name you will call the data (variable) on the templates:
    context_object_name = 'recipes'  # idk how to call more than one type of data in this way!!!
    # Default context:
    # object_list   <-- call this in template to call automatically all data from the model!


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
    context_object_name = 'recipe'
    
    





# IN URLS.PY FILE:

from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    # http://127.0.0.1:8000/recipes
    path('', views.RecipesListView.as_view(), name='list_view'),
    # http://127.0.0.1:8000/recipes/12
    path('<int:id>', views.RecipeDetailView.as_view(), name='detail_view')
    # Crucial: this 'name' above is the 'pattern name' you'll use to build URL's in templates.
]
    



# IN THE LIST-TEMPLATE (list.html):

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



# IN THE DETAIL-TEMPLATE (detail.html):

<html>
    <body>
    
        {% for field in recipe %}
            <div class="css-class-example">{{ field }}</div>
        {% endfor %}
        
        <a href="{% url 'recipes:list_view' %}">Back to recipe list</a>
    
    </body>
</html>
