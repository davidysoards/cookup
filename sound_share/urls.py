from django.urls import path
from . import views

urlpatterns = [
    # SOUND
    # path("", views.home, name="home"),
    path("", views.PackListView.as_view(), name="home"),
    path("sounds/", views.SoundListView.as_view(), name="sound-list"),
    path(
        "sound/<int:pk>/",
        views.SoundDetailView.as_view(),
        name="sound-detail",
    ),
    path(
        "sound/<int:pk>/update",
        views.SoundUpdateView.as_view(),
        name="sound-update",
    ),
    path(
        "sound/<int:pk>/delete",
        views.SoundDeleteView.as_view(),
        name="sound-delete",
    ),
    path("sound/new/", views.SoundCreateView.as_view(), name="sound-create"),
    # PACK
    # path("packs/", views.PackListView.as_view(), name="pack-list"),
    path(
        "pack/<int:pk>/<slug:slug_url>/",
        views.PackDetailView.as_view(),
        name="pack-detail",
    ),
    path(
        "pack/<int:pk>/<slug:slug_url>/update",
        views.PackUpdateView.as_view(),
        name="pack-update",
    ),
    path(
        "pack/<int:pk>/<slug:slug_url>/delete",
        views.PackDeleteView.as_view(),
        name="pack-delete",
    ),
    path("pack/new/", views.PackCreateView.as_view(), name="pack-create"),
    path(
        "shared-by/<str:username>", views.UserPackListView.as_view(), name="user-packs"
    ),
    path("about", views.about, name="about"),
]
