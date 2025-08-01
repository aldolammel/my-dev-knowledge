"""
CLASS-BASED METHOD: USING QUERYSET VIA VIEWS.PY (AGGREGATION)

"""

from django.shortcuts import render
from django.views.generic import View
from .models import Recipe
from django.db.models import Avg, Count, Sum, Q  # Crucial to use aggregation resources!


class RecipesView(View):
    model = Recipe
    template_name = 'recipes/custom.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        # Counting how many items/entries we got in 'Recipe' table:
        return Recipe.objects.aggregate(Count('id'))
        # Average of the price attribute (column) in Recipe table:
        return Recipe.objects.aggregate(Avg('price'))
        # Sum of the price attribute (column) in Recipe table:
        return Recipe.objects.aggregate(Sum('price'))
        # Conditional result, using Local Operator 'OR' through Q class:
        return Recipe.objects.filter(Q(name__istartswith='a') | Q(description__icontains='salt'))
        """ In Django '|' means the logical operator 'OR'. 
        Remember: those initial 'i' in 'istartswith' and 'icontains' mean the case-sensitive is off. """

        # LOOK THIS OUT:
        """
            Old videos from Django show these differences:
            
                def get_queryset(self):
                    base_query = super().get_queryset()
                    data = base_query.filter(id__gt=1)
                    return data
        """
