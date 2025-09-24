
"""
FUCTION-BASED METHOD: USING QUERYSET VIA VIEWS.PY (FILTERING)

"""

from django.shortcuts import render
from .models import Recipe        # Crucial: I'm importing the specific table from the same app i'm working on views.py.


# Create your views here.
def index(request):
    
    # Showing the first entry on this model/table (Recipe):
    r_first = Recipe.objects.first()
    
    # Showing the entry with pk/id = 4:
    r_specific = Recipe.objects.get(id=4)

    # Showing all objects in a specific table (Recipe):
    r_all = Recipe.objects.all()
    
    # Showing a specific number of entries:
    r_three = Recipe.objects.all()[:3]
    """ Using the slicing technic. """

    # Showing all entries greater than a value:
    greater_than = Recipe.objects.filter(id__gt=3)
    """ This 'id__' is the column (attribute) you want to search, 
    and that '__gt' means 'greater than' command. 
    You can use '__gte' for 'greater than or equal to' command."""
    
    # Filtering only entries from a specific category:
    all_from_cat = Recipe.objects.filter(category__name__iexact='salad')  
    """ This 'i' before 'exact' means the search must not be case-sensitive. 
    'category__name__exact' is case-sensitive. 
    Be aware 1: this '__name__' is exactly the attribute the filter will be applied.
    If you're looking for 'author' it must be written as '__author__'.
    Be aware 2: not sure, but maybe the 'category__' is editable too."""

    # Filtering only entries that contain a certain string in its name:
    search_in_cat = Recipe.objects.filter(category__name__icontains='soup')
    """ This 'i' before 'contains' means the search must not be case-sensitive.
    'category__name__contains' is case-sensitive.
    Be aware 1: this '__name__' is exactly the attribute the filter will be applied.
    If you're looking for 'author' it must be written as '__author__'.
    Be aware 2: not sure, but maybe the 'category__' is editable too."""
    
    # Filtering only entries that DON'T contain a certain string in its name:
    exclude_those = Recipe.objects.exclude(name__icontains='soup')
    """ This 'i' before 'contains' means the search must not be case-sensitive.
    'name__contains' is case-sensitive.
    Be aware: this 'name__' is exactly the attribute the exclude will be applied.
    If you're looking for 'author' it must be written as 'author__contains'."""

    # Filtering even more:
    super_search = Recipe.objects.exclude(name__icontains='soup').order_by('-date_added')
    """ This '-date_added' is asking for descending order of date_added. """
    
    # Context must always be a dictionary:
    context = {
        'r_first': r_first,  # In the template (index.html), it'll be called as {{ r_first }}.
        'r_specific': r_specific,
        'r_all': r_all,
        'r_three': r_three,
        'greater_than': greater_than,
        'all_from_cat': all_from_cat,
        'search_in_cat': search_in_cat,
        'exclude_those': exclude_those,
        'super_search': super_search,
    }

    return render(request, "recipes/index.html", context)