"""
    models.py - Profile Model

    This module contains the Profile model definition.

    Models:
    - Profile: Model representing user profiles.

"""

from django.db import models

class Profile(models.Model):
    """
    Profile Model

    Model representing user profiles.

    Fields:
    - name: The name of the user.
    - email: The email of the user (unique).
    - bio: The bio of the user.
    - profile_picture: The profile picture of the user.

    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='img/profile_pictures/', blank=True,null=True)

