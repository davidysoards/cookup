from django import forms
from cookup.forms import MyBaseModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    required_css_class = "required"

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super(UserRegistrationForm, self).__init__(*args, **kwargs)


class UserUpdateForm(MyBaseModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(MyBaseModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
