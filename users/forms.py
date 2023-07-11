from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import widgets
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    labels = {
            password1:'Password'
    }

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['name', 'username', 'email', 'birthday']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'birthday': forms.DateInput(attrs={'class':'form-control','type': 'date'}),
        }
        labels = {
            'name': 'Name',
            'username': 'Username',
            'email': 'Email',
            'birthday': 'Birthday',
        }



class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}), 
            'password':forms.PasswordInput(attrs={'class': 'form-control'})
        }
        labels = {
            'username': 'Username',
            'password':'Password'
        }

