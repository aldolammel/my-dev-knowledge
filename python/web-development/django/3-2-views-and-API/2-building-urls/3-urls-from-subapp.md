#### Python > Django > Router
# Sub-app `urls.py` file

---

==Just makin' it clear==
"Sub-apps" are every folder in the first level of `/apps/` folder that Django says they are "apps" from your app. Personally, I hate this name so I call them as "sub-apps" from my Django app. 

---

The `/apps/sub-app-name/urls.py` file is where you declare all URLs (endpoints) that belong specifically to a sub-app. 

Remember: once you declare an endpoint here, it's expected the endpoint logic is already built through the sub-app `views.py` file!

Every sub-app `urls.py` file MUST be tied to the `/core/urls.py`!

---

```python
from django.urls import path
from . import views

# NAMESPACE
# By convention, it defines the sub-app namespace:
# It'll be used, for example, when we create routes on templates.
app_name = 'recipes'

# EXAMPLE USING CLASS-BASED METHOD
# Declaring every sub-app endpoint (routes):
urlpatterns = [
    # http://localhost:8000/recipes or http://localhost:8000/recipes/index.html
    path('', views.RecipesList.as_view(), name='list_view'),
    # http://localhost:8000/recipes/1
    path('<int:pk>', views.RecipeDetail.as_view(), name='detail_view'),
    # Crucial: this 'name' above is the 'pattern name' you'll use to build the URL's in templates.
]
```
Example using function-based method:
```python
# Declaring every sub-app endpoint (routes):
urlpatterns = [
    # http://localhost:8000/recipes or http://localhost:8000/recipes/index.html
    path('', views.recipes, name='list_view'),
    # http://localhost:8000/recipes/1
    path('<int:recipe_id>', views.recipe, name='detail_view'),
    # Crucial: this 'name' above is the 'pattern name' you'll use to build the URL's in templates.
]
```

---
## Initial `/apps/subapp/urls.py` file for your project:
[/python/web-development/django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/urls.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/urls.py)

---
## Path converters:
[/python/web-development/django/3-2-views-and-API/2-building-urls/path-converters](/python/web-development/django/3-2-views-and-API/2-building-urls/path-converters.md)


