from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignupForm
from .models import Profile
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'gameplatform/index.html' )


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create user
            newuser = User.objects.create_user(form.cleaned_data['username'],
                                               email=form.cleaned_data['email'],
                                               password=form.cleaned_data['password'],
                                               )
            newuser.save()

            # Create and save a profile object linked to this user
            profile = Profile(user=newuser)
            account_create_successful = "Account created successfully! You may now log in."
            return render(request, 'gameplatform/message.html', {
                'message': account_create_successful
            })


    else:
        form = SignupForm()
    return render(request, 'gameplatform/signup.html', {'sign_up': form} )