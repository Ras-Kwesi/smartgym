from django.shortcuts import render, redirect
from .models import User, Gymnast, Trainer, GymManager, Chatroom, Post, Gym, Event, Join


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

