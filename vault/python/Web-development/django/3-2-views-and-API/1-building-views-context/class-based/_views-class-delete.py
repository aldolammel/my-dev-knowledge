
"""
    VIEWS CLASSES > CLASS-BASED: USING DELETE INHERIT

    >> Provides the ability to delete an object from the database. 
        It typically asks for confirmation before deletion;

    >> Perfect when you need to allow users to delete records, such as deleting a blog post 
        or removing a user account;
"""
                
    
# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from django.views.generic import DeleteView
from django.urls import reverse_lazy


class BlogPostDeleteView(DeleteView):
    model = <ModelClass>
    template_name = '<HtmlTemplatePath>'
    success_url = reverse_lazy('blogpost_list')


"""    
    HOW TO USAGE (EXAMPLE):
        ./view-class-delete-usage.py

    WHO INHERIT DELETE-VIEW CLASS:
        >> No one!
"""
