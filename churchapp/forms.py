from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your First Name', 'class': 'text'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your last Name', 'class': 'text'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'text'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email', 'class': 'text'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'text'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'text'}))

    class Meta:
        
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password1', 'password2']

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     phone = forms.CharField(max_length=10)
#     message = forms.CharField(widget=forms.Textarea)