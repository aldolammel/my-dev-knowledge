# IN VIEWS.PY FILE:

from django.views.generic import DetailView
from .models import Recipe


# Creating a class that inherits pre-defined features from one of the generic classes brought
# by Django. In this case, 'DetailView' class:   
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
    # http://127.0.0.1:8000/recipes/12
    path('<int:pk>', views.RecipeDetailView.as_view(), name='detail_view')
    # Crucial: this 'name' argument above is the 'pattern name' you'll use to build URL's in templates.
]
    



# IN THE DETAIL-TEMPLATE (detail.html): ------------------------------------------------------------

<html>
    <body>
    
        {% for field in recipe %}
            <div class="css-class-example">{{ field }}</div>
        {% endfor %}
        
        <a href="{% url 'recipes:list_view' %}">Back to recipe list</a>
    
    </body>
</html>
