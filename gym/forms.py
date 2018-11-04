from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chatroom
        exclude = ['admin']


class ChatPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['chatroom','poster']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
