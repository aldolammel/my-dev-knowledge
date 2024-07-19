from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView


def recipes(request):
    # Collecting all recipes recorded in the Recipe table:
    recipes = Recipe.objects.all()
    # If you wanna pass variables to the template, you need this always as dictionary:
    context = {'recipes': recipes}
    # Return the data to be rendered with the template when a key of the context dict is called:
    return render(request, 'recipes/index.html', context)


def recipe(request, recipe_id):
    # Defining the recipe:
    recipe = Recipe.objects.get(id=recipe_id)
    # If you wanna pass variables to the template, you need this always as dictionary:
    context = {'recipe': recipe}
    # Return the data to be rendered with the template when a key of the context dict is called:
    return render(request, 'recipes/recipe.html', context)


class RecipesList(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'
    # Check the urls.py file to see how this class-based method is different from the
    # function-based method.
