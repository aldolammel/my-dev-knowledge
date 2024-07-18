"""
 USING QUERYSET VIA VIEWS.PY

"""

from django.shortcuts import render
from .models import Recipe
from django.db.models import Count  # Crucial to use aggregation counting!


# Create your views here.
def index(request):

    # Counting how many items/entries we got (using Count Class):
    total_class = Recipe.objects.aggregate(Count('id'))

    # Counting how many items/entries we got (using Count Method):
    total_method = Recipe.objects.all().count()

    # Counting how many items/entries in a filter we got (using Count Method):
    subtotal_method = Recipe.objects.filter(id__gt=5).count()

    # Counting how many items/entries in a filter we got (using Count Class)
    subtotal_class = Recipe.objects.filter(id__gt=5).aggregate(Count('id'))

    # Context must always be a dictionary:
    context = {
        'total_class': total_class,  # In the template (index.html), it'll be called as {{ total_class }}.
        'total_method': total_method,
        'subtotal_method': subtotal_method,
        'subtotal_class': subtotal_class,
    }

    return render(request, "recipes/index.html", context)
