from django.db import models
from django.contrib.auth.models import User


class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey(
        "Profile", on_delete=models.CASCADE, related_name='hood')
    description = models.TextField()
    health_contact = models.IntegerField(null=True, blank=True)
    police_contact = models.IntegerField(null=True, blank=True)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=80, blank=True)
    profile_picture = models.ImageField(
        upload_to='images/', default='default.png')
    neighbourhood = models.ForeignKey(
        NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)


class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(
        NeighbourHood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()


class Post(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='posts/')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)


class Authorities(models.Model):
    name = models.CharField(max_length=40)
    Neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    contacts = models.IntegerField()

    def __str__(self):
        return self.name