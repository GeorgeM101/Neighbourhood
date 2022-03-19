from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'profile')
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=80, blank=True)
    profile_picture = models.ImageField(upload_to = 'images/', default = 'default.png')
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
