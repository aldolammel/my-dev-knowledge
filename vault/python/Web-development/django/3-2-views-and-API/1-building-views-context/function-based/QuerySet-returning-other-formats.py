"""
FUCTION-BASED METHOD: USING QUERYSET VIA VIEWS.PY (OTHER FORMATS)

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
    as_tuple = Recipe.objects.filter(id=7).values_list()
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
    as_bool = Recipe.objects.filter(id=7).exists()
    """ Output: True """

    # Context must always be a dictionary:
    context = {
        'as_obj': as_obj,  # In the template (index.html), it'll be called as {{ as_obj }}.
        'as_dict': as_dict,
        'as_tuple': as_tuple,
        'as_bool': as_bool,
    }

    return render(request, "recipes/index.html", context)
