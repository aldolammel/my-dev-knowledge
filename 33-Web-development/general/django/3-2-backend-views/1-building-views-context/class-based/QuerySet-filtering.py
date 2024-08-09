"""
CLASS-BASED METHOD: USING QUERYSET VIA VIEWS.PY (FILTERING)

"""

from django.shortcuts import render
from django.views.generic import View
from .models import Recipe


class Recipes(View):
    model = Recipe
    template_name = 'recipes/custom.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        # Showing the first entry on this model/table (Recipe):
        return Recipe.objects.first()
        # Showing the entry with pk/id = 4:
        return Recipe.objects.get(id=4)
        # Showing all objects in a specific table (Recipe):
        return Recipe.objects.all()
        # Showing a specific number of entries:
        return Recipe.objects.all()[:3]
        """ Using the slicing technic. """
        # Showing all entries greater than a value:
        return Recipe.objects.filter(id__gt=3)
        """ This 'id__' is the column (attribute) you want to search, 
        and that '__gt' means 'greater than' command. 
        You can use '__gte' for 'greater than or equal to' command."""
        # Filtering only entries from a specific category:
        return Recipe.objects.filter(category__name__iexact='salad')
        """ This 'i' before 'exact' ('__iexact') means the search must not be case-sensitive. 
        And '__exact' is case-sensitive. 
        Be aware 1: this '__name__' is exactly the attribute the filter will be applied.
        If you're looking for 'author' it must be written as '__author__'.
        Be aware 2: not sure, but maybe the 'category__' is editable too."""
        # Filtering only entries that contain a certain string in its name:
        return Recipe.objects.filter(category__name__icontains='soup')
        """ This 'i' before 'contains' means the search must not be case-sensitive.
        'category__name__contains' is case-sensitive.
        Be aware 1: this '__name__' is exactly the attribute the filter will be applied.
        If you're looking for 'author' it must be written as '__author__'.
        Be aware 2: not sure, but maybe the 'category__' is editable too."""
        # Filtering only entries that DON'T contain a certain string in its name:
        return Recipe.objects.exclude(name__icontains='soup')
        """ This 'i' before 'contains' means the search must not be case-sensitive.
        'name__contains' is case-sensitive.
        Be aware: this 'name__' is exactly the attribute the exclude will be applied.
        If you're looking for 'author' it must be written as 'author__contains'."""
        # Filtering even more:
        return Recipe.objects.exclude(name__icontains='soup').order_by('-date_added')
        """ This '-date_added' is asking for descending order of date_added. """
