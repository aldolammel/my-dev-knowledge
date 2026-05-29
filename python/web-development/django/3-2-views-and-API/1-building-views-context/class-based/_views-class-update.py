
"""
    VIEWS CLASSES > CLASS-BASED: USING UPDATE INHERIT

    >> Provides a form for updating an existing object. It is similar to CreateView but 
        is used for editing existing objects;

    >> Perfect when you need to allow users to edit existing records, such as updating a blog post
        or editing a user profile;
"""


# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from django.views.generic import UpdateView
from django.urls import reverse_lazy


class BlogPostUpdateView(UpdateView):
    model = <ModelClass>
    fields = ['title', 'content']
    template_name = '<HtmlTemplatePath>'
    success_url = reverse_lazy('blogpost_list')


"""
    HOW TO USAGE (EXAMPLE):    
        ./view-class-update-usage.py

    WHO INHERIT UPDATE-VIEW CLASS:
        >> No one!
"""