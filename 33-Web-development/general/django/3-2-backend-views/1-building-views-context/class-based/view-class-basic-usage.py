# IN VIEWS.PY FILE:

from django.shortcuts import render
from django.views.generic import View
from .models import Recipe  # hypothetical class just for example purposes.


class RecipeView(View):
    def get(self, request):
        form = Recipe()
        context = {
            'form': form,
        }
        return render(request, 'recipes/list.html', context)

    def post(self, request):
        form = Recipe(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, 'recipes/detail.html', context)



# IN URLS.PY FILE:

from django.urls import path
from . import views

app_name = 'recipes'

urlspatterns = [
    # http://127.0.0.1:8000/recipes
    path('', views.RecipeView.as_view(), name='list_view'),
    # http://127.0.0.1:8000/recipes/12
    path('<int:id>', views.RecipeView.as_view(), name='detail_view'),
    # Crucial: this 'name' above is the 'pattern name' you'll use to build URL's in templates.
]



# IN LIST-TEMPLATE (list.html):

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



# IN DETAIL-TEMPLATE (detail.html):

<html>
    <body>
    
        {% for field in form %}
            <div class="css-class-example">{{ field }}</div>
        {% endfor %}
        
        <a href="{% url 'recipes:list_view' %}">Back to recipe list</a>
    
    </body>
</html>