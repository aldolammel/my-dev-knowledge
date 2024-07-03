
"""
 USING QUERYSET VIA VIEWS.PY

"""

from django.shortcuts import render
from .models import Recipe                    # Crucial: I'm importing the specific table from the same app i'm working on views.py.


# Create your views here.
def index(request):
    
    
    # Showing the first entry on this model/table (Recipe):
    recipes_one = Recipe.objects.first()
    
    
    # Showing the entry with pk/id = 4:
    recipes_specific = Recipe.objects.get(id=4)


    # Showing all objects in a specific table (Recipe):
    recipes_all = Recipe.objects.all()   
    
    
    # Showing a specific number of entries:
    three_recipes = Recipe.objects.all()[:3]
    """ Using the slicing tecnhic. """
    
    
    # Filtering only entries from a specific category:
    all_from_category = Recipe.objects.filter(category__name__iexact='salad')  
    """ This 'i' before 'exact' means the search must not be case-sensitive. 
    'category__name__exact' is case-sensitive. 
    Be aware 1: this '__name__' is exactly the attribute the filter will be applied.
    If you're looking for 'author' it must be written as '__author__'.
    Be aware 2: not sure, but maybe the 'category__' is editable too."""
    
    
    # Filtering only entries that contain a certain string in its name:
    search_in_category = Recipe.objects.filter(category__name__icontains='soup')
    """ This 'i' before 'contains' means the search must not be case-sensitive.
    'category__name__contains' is case-sensitive.
    Be aware 1: this '__name__' is exactly the attribute the filter will be applied.
    If you're looking for 'author' it must be written as '__author__'.
    Be aware 2: not sure, but maybe the 'category__' is editable too."""
    
    
    # Filtering only entries that DON'T contain a certain string in its name:
    exclude_those_ones = Recipe.objects.exclude(name__icontains='soup')
    """ This 'i' before 'contains' means the search must not be case-sensitive.
    'name__contains' is case-sensitive.
    Be aware: this 'name__' is exactly the attribute the exclude will be applied.
    If you're looking for 'author' it must be written as 'author__contains'."""
    
    
    # Filtering even more:
    super_search = Recipe.objects.exclude(name__icontains='soup').order_by('-date_added')
    """ This '-date_added' is asking for descending order of date_added. """
    
    
    return render(request, "recipes/index.html", {'recipes': all_from_category})    # <<--- to test, change here ;)