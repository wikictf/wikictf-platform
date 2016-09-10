from django.shortcuts import render
from .forms import SignupForm
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'gameplatform/index.html' )

def signup(request):
    return render(request, 'gameplatform/signup.html', {'sign_up': SignupForm()} )