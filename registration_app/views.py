from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, "registration/login.html", {'error_message': 'Invalid username and/or password.'})
    return render(request, "registration/login.html")

def logout_view(request):
    logout(request)
    return redirect('homepage')

