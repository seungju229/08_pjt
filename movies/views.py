from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_safe, require_http_methods
from .serializers import GenreSerializers
from .models import Genre, Movie

# Create your views here.
@require_safe
def index(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    context = {
        'genres':genres,
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

@require_safe
def filter_genre(request):
    movies = Movie.objects.get()



@require_safe
def recommended(request):
    pass
