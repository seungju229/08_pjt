from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Genre, Movie
from django.http import JsonResponse
import json


# Create your views here.
@require_safe
def index(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    context = {
        'genres': genres,
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


def filter_genre(request):
    body = json.loads(request.body)
    genre_name = body.get('genre')

    print(genre_name)
    genre = Genre.objects.filter(name=genre_name).first()

    movies = Movie.objects.filter(genres=genre)
    movies_list = list(movies.values())
    context = {
        'movies': movies_list,
    }
    return JsonResponse(context)


@require_safe
def recommended(request):
    pass
