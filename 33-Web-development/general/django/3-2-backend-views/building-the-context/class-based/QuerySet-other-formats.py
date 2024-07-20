"""
CLASS-BASED METHOD: USING QUERYSET VIA VIEWS.PY (OTHER FORMATS)

"""

from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe


class Recipes(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        # Return as object (default):
        return Recipe.objects.filter(id=7)
        """ Output: <QuerySet [<Recipe: African Chicken Curry>]> """
        # Return as dictionary:
        return Recipe.objects.filter(id=7).values()
        """ Output: 
            <QuerySet [
                {
                    'id': 7, 
                    'name': 
                    'African Chicken Curry', 
                    'description': 'Are you ready!', 
                    'date_added': datetime.datetime(
                        2024, 
                        7, 
                        3, 
                        15, 
                        29, 
                        41, 
                        39059, 
                        tzinfo=datetime.timezone.utc
                    ), 
                    'category_id': 1
                }
            ]> 
        """
        # Return as tuple:
        return Recipe.objects.filter(id=7).values_list()
        """ Output: 
            <QuerySet [
                (
                    7, 
                    'African Chicken Curry', 
                    'Are you ready!', 
                    datetime.datetime(
                        2024, 
                        7, 
                        3, 
                        15, 
                        29, 
                        41, 
                        39059, 
                        tzinfo=datetime.timezone.utc
                    ), 
                    1
                )
            ]>
        """
        # Return as boolean:
        return Recipe.objects.filter(id=7).exists()
        """ Output: True """
