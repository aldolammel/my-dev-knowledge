from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView, DetailView


# EXAMPLE USING FUNCTION-BASED METHOD
# The same as the 'RecipesList' class but using the function-based method:
def recipes(request):
    # Collecting all recipes recorded in the Recipe table:
    recipes = Recipe.objects.all()
    # If you wanna pass variables to the template, you need this always as dictionary:
    context = {'recipes': recipes}
    # Return the data to be rendered with the template when a key of the context dict is called:
    return render(request, 'recipes/index.html', context)


# The same as the 'RecipeDetail' class but using the function-based method:
def recipe(request, recipe_id):
    # Collecting a specific recipe in the Recipe table:
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe.html', context)


"""
    MORE OPTIONS:
    /33-Web-development/backend/django/3-2-backend-views/

"""
