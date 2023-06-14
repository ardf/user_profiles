from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='img/profile_pictures/', blank=True,null=True)

