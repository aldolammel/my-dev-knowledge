from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm


def movie_list(request):
    """
    Responsable to show the list of movies on the front-end.
    """
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/movies.html', context)


def movie_add(request):
    """
    Responsable to show the same front-end form of movie_edit function
    but with clean fields to add a new movie.
    """
    # When the form wants to change some in the database:
    if request.method == 'POST':
        # Creating the form object ready to POST method:
        form = MovieForm(request.POST)
        # If form fields validation is alright:
        if form.is_valid():
            # Finally save the changes in db:
            form.save()
            # Send user to the list of movies:
            return redirect('movies:movie_list_view')
    # When the form doesn't change any (GET method):
    else:
        # Creating the form object only to be read (GET):
        form = MovieForm()
    # Defining what will be sent to the front-end/template:
    context = {
        'form': form,
        'page_title': 'Adding movie',
        'bt_submit': 'Add',
    }
    # Load the template:
    return render(request, 'movies/movie.html', context)


def movie_edit(request, movie_id):
    """
    Responsable to show the same front-end form of movie_add function
    but with a specific movie data loaded in fields.
    """
    # Defining the specific movie to update:
    movie = get_object_or_404(Movie, id=movie_id)  # Movie.objects.get(id=movie_id)
    # When the form wants to change some in the database:
    if request.method == 'POST':
        # Defining the form object based in an existent movie in db ready to POST method:
        form = MovieForm(request.POST, instance=movie)
        # If form fields validation is alright:
        if form.is_valid():
            # Finally save the changes in db:
            form.save()
            # Send user to the list of movies:
            return redirect('movies:movie_list_view')
    # When the form doesn't change any (GET method):
    else:
        # Defining the form object based in an existent movie in db
        form = MovieForm(instance=movie)
    # Defining what will be sent to the front-end/template:
    context = {
        'form': form,
        'page_title': 'Editing movie',
        'bt_submit': 'Update',
    }
    # Load the template:
    return render(request, 'movies/movie.html', context)


def movie_delete(request, id):
    pass


"""
    MORE OPTIONS:
    /33-Web-development/backend/python/django/3-2-backend-views/

"""
