from django import forms
from cookup.forms import MyBaseModelForm
from .models import Sound, Pack


class SoundCreateForm(MyBaseModelForm):
    KEYS = [
        ("", "----"),
        (1, "A"),
        (2, "A#/B♭"),
        (3, "B"),
        (4, "C"),
        (5, "C#/D♭"),
        (6, "D"),
        (7, "D#/E♭"),
        (8, "E"),
        (9, "F"),
        (10, "F#/G♭"),
        (11, "G"),
        (12, "G#/A♭"),
    ]

    SCALES = [
        ("", "----"),
        ("M", "Major"),
        ("m", "minor"),
    ]

    key = forms.ChoiceField(choices=KEYS, required=False)
    scale = forms.ChoiceField(choices=SCALES, required=False)

    class Meta:
        model = Sound
        fields = [
            "name",
            "audio_file",
            "key",
            "scale",
        ]


class PackCreateForm(MyBaseModelForm):
    class Meta:
        model = Pack
        fields = ["title", "description", "audio_file"]
