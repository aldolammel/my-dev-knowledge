'''

VIEWS.PY WITH FUNCTIONS:

    >> 
    
    >> 
    
    

'''


# 1) IN SUB-APP VIEWS.PY:

    from django.shortcuts import render
    from .models import Recipe


    def recipes(request):
        # Collecting all recipes recorded in the Recipe table:
        recipes = Recipe.objects.all()
        # If you wanna pass variables to the template, you need this always as dictionary:
        context = {'recipes': recipes}
        # Return the data to be rendered with the template when a key of the context dict is called:
        return render(request, 'recipes/index.html', context)


    def recipe(request, recipe_id):
        # Collecting a specific recipe in the Recipe table:
        recipe = Recipe.objects.get(id=recipe_id)
        context = {'recipe': recipe}
        return render(request, 'recipes/recipe.html', context)




# 2) IN SUB-APP URLS.PY:

    from django.urls import path
    from . import views
    
    app_name = 'recipes'
    urlpatterns = [
        # http://127.0.0.1:8000/recipes or http://127.0.0.1:8000/recipes/index.html
        path('', views.recipes, name='list_view'),
        # http://127.0.0.1:8000/recipes/1
        path('<int:recipe_id>', views.recipe, name='detail_view'),
        # Crucial: this 'name' above is the 'pattern name' you'll use to build URL's in templates.
    ]




# 3) IN SOME TEMPLATE TO LIST RECIPES:

    <html>
        <body>
        
            {% if recipes %}    # <---- magic variable from class-based views!
            
                {% for i in recipes %}
                
                    <p><a href="{% url 'subapp_namespace:detail_view' i.id %}">{{ i }}</a></p>
                    
                {% endfor %}
                
            {% endif %}
            
        </body>
    </html>