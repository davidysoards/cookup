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


class SoundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sound
    form_class = SoundCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class SoundDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sound
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


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
