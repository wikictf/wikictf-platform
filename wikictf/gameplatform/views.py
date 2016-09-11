from django.shortcuts import render
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm
from .models import Profile, Problem
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

@login_required
def play(request):
    problem_list = Problem.objects.all().order_by("value")
    context = {
        "problem_list": problem_list,
        "enable_submission": request.user.is_authenticated()
    }
    context.update(csrf(request))
    return render(request, "gameplatform/play.html", context)