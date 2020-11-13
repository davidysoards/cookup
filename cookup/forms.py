from django import forms

# remove the default colon suffix from labels
class MyBaseModelForm(forms.ModelForm):
    required_css_class = "required"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super(MyBaseModelForm, self).__init__(*args, **kwargs)
