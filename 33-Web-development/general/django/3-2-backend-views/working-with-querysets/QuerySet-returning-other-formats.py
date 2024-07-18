
"""
 USING QUERYSET VIA VIEWS.PY

"""

from django.shortcuts import render
from .models import Recipe


# Create your views here.
def index(request):
    
    # Return as object (default):
    as_obj = Recipe.objects.filter(id=7)
    """ Output: <QuerySet [<Recipe: African Chicken Curry>]> """
    
    # Return as dictionary: 
    as_dict = Recipe.objects.filter(id=7).values()
    """ Output: <QuerySet [{'id': 7, 'name': 'African Chicken Curry', 'description': 'Are you ready!', 'date_added': datetime.datetime(2024, 7, 3, 15, 29, 41, 39059, tzinfo=datetime.timezone.utc), 'category_id': 1}]> """

    # Return as tuple: 
    as_tuple = Recipe.objects.filter(id=7).values_list()
    """ Output: <QuerySet [(7, 'African Chicken Curry', 'Are you ready!', datetime.datetime(2024, 7, 3, 15, 29, 41, 39059, tzinfo=datetime.timezone.utc), 1)]> """

    # Return as boolean:
    as_bool = Recipe.objects.filter(id=7).exists()
    """ Output: True """

    return render(request, "recipes/index.html", {'recipes': as_tuple})    # <<--- to test, change here ;)

