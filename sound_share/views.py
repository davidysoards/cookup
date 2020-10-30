from django.shortcuts import render
from .models import Pack

# packs = [
#     {
#         "title": "Pack 1",
#         "description": "An awesome pack of sounds.",
#         "date_posted": "October 29, 2020",
#         "author": "davidsoards",
#     },
#     {
#         "title": "Pack 2",
#         "description": "An amazing pack of sounds.",
#         "date_posted": "October 29, 2020",
#         "author": "davidsoards",
#     },
# ]

# Create your views here.
def home(request):
    context = {"packs": Pack.objects.all()}
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")
