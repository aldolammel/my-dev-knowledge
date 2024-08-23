"""
CLASS-BASED METHOD: USING QUERYSET VIA VIEWS.PY (COUNTING)

"""

from django.shortcuts import render
from django.views.generic import View
from .models import Recipe
from django.db.models import Count  # Crucial to use aggregation counting!


class RecipesView(View):
    model = Recipe
    template_name = 'recipes/custom.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        # Counting how many items/entries we got (using Count Class):
        return Recipe.objects.aggregate(Count('id'))
        # Counting how many items/entries we got (using Count Method):
        return Recipe.objects.all().count()
        # Counting how many items/entries in a filter we got (using Count Method):
        return Recipe.objects.filter(id__gt=5).count()
        # Counting how many items/entries in a filter we got (using Count Class)
        return Recipe.objects.filter(id__gt=5).aggregate(Count('id'))
