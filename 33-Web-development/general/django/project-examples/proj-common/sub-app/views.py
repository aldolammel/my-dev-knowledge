from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView, DetailView



# EXAMPLE USING CLASS-BASED METHOD:


    # The same as 'recipes' function but using the class-based method:
    class RecipesList(ListView):
        # Attaching the table (defined in some models.py) will feed this view-class:
        model = Recipe
        # Defining with template must be used to show the data:
        template_name = 'recipes/index.html'
        # Defining the name you will call the data (variable) on the templates:
            # Custom definition:
            context_object_name = 'recipes'
            # Or the default one:
            # object_list   <-- call this in template to call automatically all data from the model!
    
    # The same as 'recipe' function but using the class-based method:
    class RecipeDetail(DetailView):
        model = Recipe
        template_name = 'recipes/recipe.html'
        context_object_name = 'recipe'



# EXAMPLE USING FUNCTION-BASED METHOD:

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


