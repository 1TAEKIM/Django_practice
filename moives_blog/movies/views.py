from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')

def create_movie(request):
    return render(request, 'movies/create_movie.html')