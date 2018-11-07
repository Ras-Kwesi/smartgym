from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Gym,Event

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')
        


        
class AddgymForm(forms.ModelForm):
    """
    Model form class to create a neighbourhood
    """
    class Meta:
        model = Gym
        exclude =['user', 'posted_on', 'manager'] 


class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
    } 