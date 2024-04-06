from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import User
from django import forms


class register(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Optional',widget=forms.TextInput(attrs={
        'class':'form-input',
        'placeholder':'Username'
        }) )
    
    email = forms.EmailField(max_length=30, required=False, help_text='Optional',widget=forms.EmailInput(attrs={
        'class':'form-input',
        'placeholder':'Email'
        }) )
    
    password1 = forms.CharField(max_length=30, required=True, help_text='Optional',widget=forms.PasswordInput(attrs={
        'class':'form-input',
        'placeholder':'Password',
        'id':'password'

        }) )
    password2 = forms.CharField(max_length=30, required=True, help_text='Optional',widget=forms.PasswordInput(attrs={
        'class':'form-input',
        'placeholder':'Confirm Password',
        'id':'re_password'
        }) )
    class Meta:
        model = User
        fields = [
             
             
            'username', 
            'email', 
            'password1', 
            'password2', 
            
            ]
        



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'placeholder':'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-input',
            'placeholder':'Password',
            'id':'password'
            
        })
    )
    class Meta:
        model = User
        fields = ('username','password')