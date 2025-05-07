from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nickname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ( 'username', 'email','nickname','phone_number', 'password1', 'password2')

class PasswordResetForm(forms.Form):
    username = forms.CharField(label="아이디", max_length=150)
    email = forms.EmailField(label="이메일", required=True)
    new_password = forms.CharField(label="새 비밀번호", widget=forms.PasswordInput)

class CustomUserUpdateForm(UserChangeForm):
    password = None  # 비밀번호 수정은 제외

class Meta:
    model = CustomUser
    fields = ('username', 'nickname', 'email', 'phone_number')