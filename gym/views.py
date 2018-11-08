from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User # May not be in use
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import login, authenticate, get_user_model
import json
import urllib
from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings
from django.contrib import messages
from .forms import *
from .models import *
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
import requests
from .decorators import check_recaptcha
# from .decorators import check_recaptcha


# Create your views here.


# @login_required(login_url='/accounts/login/')
def chatroom(request,room_id):              # This vew function is to log into a chatroom the user belongs to
    current_user = request.user
    form = ChatPostForm()

    chatroom = get_object_or_404(Chatroom,pk=room_id)
    chatrooms = request.user.chatroom.all()
    chatrooms = Chatroom.objects.all()

    print(chatroom)
    # posts = Post.objects.filter(chatroom=chatroom)
    return render(request, 'chatroom/chatroom.html', locals())


def post(request, id):       
    posts = Post.get_posts().order_by('-posted_on')                # This view function is to make a post in a chatroom,its the formaction
    chatroom = Chatroom.objects.get(id=id)   # to the post form in chatroom
    print(id)
    # new_post = Post()
    if request.method == 'POST':
        newpost = ChatPostForm(request.POST,request.FILES)
        if newpost.is_valid():
            post = newpost.save(commit=False)
            post.poster = request.user
            post.chatroom = chatroom
            print(post.poster)
            post.save()
            return redirect('chatroom',id)
        return redirect('chatroom', id)

def chat(request, id):       
    chats = Post.get_posts().order_by('-posted_on')                # This view function is to make a post in a chatroom,its the formaction
    chatroom = Chatroom.objects.get(id=id)   # to the post form in chatroom
    print(id)
    # new_post = Post()
    if request.method == 'POST':
        newpost = ChatForm(request.POST,request.FILES)
        if newpost.is_valid():
            chat = newpost.save(commit=False)
            post.poster = request.user
            post.chatroom = chatroom
            print(post.poster)
            post.save()
            return redirect('chatroom',id)
        return redirect('chatroom', id)

@login_required(login_url='/accounts/login/')
def chatrooms(request):
    """
    Enables a user to join a chatroom
    """
    if Join.objects.filter(user_id = request.user).exists():
        chatroom = Chatroom.objects.get(pk = request.user.join.chatroom_id)
        return render(request,'chatroom/chatroom.html', locals())

    else:
        chatrooms = Chatroom.objects.all()
        return render(request, 'chatroom/chatrooms.html', locals())

@login_required(login_url='/accounts/login/')
def join_chatroom(request , chatroom_id):
    """
    View function that enables a user join a chat room
    """
    chatroom = Chatroom.objects.get(pk = chatroom_id)
    if JoinChat.objects.filter(user = request.user).exists():
        JoinChat.objects.filter(user_id = request.user).update(chatroom_id = chatroom.id)
    else:
        JoinChat(user=request.user, chatroom_id = chatroom.id).save()

    return redirect('chatroom',chatroom_id)


def exitchatroom(request,id):                  # This is the view function to exit a chatroom
    current_user = request.user
    # current_user.profile.chatroom = None       # It replaces the id for a chatroom with an empty entry in column
    chat = Chatroom.objects.get(id=id)
    current_user.removechatroom(chat, current_user)
    current_user.profile.save()

    return redirect('landing')


# @login_required(login_url='/accounts/login/')
def newchatroom(request):
    current_user = request.user
    if request.method == 'POST':
        NewChatForm = ChatForm(request.POST)
        if NewChatForm.is_valid():
            chatform = NewChatForm.save(commit=False)
            chatform.admin = current_user
            chatform.save()
            print('saved')
        return redirect('chatrooms')


    else:
        NewChatForm = ChatForm()
    return render(request, 'forms/newchat.html', {"newChatForm": NewChatForm})



def joinchat(request, id):
    current_user = request.user
    chat = Chatroom.objects.get(id=id)
    chat.addchatroom(chat, current_user)
    chat.save()

    return redirect('chatroom',id)


# def user(request):
#     return render(request,'user_type.html', locals())

# def homepage(request):
#     return render(request,'home.html', locals())

# def client_login(request):
  
#     return render(request, 'registration/client/login.html')

    
# def manager_login(request):

#     return render(request, 'registration/gym_manager/login.html')

    
# def trainer_login(request):
  
#     return render(request, 'registration/trainer/login.html')


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


# @check_recaptcha
# def client_signup(request):

#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid() and request.recaptcha_is_valid:
#             form.save()
#             messages.success(request, 'Account created successfully!')
#             return redirect('home')
#     else:
#         form = SignupForm()

#     return render(request, 'registration/client/registration_form.html', {'form': form})

# @check_recaptcha
# def manager_signup(request):

#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid() and request.recaptcha_is_valid:
#             form.save()
#             messages.success(request, 'Account created successfully!')
#             return redirect('home')
#     else:
#         form = SignupForm()

#     return render(request, 'registration/gym_manager/registration_form.html', {'form': form})


@check_recaptcha
def trainer_signup(request):

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
        return render(request, 'trainer/home.html')

    else:
        return render(request, 'manager/home.html')

@login_required(login_url='/accounts/login/')
def join(request , gymid):
    """
    This view edits neighbour class
    """
    this_gym = Gym.objects.get(pk = gymid)
    if Join.objects.filter(user = request.user).exists():
        Join.objects.filter(user_id = request.user).update(gym_id = this_gym.id)
    else:
        Join(user=request.user, gym_id = this_gym.id).save()
    messages.success(request, 'Success! You have succesfully joined this Neighbourhood ')
    return redirect('landing')

@login_required(login_url='/accounts/login/')
def myprofile(request, user_id):
    """
    Function that enables one to see their profile details
    """
    title = "Profile"
    profiles = Gymnast.objects.get(user_id=user_id)
    users = User.objects.get(id=user_id)
    return render(request, 'myprofile.html', locals())


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    """
    Function that enables one to edit their profile information
    """
    current_user = request.user
    profile = Gymnast.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance= profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('landing')
    else:
        form = ProfileForm(instance = profile)
    return render(request, 'edit-profile.html', {"form": form,})


@login_required(login_url='/accounts/login/')
def addgym(request):
    """
    Renders the creating hood form
    """
    if request.method == 'POST':
        form = AddgymForm(request.POST,request.FILES)
        if form.is_valid():
            gym = form.save(commit = False)
            gym.manager = request.user
            gym.save()
            return redirect('landing')
    else:
        form = AddgymForm()
        return render(request, 'forms/gym.html', {"form":form})

@login_required(login_url='/accounts/login/')
def exitgym(request, id):
    """
    Allows users to exit gyms
    """
    Join.objects.get(user_id = request.user).delete()
    return redirect('landing')


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user

    # profile = User.objects.get(user=current_user)
    print(profile)
    posts = Post.objects.filter(poster = current_user)
    chatrooms = current_user.chatroom.all()
    print(chatrooms)
    # profile = Profile.objects.filter(user=request.user.id)
    # friend = Friend.objects.get(current_user=current_user)
    # friends = friend.users.all()
    # print(friends)
    return render(request, 'profile.html', {'profile': current_user,'posts':posts,'chatrooms':chatrooms})

