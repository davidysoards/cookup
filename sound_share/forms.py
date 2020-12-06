from django import forms
from cookup.forms import MyBaseModelForm
from .models import Sound, Pack


class SoundCreateForm(forms.ModelForm):
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

    required_css_class = "required"

    pack = forms.ModelChoiceField(queryset=None)
    key = forms.ChoiceField(choices=KEYS, required=False)
    scale = forms.ChoiceField(choices=SCALES, required=False)
    tempo = forms.CharField(widget=forms.NumberInput(attrs={"min": 1, "max": 300}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        kwargs.setdefault("label_suffix", "")
        super(SoundCreateForm, self).__init__(*args, **kwargs)
        self.fields["pack"].queryset = Pack.objects.filter(author=self.user)

    class Meta:
        model = Sound
        fields = [
            "audio_file",
            "pack",
            "key",
            "scale",
            "tempo",
        ]


class PackCreateForm(MyBaseModelForm):
    class Meta:
        model = Pack
        fields = ["title", "description", "image"]
