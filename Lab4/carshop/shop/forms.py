from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'date_birth', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={}))
    email = forms.CharField(widget=forms.EmailInput(attrs={}))
    date_birth = forms.DateField(widget=forms.DateInput(attrs={}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={}))
