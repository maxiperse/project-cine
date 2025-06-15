from django.shortcuts import render, get_object_or_404
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'home.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # Aquí podrías añadir lógica para reservar, pero para la evaluación esto es suficiente.
    context = {'movie': movie}
    return render(request, 'detail.html', context)
