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
    if request.method == 'POST':
        form = reviewsForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:review_detail', pk=review.pk)
    else:
        form = reviewsForm(instance=review)
        
    context = {
        'form' : form,
        'review' : review
    }
    
    return render(request, 'reviews/review_update.html', context)


def review_delete(request, pk):
    
    review = reviews.objects.get(pk=pk)
    if review:
        review.delete()
        
    return redirect('reviews:review_list')