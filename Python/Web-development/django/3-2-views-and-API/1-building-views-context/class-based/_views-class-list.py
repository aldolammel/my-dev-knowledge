
"""
    VIEWS CLASSES > CLASS-BASED: USING LIST INHERIT

    >> A subclass of 'TemplateView' class designed for displaying a list of objects. 
        It automates the process of fetching data from a model and rendering it in a template.

    >> Perfect when you need to display a list of objects from a database, such as a category of pages or posts;
"""
                

# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from django.views.generic import ListView


class ProductsListView(ListView):  # This 'View' in classname is a convention.
    model = <ModelClass>
    template_name = '<HtmlTemplatePath>'
    context_object_name = 'products'

        
"""    
    HOW TO USAGE (EXAMPLE):
        ./view-class-list-usage.py

    WHO INHERIT LIST-VIEW CLASS:        
        >> No one!
"""