from django import forms
from cookup.forms import MyBaseModelForm
from .models import Pack


class PackCreateForm(MyBaseModelForm):
    class Meta:
        model = Pack
        fields = ["title", "description", "audio_file"]
