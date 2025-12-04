

DJANGO > VIEWS.PY: BUILDING THE CONTEXT

    
    >> Here 'Context' is the package of data that a sub-app-view (back-end) sends to
        the template (front-end);

    
    >> All views of a sub-app must be in the automatically created sub-app views.py file;


    >> If something from the database is visible in a template (html) it's because the data
        was called by some sub-app views.py class or function;

    
    >> In order to alocate data in a view, most of the time you'll have to set the data in a
        dictionary named as 'context' (convention);

        views.py e.g.

            # A view-function-based example:
            def view_name_example(request):

                <code>

                context = {
                    'recipes': recipes,  # In the template (index.html), it'll be called as {{ recipes }}.
                    'restaurants': restaurants,
                    'has_error': False,
                }
                return render(request, "recipes/index.html", context)


            # A view-class-based example:
            class ViewNameExample(View):

                <IDK YET!!!!!!>


    >> Another example, using the same logic of Context convention:

        >> Avoid to declare your context dictionary like this...
          
             return render(request, 'template_path_here.html', {'key1': 'value1', 'key2': 'value2'})


        >> Instead, declare like this:

                context = {
                    'key1': 'value1',
                    'key2': 'value2',
                }
                return render(request, 'template_path_here.html', context)


        >> You could easily add new variables in your dictionary (context) dynamically through
            your views functions/classes, using it (below) before returning render():

                context['key3'] = 'value3'