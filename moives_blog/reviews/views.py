from django.shortcuts import render, redirect
from .models import reviews, Comment
from .forms import reviewsForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def reviews_list(request):
    
    review = reviews.objects.all()
    context = {
        'reviews' : review
    }
    
    return render(request, 'reviews/review_list.html', context)        

@login_required
def review_create(request):
    
    form = reviewsForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        return redirect('reviews:review_list')
    
    context = {
        'form' : form
    }
    
    return render(request, 'reviews/review_create.html', context)


def review_detail(request, pk):
    
    review = reviews.objects.get(pk=pk)
    comments = review.comments.all()
    comment_form = CommentForm()
    context = {
        'review' : review,
        'comments' : comments,
        'comment_form' : comment_form
    }
    
    return render(request, 'reviews/review_detail.html', context)

def create_comment(request, pk):
    review = reviews.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.save()
        return redirect('reviews:review_detail', pk)
    context ={
        'review': review,
        'comment_form' : comment_form
    }
    return render(request, 'reviews/review_detail.html', context)


def review_update(request, pk):
    
    review = reviews.objects.get(pk=pk)
    if request.user != review.user:
        return redirect('reviews:review_list')
    
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
    
    if request.user == review.user:
        review.delete()
        
    return redirect('reviews:review_list')

def delete_comment(request, review_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('reviews:review_detail', review_id)
