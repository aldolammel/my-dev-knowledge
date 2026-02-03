
"""
    VIEWS CLASSES > CLASS-BASED: USING TEMPLATE INHERIT

    >> A subclass of 'View' (basic class) that renders a template. It automatically handles 
        GET requests and provides context data to the template;

    >> Perfect when you simply need to render a template with context data and don’t require
        complex logic beyond that;
"""
                

# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from django.views.generic.base import TemplateView


class ThankYouMsgView(TemplateView):
    template_name = '<HtmlTemplatePath>'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "It was very much appreciated!"
        return context


"""
    HOW TO USE (EXAMPLE):
        ./view-class-template-usage.py

    WHO INHERIT TEMPLATE-VIEW CLASS:
        >> ListView
        >> DetailView
"""