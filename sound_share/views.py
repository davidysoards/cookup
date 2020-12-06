from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Sound, Pack
from .forms import SoundCreateForm, PackCreateForm
from django.urls import reverse
from cookup.custom_tags import get_item


KEYS = {
    "1": "A",
    "2": "A#/B♭",
    "3": "B",
    "4": "C",
    "5": "C#/D♭",
    "6": "D",
    "7": "D#/E♭",
    "8": "E",
    "9": "F",
    "10": "F#/G♭",
    "11": "G",
    "12": "G#/A♭",
}

SCALES = {
    "M": "Major",
    "m": "minor",
}


class SoundListView(ListView):
    model = Sound
    ordering = ["-date_posted"]
    paginate_by = 20


# class UserSoundListView(ListView):
#     model = Sound
#     template_name = (
#         "sound_share/user_sounds.html"  # default = sound_share/sound_list.html
#     )
#     paginate_by = 3

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get("username"))
#         return Sound.objects.filter(author=user).order_by("-date_posted")


class SoundDetailView(DetailView):
    model = Sound


class SoundCreateView(LoginRequiredMixin, CreateView):
    model = Sound
    form_class = SoundCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("sound-detail", kwargs={"pk": self.object.pk})

    def get_form_kwargs(self):
        kwargs = super(SoundCreateView, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    # pass in intial input values using URL params
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial


class SoundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sound
    form_class = SoundCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        sound = self.get_object()
        return self.request.user == sound.author


class SoundDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sound
    success_url = "/"

    def test_func(self):
        sound = self.get_object()
        return self.request.user == sound.author


class PackListView(ListView):
    model = Pack
    ordering = ["-date_posted"]
    paginate_by = 10


class UserPackListView(ListView):
    model = Pack
    template_name = (
        "sound_share/user_packs.html"  # default = sound_share/pack_list.html
    )
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Pack.objects.filter(author=user).order_by("-date_posted")


class PackDetailView(DetailView):
    model = Pack
    slug_url_kwarg = "slug_url"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["keys"] = KEYS
        context["scales"] = SCALES
        return context


class PackCreateView(LoginRequiredMixin, CreateView):
    model = Pack
    form_class = PackCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PackUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pack
    form_class = PackCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PackDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pack
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
