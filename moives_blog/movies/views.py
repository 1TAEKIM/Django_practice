from django.shortcuts import render

def main_page(request):
    print(request.GET)

    req_data = request.GET

    context = {
       'create_movie' : req_data.get('create_movie') 
        if req_data else '영화가 없습니다.'
    }

    return render(request, 'movies/main_page.html', context)



def create_movie(request):

    return render(request, 'movies/create_movie.html')


def detail_page(request):


    return render(request, 'movies/detail_page.html')