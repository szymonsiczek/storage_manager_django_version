from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(
        default='default_profile_pic.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"
