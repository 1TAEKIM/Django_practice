from django.shortcuts import render, redirect
from .models import reviews
from .forms import reviewsForm

# Create your views here.
def reviews_list(request):
    
    review = reviews.objects.all()
    context = {
        'reviews' : review
    }
    
    return render(request, 'reviews/review_list.html', context)        

def review_create(request):
    
    form = reviewsForm(request.POST)
    if form.is_valid():
        review = form.save()
        return redirect('reviews:review_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'reviews/review_create.html', context)

def review_detail(request, pk):
    
    review = reviews.objects.get(pk=pk)
    context = {
        'review' : review
    }
    
    return render(request, 'reviews/review_detail.html', context)

def review_update(request, pk):
    
    review = reviews.objects.get(pk=pk)
    
    context = {
        'review' : review
    }
    
    if request.method == 'POST':
        data = request.POST
        reviews.objects.filter(pk=pk).update(
            review_title=data.get('update_review_title'), 
            review_content=data.get('update_review_content')
        )
        return redirect('reviews:review_detail', pk=pk)
    
    return render(request, 'reviews/review_update.html', context)