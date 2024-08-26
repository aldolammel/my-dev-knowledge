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
    
    # But if you don't wanna define a 'context_object_name', use the default context:
    # object_list   <-- call this in template!
    
    # Customizing the list features:
    # def get_ordering(self):
    # ...
    
    # Filtering/Counting/aggregating the list:
    # def get_queryset(self):
        # /33-Web-development/general/django/3-2-backend-views/1-building-views-context/class-based/QuerySet-filtering.py
        # /33-Web-development/general/django/3-2-backend-views/1-building-views-context/class-based/QuerySet-counting.py
        # /33-Web-development/general/django/3-2-backend-views/1-building-views-context/class-based/QuerySet-aggregation.py
        # /33-Web-development/general/django/3-2-backend-views/1-building-views-context/class-based/QuerySet-other-formats.py
    

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
    # context_object_name = 'recipe'    # In DetailView it's not needed because Django automatically
                                        # defines the context name as lowercase based on models name.
                                        
    # But if you don't wanna use the model name as 'context_object_name', use the default context:
    # object   <-- call this in template!
    





# IN URLS.PY FILE: ---------------------------------------------------------------------------------

from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    # http://127.0.0.1:8000/recipes
    path('', views.RecipesListView.as_view(), name='list_view'),
    # http://127.0.0.1:8000/recipes/12
    path('<int:pk>', views.RecipeDetailView.as_view(), name='detail_view')
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
    
        {% for field in recipe %}
            <div class="css-class-example">{{ field }}</div>
        {% endfor %}
        
        <a href="{% url 'recipes:list_view' %}">Back to recipe list</a>
    
    </body>
</html>
