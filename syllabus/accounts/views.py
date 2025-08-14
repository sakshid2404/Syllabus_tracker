from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    return render(request, 'accounts/home.html')

@login_required
def some_protected_view(request):
    ...

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')
