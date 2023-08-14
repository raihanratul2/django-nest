from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def endgame(request):
    return render(request, 'endgame.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')