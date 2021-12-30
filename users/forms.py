from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, CustomUser
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    phone = forms.CharField(label=_('Phone'), max_length=14,
                            widget=forms.TextInput(attrs={'placeholder': '+250----------'}))
    name = forms.CharField(label=_('Name'), max_length=250,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter name'}))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'required': 'true', 'data-toggle': 'password',
               'placeholder': 'Password'}))
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'required': 'true', 'data-toggle': 'password',
               'placeholder': 'Confirm Password'}))

    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'phone', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))
    # phone = forms.CharField(label='Phone')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

    class Meta:
        model = get_user_model()
        widgets = {
            'password': forms.PasswordInput(
                attrs={'placeholder': '********', 'autocomplete': 'off', 'data-toggle': 'password'}),
        }
        fields = ['email', 'password']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'phone',)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
