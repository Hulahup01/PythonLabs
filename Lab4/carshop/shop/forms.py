import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'phone', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            if not re.match(r'^\+375 \d{2} \d{7}$', phone):
                raise forms.ValidationError("Phone number must be in the format +375 XX XXXXXXX.")
        return phone

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year - (
                        (today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            if age < 18:
                raise forms.ValidationError("You must be at least 18 years old to register.")
        return date_of_birth

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={}))
    second_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={}))
    email = forms.CharField(widget=forms.EmailInput(attrs={}))
    date_of_birth = forms.DateField(label='Birth date', widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'placeholder': '+375 XX XXXXXXX',
    }))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={}))

