from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File
from pathlib import Path

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile-default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image)
        if img.height > 512 or img.width > 512:
            buffer = BytesIO()
            output_size = (512, 512)
            img.thumbnail(output_size)
            img_filename = Path(self.image.file.name).name
            img_suffix = Path(self.image.file.name).name.split(".")[-1]
            img_format = image_types[img_suffix]
            # First we save the image data into the buffer
            img.save(buffer, format=img_format)
            file_object = File(buffer)
            # Now we actually save the data to S3 through the storage backend
            self.image.save(img_filename, file_object)
