'''

VIEWS.PY WITH CLASSES:

    >> 
    
    >> 
    
    

'''

from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView


class RecipeList(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'
    
