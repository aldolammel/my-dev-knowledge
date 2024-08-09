'''

VIEWS WITH CLASSES:

    >> xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    >> xxxxxxxxxxxxxxxxxxxxxxxxx
    
'''


# 1) IN SUB-APP VIEWS.PY
from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView, DetailView

# Creating a class that inherits pre-defined features from one of the generic classes brought
# by Django. In this case, 'ListView' class:
class RecipesList(ListView):
    # Attaching the table (defined in some models.py) will feed this view-class:
    model = Recipe
    # Defining with template must be used to show the data:
    template_name = 'recipes/index.html'
    
    # Defining the name you will call the data (variable) on the templates:
    # Important custom context: idk how to call more than one type of data in this way:
    # context_object_name = 'recipes'

    # Default context:
    # object_list   <-- call this in template to call automatically all data from the model!


class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipes/recipe.html'
    context_object_name = 'recipe'




# 2) IN SUB-APP URLS.PY
from django.urls import path
from . import views

app_name = 'subapp_namespace'
urlpatterns = [
    # http://127.0.0.1:8000/recipes or http://127.0.0.1:8000/recipes/index.html
    path('', views.RecipesList.as_view(), name='list_view'),
    # http://127.0.0.1:8000/recipes/1
    path('<int:id>', views.RecipeDetail.as_view(), name='detail_view')
    # Crucial: this 'name' above is the 'pattern name' you'll use to build URL's in templates.
]
    



# 3) IN SOME TEMPLATE TO LIST RECIPES
<html>
    <body>
    
        {% if object_list %}    # <---- magic variable from class-based views!
        
            {% for i in object_list %}
            
                <p><a href="{% url 'subapp_namespace:detail_view' i.id %}">{{ i }}</a></p>
                
            {% endfor %}
            
        {% endif %}
        
    </body>
</html>