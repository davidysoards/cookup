from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils import timezone
from django.contrib.auth.models import User


class Pack(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.title


# class Pack(models.Model):

#     title = models.CharField(_("title"), max_length=50)

#     class Meta:
#         verbose_name = _("pack")
#         verbose_name_plural = _("packs")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("pack_detail", kwargs={"pk": self.pk})
