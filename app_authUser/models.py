from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username