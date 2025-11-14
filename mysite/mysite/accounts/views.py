from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import User

def signup_view(request):
    message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                message = 'User already exists. Please choose another username.'
            else:
                form.save()
                return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'message': message})

def login_view(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username, password=password).exists():
                return redirect('project_home')
            else:
                message = 'Invalid username or password.'
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form, 'message': message})

def project_home(request):
    return render(request, 'accounts/project_home.html')

