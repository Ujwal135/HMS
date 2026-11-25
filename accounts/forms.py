from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class Accountcreationform(UserCreationForm):
    
    email = forms.EmailField()
    
    role = forms.ChoiceField(
        
        choices=[
            ('doctor','Doctor'),
            ('patient','Patient'),
            ] 
        )
    class meta:
        model = User
        fields = ['username','email','role',]

class Userloginform(AuthenticationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'placeholder': 'Enter username'
        }
        )
        )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            'placeholder': 'Enter password'
            }
            )
            )