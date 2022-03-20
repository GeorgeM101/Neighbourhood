from django.contrib import admin

from hood.models import NeighbourHood, Profile, Post, Business, Authorities

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Authorities)
