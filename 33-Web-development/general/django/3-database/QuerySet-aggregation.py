
"""
 USING QUERYSET VIA VIEWS.PY

"""

from django.shortcuts import render
from .models import Recipe                    
from django.db.models import Avg, Count, Sum, Q      # Crucial to use aggregation resources!


# Create your views here.
def index(request):

    # Counting how many items/entries we got in 'Recipe' table:
    count_the_entries = Recipe.objects.aggregate(Count('id'))

    # Average of the price attribute (column) in Recipe table:
    price_average = Recipe.objects.aggregate(Avg('price'))
    
    # Sum of the price attribute (column) in Recipe table:
    price_sum = Recipe.objects.aggregate(Sum('price'))

    # Conditional result, using Local Operator 'OR' through Q class:
    one_or_another = Recipe.objects.filter(Q(name__istartswith='a') | Q(description__icontains='salt'))
    """ In Django '|' means the logical operator 'OR'. 
    Remember: those initial 'i' in 'istartswith' and 'icontains' mean the case-sensitive is off. """

    return render(request, "recipes/index.html", {'recipes': count_the_entries})    # <<--- to test, change here ;)