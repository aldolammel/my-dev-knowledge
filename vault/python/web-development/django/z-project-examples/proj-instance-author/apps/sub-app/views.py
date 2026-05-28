from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm


@login_required
def index(request):
    user_movies = Movie.objects.filter(created_by=request.user)
    context = {
        'user_movies': user_movies,
    }
    return render(request, 'movies/index.html', context)


@login_required
def movie_detail(request, movie_id=None):
    if movie_id:
        movie = get_object_or_404(Movie, id=movie_id, created_by=request.user)
    else:
        movie = None

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('movies:index')
    else:
        form = MovieForm(instance=movie)

    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/movie.html', context)


@login_required
def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, created_by=request.user)
    movie.delete()
    return redirect('movies:index')
