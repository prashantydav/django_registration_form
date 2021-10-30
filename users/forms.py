from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.models import  User

class UserForm(UserCreationForm):

    first_name = forms.CharField(max_length=50 , required = True , widget = forms.TextInput())
    last_name = forms.CharField(max_length=50 , required = True , widget = forms.TextInput())
    username = forms.EmailField(max_length=100 , required = True , widget = forms.TextInput())
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'password','class':'password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'confirm password','class':'password'}))

    class Meta:
        model = User
        fields = ('first_name' , 'last_name' , 'username' , 'password1' , 'password2' ,)

class AuthForm(AuthenticationForm):

    username = forms.EmailField(max_length=100 , required = True , widget = forms.TextInput())
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'password','class':'password'}))

    class Meta:
        model = User
        fields = ('username' , 'password')