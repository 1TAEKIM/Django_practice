from django.shortcuts import render, redirect
from .models import Movie

def main(request):

    movies=  Movie.objects.all()
    context = {
        
        'movies': movies
    }

    return render(request, 'movies/main_page.html', context)



def create_movie(request):
    
    if request.method == 'POST':
        data = request.POST
        print(data)
        
        new_movie = Movie.objects.create(
            title=data.get('create_movie_title'),
            content=data.get('create_movie_content'),
            is_open=data.get('create_movie_is_open')
        )
        
        return redirect('movies:detail', pk=new_movie.pk)

    return render(request, 'movies/create_movie.html')


def detail(request, pk):

    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    
    if request.method == 'POST':
        data = request.POST
        print(data)
        
        Movie.objects.filter(pk=pk).delete()
        
        return redirect('movies:main')
    
    return render(request, 'movies/detail_page.html', context)

def delete(request, pk):
    
    data = request.POST
    Movie.objects.filter(pk=pk).delete()
        
    return redirect('movies:main')

def update(request, pk):
    
    if request.method == 'POST':
        data = request.POST
        Movie.objects.filter(pk=pk).update(
            title=data.get('update_movie_title'), content=data.get('update_movie_content'))
        
        return redirect('movies:detail', pk=pk)

    return render(request, 'movies/update_page.html')