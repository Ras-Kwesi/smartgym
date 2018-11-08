from django.shortcuts import render, redirect
from .models import User, Gymnast, Trainer, GymManager, Chatroom, Post, Gym, Event, Join,Entry
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
from .forms import SignupForm, AddgymForm,NewEventForm
from .decorators import check_recaptcha

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

            return redirect('landing')
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
    if request.user.user_type == 1:
        if Join.objects.filter(user_id = request.user).exists():
            gym = Gym.objects.get(pk = request.user.join.gym_id)
            return render(request, 'gymnast/home.html', locals())

        else:
            gyms = Gym.objects.all()
            return render(request, 'gymnast/index.html', locals())

    elif request.user.user_type == 2:
        entries = Entry.objects.all()
        print(entries)
        print('notworking')
        return render(request, 'trainer/home.html', locals())

    else:
        events = Event.objects.all()
        return render(request, 'manager/home.html',locals())

@login_required(login_url='/accounts/login/')
def join(request , gymid):
    """
    This view edits neighbour class
    """
    this_gym = Gym.objects.get(pk = gymid)
    if Join.objects.filter(user = request.user).exists():
        Join.objects.filter(user_id = request.user).update(gym_id = this_gym.id)
    else:
        Join(user=request.user, hood_id = this_gym.id).save()
    messages.success(request, 'Success! You have succesfully joined this Neighbourhood ')
    return redirect('landing')


@login_required(login_url='/accounts/login/')
def addgym(request):
    """
    Renders the creating hood form
    """
    if request.method == 'POST':
        form = AddgymForm(request.POST)
        if form.is_valid():
            gym = form.save(commit = False)
            gym.manager = request.user
            gym.save()
            return redirect('landing')
    else:
        form = AddgymForm()
        return render(request, 'forms/gym.html', {"form":form})


@login_required(login_url='/accounts/login/')
def new_event(request):
    if request.method == 'POST':
        form = NewEventForm(request.POST, request.FILES)
        if form.is_valid():
            gym = form.save(commit=False)
            gym.manager = request.user
            gym.save()
        return redirect('home.html')

    else:
        form = NewEventForm()
    return render(request, 'manager/new_event.html', {"form": form})

def gymnast(request, user_id):
    """
    Function that enables one to see their gymnast
    """
    title = "gymnast"
    images = Image.get_image_by_id(id= user_id).order_by('-posted_time')
    gymnasts = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'gymnast.html',{'title':title, "images":images,"gymnasts":gymnasts})

  
def new_gymnast(request):
    current_user = request.user
    gymnast=Gymnast.objects.get(user=request.user)
    image= Gymnast.objects.get(user=request.user)
    if request.method == 'POST':
        form = GymnastForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form = GymnastForm()
    return render(request, "edit_profile.html", {"form":form,"image":image}) 
