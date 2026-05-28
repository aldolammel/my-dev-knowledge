"""
FUCTION-BASED METHOD: USING QUERYSET VIA VIEWS.PY (AGGREGATION)

"""

from django.shortcuts import render
from .models import Recipe
from django.db.models import Avg, Count, Sum, Q  # Crucial to use aggregation resources!


# Create your views here.
def index(request):

    # Counting how many items/entries we got in 'Recipe' table:
    count_the_entries = Recipe.objects.aggregate(Count('id'))

    # Average of the price attribute (column) in Recipe table:
    price_average = Recipe.objects.aggregate(Avg('price'))

    # Sum of the price attribute (column) in Recipe table:
    price_sum = Recipe.objects.aggregate(Sum('price'))

    # Conditional result, using Local Operator 'OR' through Q class:
    one_or_another = Recipe.objects.filter(
        Q(name__istartswith='a') | Q(description__icontains='salt')
    )
    """ In Django '|' means the logical operator 'OR'. 
    Remember: those initial 'i' in 'istartswith' and 'icontains' mean the case-sensitive is off. """

    # Context must always be a dictionary:
    context = {
        'count': count_the_entries,  # In the template (index.html), it'll be called as {{ count }}.
        'price_average': price_average,
        'price_sum': price_sum,
        'one_or_another': one_or_another,
    }

    return render(request, "recipes/index.html", context)
