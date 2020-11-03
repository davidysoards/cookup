from django.urls import path
from .views import (
    PackListView,
    PackDetailView,
    PackCreateView,
    PackUpdateView,
    PackDeleteView,
    UserPackListView,
)
from . import views

urlpatterns = [
    path("", PackListView.as_view(), name="home"),
    path(
        "pack/<int:pk>/<slug:slug_url>/", PackDetailView.as_view(), name="pack-detail"
    ),
    path(
        "pack/<int:pk>/<slug:slug_url>/update",
        PackUpdateView.as_view(),
        name="pack-update",
    ),
    path(
        "pack/<int:pk>/<slug:slug_url>/delete",
        PackDeleteView.as_view(),
        name="pack-delete",
    ),
    path("pack/new/", PackCreateView.as_view(), name="pack-create"),
    path("shared-by/<str:username>", UserPackListView.as_view(), name="user-packs"),
    path("about", views.about, name="about"),
]
