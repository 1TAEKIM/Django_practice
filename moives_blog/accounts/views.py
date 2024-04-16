from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from reviews.models import reviews, Comment



# Create your views here.
def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # contrib.auth 패키지의 login 함수를 사용하는데
            # 현재 함수와 이름이 중복이므로 별명을 지어서 사용
            # login(request,form.get_user())
            
            auth_login(request, form.get_user())
            return redirect('accounts:info')
            
    else:
        form = AuthenticationForm()
    
    context = {
        'form':form
    }
    
    return render(request, 'accounts/login_page.html', context)

def index(request):
    
    return render(request, 'accounts/index.html')

@login_required
def info(request):
    
    review = reviews.objects.filter(user_id=request.user.id)
    
    context = {
        'reviews' : review,

    }
    
    
    return render(request, 'accounts/user_info.html', context)

    
    
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:info')
        
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form':form
    }
    
    return render(request, 'accounts/signup.html', context)

def delete(request):
    request.user.delete()
    return redirect('accounts:login')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:info')
    else:
        form = CustomUserChangeForm(instance=request.user)
        
    context = {
        'form':form
    }
    return render(request, 'accounts/update.html', context)


def change_password(request, user_id):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:info')
    else:
        form = PasswordChangeForm(request.user)
        
    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)