from django.contrib import admin
from .models import Pack, PackAdmin

admin.site.register(Pack, PackAdmin)
