from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={'required':"Enter your name."},
        max_length=50, label = "name"
    )
    email = forms.EmailField(
        error_messages={'required':"Enter your email."},
        max_length=50, label = "email"
    )
    password = forms.CharField(
        error_messages={'required' : "Enter your password"},
        widget = forms.PasswordInput, label = "password"
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required':'Enter your email'},
        max_length=64, label = "email"
    )
    password = forms.CharField(
        error_messages = {'required' : "Enter your password"},
        max_length = 128, label = "password", widget = forms.PasswordInput
    )
    
