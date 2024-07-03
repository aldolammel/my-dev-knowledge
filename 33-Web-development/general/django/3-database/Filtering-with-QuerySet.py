
"""
 USING QUERYSET VIA VIEWS.PY

"""

from django.shortcuts import render
from .models import Recipe                             # Crucial: I'm importing the specific table from the same app i'm working on views.py.

# Create your views here.
def index(request):
    recipes_all = Recipe.objects.all()                 # showing all objects in a specific table
    recipes_one = Recipe.objects.first()               # showing the first entry on this model/table (Recipe).
    recipes_specific = Recipe.objects.get(id=4)        # showing the entry with pk/id = 4.
    all_from_category = Recipe.objects.filter(category__name__iexact='salad')  # This 'i' before 'exact' means
                                                                               # the search must not be case-sensitive.
    # context = { 'recipes': recipes}
    return render(request, "recipes/index.html", {'recipes': all_from_category})    # to test, change here ;)