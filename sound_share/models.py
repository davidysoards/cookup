from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib import admin
from django.urls import reverse


class Pack(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    audio_file = models.FileField(upload_to="audio_files", max_length=100, default="")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("pack-detail", kwargs={"pk": self.pk, "slug_url": self.slug})


# auto populates the slug based on the title but only works in the Admin area
class PackAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
