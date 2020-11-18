from django.contrib import admin
from .models import Sound, Pack, PackAdmin

admin.site.register(Pack, PackAdmin)
admin.site.register(Sound)
