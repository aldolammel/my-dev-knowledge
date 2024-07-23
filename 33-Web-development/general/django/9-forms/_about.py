


    """
    DJANGO FORMS:
    
        >> Unless you're planning to build websites and applications that do nothing but publish
            content, and don't accept input from your visitors, you're going to need to understand 
            and use forms. Django provides a range of tools and libraries to help you build forms to
            accept input from site visitors, and then process and respond to the input.
            
            That said: The forms.py is for all data that can be inputed to database from a
                        front-end form!

        
        >> Forms always are created in forms.py file into the sub-app folder;
        
        >> There are two ways to build up a front-end form:
        
            1) Connecting a models.py class to a forms.py class (inherit from forms.ModelForm);
            2) Creating a custom forms.py class (inherit from forms.Form);

        >> Let's imagine you got in the models.py file a class to record movies with a few fields to
        fill. Now, to the user add movies from the front-end, we need to create a form class to
        connect the database with the template:
    
    """
    
        # 1) In some sub-app folder, create a file called 'forms.py';

        
        # 2) In the new sub-app forms.py file, create the class:

            # E.g.

                # Importing:
                from django import forms
                from .models import Movie
                
                # Create a class specifically for this form:
                class MovieForm(forms.ModelForm):

                    # Call this the built-in class:
                    class Meta:

                        # Connecting the form with the model/table it will populate:
                        model = Movie  # assuming it's the table you got in your models.py;

                        # Bring all class attributes/database columns that will be worked by form:
                        fields = '__all__'
                        # or only a few of them: 
                        fields = [
                            'title',
                            'rating',
                        ]
                        # or show all but less them:
                        exclude = ('release_year',)
                        # Customizing each field name:
                        labels = {
                            'title': 'Movie title',
                            'rating': 'Your personnal rating',
                        }
                    

    
        # 3) In the sub-app views.py, create the function-view or the class-view responsable for
        #   this form to be used in a template:

            # E.g.
                
                # Importing:
                from django.shortcuts import render, redirect, HttpResponse
                
                # Using a function-based method:
                def movie_add(request):
                    # When the application need to save something from the page:
                    if request.method == 'POST':
                        form = MovieForm(request.POST)
                        if form.is_valid():
                            # Finally record the new things on the database:
                            form.save()
                            # After that, send user to another page:
                            return redirect('movies_namespace:list_view')
                        # If NOT valid, load the page again (GET), but keeping
                        # the form data already validated:
                        else:
                            context = {'form': form}
                    # When the application just need to print the page:
                    else:
                        form = MovieForm()
                        context = {'form': form}
                    #
                    return render(request, 'movies/add.html', context)



        # 4) In the sub-app urls.py file, do it:

            # E.g.
            
                # Importing:
                from . import views

                # Namespace:
                app_name = 'movies_namespace'
                
                urlpatterns = [
                    # Assuming the movie class has a list view (with class-based view):
                    # http://127.0.0.1:8000/movies/  or  # http://127.0.0.1:8000/movies/index.html
                    path('', views.MoviesList.as_view(), name='list_view'),
                    # http://127.0.0.1:8000/movies/new
                    path('new/', views.movie_add, name='form_new'),
                ]



        # 5) In the sub-app template 'movies/add.html', let's apply the form:

            {% block content %}
                
                <h1>Adding New Movie</h1>

                <form method="post" action="."> # action = '.' means the same page.

                    # Add this on each form for Django security reason:
                    {% csrf_token %}
                    # Load the entire form where each form field will be a div:
                    {{ form.as_div }}

                    <button type="submit">Save</button>
                    
                </form>
                
            {% endblock content %}


