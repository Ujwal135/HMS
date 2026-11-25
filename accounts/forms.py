from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
    