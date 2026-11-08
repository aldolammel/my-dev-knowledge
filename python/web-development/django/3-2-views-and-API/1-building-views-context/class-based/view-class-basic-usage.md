#### Python > Django > Views > Class-based
# View class basic implementation example
---
## Before:
- About this implementation: [/python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/\_views-class-basic](/python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/_views-class-basic.md)

---
## In `/apps/subapp/views.py`:
```python
from django.shortcuts import render
from django.views import View
from .models import Recipe  # hypothetical class just for example purposes.


# Creating a class that inherits the most basic Django views, perfect to create your own view class.
# In this case, 'View' class:
class RecipeView(View):
    # To show data from database:
    def get(self, request):
        form = Recipe()
        context = {
            'form': form,
        }
        return render(request, 'recipes/list.html', context)

    # To update data to database:
    def post(self, request):
        form = Recipe(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, 'recipes/detail.html', context)

```

---
## In `/apps/subapp/urls.py`:
```python
from django.urls import path
from . import views

app_name = 'recipes'

urlspatterns = [
    # http://127.0.0.1:8000/recipes
    path('', views.RecipeView.as_view(), name='list_view'),
    # http://127.0.0.1:8000/recipes/12
    path('<int:pk>', views.RecipeView.as_view(), name='detail_view'),
    # Crucial: this 'name' argument above is the 'pattern name' you'll use to build URL's in templates.
]
```

---
## In `/apps/subapp/templates/xxxxx/list.html` (list-template):
```python
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

```

---
## In `/apps/subapp/templates/xxxxx/detail.html` (detail-template):
```html
<html>
    <body>
    
        {% for field in form %}
            <div class="css-class-example">{{ field }}</div>
        {% endfor %}
        
        <a href="{% url 'recipes:list_view' %}">Back to recipe list</a>
    
    </body>
</html>
```

---



