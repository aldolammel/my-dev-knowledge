# IN VIEWS.PY FILE:

from django.views.generic.base import RedirectView


# Creating another class that also inherits pre-defined features brought by Django.
# In this case, 'RedirectView' class:
class DevelopedByView(RedirectView):  # This 'View' in classname is a convention.
    # Defining where to redirect the visitor:
    url = 'https://abcoo.com.br'





# IN URLS.PY FILE: ---------------------------------------------------------------------------------

from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    # http://127.0.0.1:8000/by/
    path('by', views.DevelopedByView.as_view(), name='developed_view'),
]



    
# IN THE HTML: -------------------------------------------------------------------------------------

<html>
    <footer>
    
        <p>Developed by <a href="{% url 'general:developed_view' %}" target="_blank">ABCOO</a></p>
        
    </footer>
</html>