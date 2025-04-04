from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nickname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ( 'username', 'email','nickname','phone_number', 'password1', 'password2')