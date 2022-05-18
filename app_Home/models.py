from django.db import models
from django.contrib.auth.models import User

from app_authUser.models import UserProfile

# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='news_image/', blank=True, null=True)
    image2 = models.ImageField(upload_to='news_image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='news_image/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='review_image/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='review', null=True, blank=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='service_image/', blank=True, null=True)
    image2 = models.ImageField(upload_to='service_image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='service_image/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='service', null=True, blank=True)

    def __str__(self):
        return self.title

class ModelInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    details = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    bust = models.IntegerField(null=True, blank=True)
    waist = models.IntegerField(null=True, blank=True)
    hips = models.IntegerField(null=True, blank=True)
    hair_color = models.CharField(max_length=100, null=True, blank=True)
    eye_color = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    title_image = models.ImageField(upload_to='model_image/', blank=True, null=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    image2 = models.ImageField(upload_to='model_image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='model_image/', blank=True, null=True)
    image4 = models.ImageField(upload_to='model_image/', blank=True, null=True)
    image5 = models.ImageField(upload_to='model_image/', blank=True, null=True)
    image6 = models.ImageField(upload_to='model_image/', blank=True, null=True)
    image7 = models.ImageField(upload_to='model_image/', blank=True, null=True)
    image8 = models.ImageField(upload_to='model_image/', blank=True, null=True)
    image9 = models.ImageField(upload_to='model_image/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
   
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    