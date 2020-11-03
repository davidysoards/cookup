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

from .models import Pack


class PackListView(ListView):
    model = Pack
    template_name = "home.html"  # default = sound_share/pack_list.html
    ordering = ["-date_posted"]
    paginate_by = 3


class UserPackListView(ListView):
    model = Pack
    template_name = (
        "sound_share/user_packs.html"  # default = sound_share/pack_list.html
    )
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Pack.objects.filter(author=user).order_by("-date_posted")


class PackDetailView(DetailView):
    model = Pack
    slug_url_kwarg = "slug_url"


class PackCreateView(LoginRequiredMixin, CreateView):
    model = Pack
    fields = ["title", "description"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PackUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pack
    fields = ["title", "description"]

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


def about(request):
    return render(request, "about.html")
