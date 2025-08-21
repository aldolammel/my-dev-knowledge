# IN VIEWS.PY FILE:

from django.views.generic import ListView
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
        # /Python/Web-development/django/3-2-backend-views/1-building-views-context/class-based/QuerySet-filtering.py
        # /Python/Web-development/django/3-2-backend-views/1-building-views-context/class-based/QuerySet-counting.py
        # /Python/Web-development/django/3-2-backend-views/1-building-views-context/class-based/QuerySet-aggregation.py
        # /Python/Web-development/django/3-2-backend-views/1-building-views-context/class-based/QuerySet-other-formats.py
    




# IN URLS.PY FILE: ---------------------------------------------------------------------------------

from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    # http://127.0.0.1:8000/recipes
    path('', views.RecipesListView.as_view(), name='list_view'),
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