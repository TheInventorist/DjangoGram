""" posts model """

from django.db import models

class User(models.Model):
    """ User model """

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    bio = models.TextField()
    birthdate = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)