from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def index(request):
    movies = Movie.objects.all()  # SELECT * FROM movies_movie
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id) # GET a single Movie FROM movies_movie
    return render(request, 'movies/detail.html', {'movie': movie})

