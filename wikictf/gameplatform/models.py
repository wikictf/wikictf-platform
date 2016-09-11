from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=200)


class Problem(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.OneToOneField(User)
    text = models.TextField()
    value = models.IntegerField()
    category = models.CharField(max_length=50)

    flag_sha512_hash = models.CharField(max_length=128)
