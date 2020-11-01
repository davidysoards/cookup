from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# remove the default colon suffix from labels
class BaseModelForm(forms.ModelForm):
    required_css_class = "required"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super(BaseModelForm, self).__init__(*args, **kwargs)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    required_css_class = "required"

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super(UserRegistrationForm, self).__init__(*args, **kwargs)


class UserUpdateForm(BaseModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
