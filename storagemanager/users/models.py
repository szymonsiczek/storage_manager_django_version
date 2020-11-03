from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username} ({self.email})'


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(
        default='default_profile_pic.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def add_phone_number(self, phone_number):
        self.phone_number = phone_number
        self.save()
