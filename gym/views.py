from django.shortcuts import render, redirect
from .models import User, Gymnast, Trainer, GymManager, Chatroom, Post, Gym, Event, Join
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import urllib
import json
import requests
from .forms import SignupForm
from .decorators import check_recaptcha


User = get_user_model()

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
  
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                form.save()
                messages.success(request, 'Account verified successfully!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'registration/registration_form.html', {'form': form})

@check_recaptcha
def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('landing')
    else:
        form = SignupForm()

    return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def index(request):
    """
    Renders the index page
    """
    # if Join.objects.filter(user_id = request.user).exists():
    #     gym = Gym.objects.get(pk = request.user.join.gym_id)
    #     return render(request, 'gymnast/home.html', locals())

    # else:
    gyms = Gym.objects.all()
    return render(request, 'gymnast/index.html', locals())

