from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Pack


def home(request):
    context = {"packs": Pack.objects.all()}
    return render(request, "home.html", context)


class PackListView(ListView):
    model = Pack
    template_name = "home.html"  # default = sound_share/pack_list.html
    context_object_name = "packs"
    ordering = ["-date_posted"]


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
