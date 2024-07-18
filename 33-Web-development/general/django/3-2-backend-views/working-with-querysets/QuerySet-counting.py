
"""
 USING QUERYSET VIA VIEWS.PY

"""

from django.shortcuts import render
from .models import Recipe                    
from django.db.models import Count      # Crucial to use aggregation counting!


# Create your views here.
def index(request):

    # Counting how many items/entries we got (using Count Class):
    total_using_a_class = Recipe.objects.aggregate(Count('id'))
    
    # Counting how many items/entries we got (using Count Method):
    total_using_a_method = Recipe.objects.all().count()
    
    # Counting how many items/entries in a filter we got (using Count Method):
    subtotal_using_a_method = Recipe.objects.filter(id__gt=5).count()
    
    # Counting how many items/entries in a filter we got (using Count Class)
    subtotal_using_a_class = Recipe.objects.filter(id__gt=5).aggregate(Count('id'))

    return render(request, "recipes/index.html", {'recipes': subtotal_using_a_class})    # <<--- to test, change here ;)