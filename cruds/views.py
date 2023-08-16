from django.shortcuts import render
from .models import customer_profile

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def endgame(request):
    return render(request, 'endgame.html')


def signup(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('password2')
        securityCode = request.POST.get('sqcode')
        prof = customer_profile(UserName=userName, Email=email, Password=password, ConfirmPassword=confirmPassword, SecurityCode=securityCode)
        prof.save()
        print(userName, email, password, confirmPassword, securityCode)
            
       
    return render(request, 'signup.html')



def signin(request):
    return render(request, 'signin.html')