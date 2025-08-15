from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
<<<<<<< HEAD
            return redirect('syllabus-list')  
=======
            return redirect('home')  
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('syllabus-list')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')
