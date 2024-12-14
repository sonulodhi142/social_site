from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='image')
    full_name = models.CharField(max_length=100 ,null=True, blank=True)
    boi = models.CharField(max_length=100 ,null=True, blank=True)
    about = models.CharField(max_length=100 ,null=True, blank=True)
    country = models.CharField(max_length=100 ,null=True, blank=True)
    twitter = models.CharField(max_length=100 ,null=True, blank=True)
    facebook = models.CharField(max_length=100 ,null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
