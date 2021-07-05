from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Movie


def index(request):
    movies = Movie.objects.all()  # SELECT * FROM movies_movie
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)  # GET a single Movie FROM movies_movie OR Raise 404 error.
    return render(request, 'movies/detail.html', {'movie': movie})

