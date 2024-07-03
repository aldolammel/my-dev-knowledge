
"""
 USING QUERYSET VIA VIEWS.PY

"""

from django.shortcuts import render
from .models import Recipe                    
from django.db.models import Avg, Count, Sum      # Crucial to use aggregation resources!


# Create your views here.
def index(request):


    # Counting how many items/entries we got in 'Recipe' table:
    count_the_entries = Recipe.objects.aggregate(Count('id'))
    
    
    # Average of the price attribute (column) in Recipe table:
    price_average = Recipe.objects.aggregate(Avg('price'))
    
    
    # Sum of the price attribute (column) in Recipe table:
    price_sum = Recipe.objects.aggregate(Sum('price'))
    
    
    return render(request, "recipes/index.html", {'recipes': count_the_entries})    # <<--- to test, change here ;)