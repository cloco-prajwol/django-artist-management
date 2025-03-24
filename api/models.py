from django.db import models
from django.contrib.auth.models import User

class Gender(models.TextChoices):
    male = 'Male'
    female = 'Female'

class UserType(models.TextChoices):
    admin = 'Admin'
    user = "User"
class Genre(models.TextChoices):
    rmb = "rmb"
    country = "country"
    classics = "classics"
    rock = "rock"
    jazz = "jazz"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10,choices=Gender.choices,null=True)
    address = models.CharField(max_length=100, null=True)
    usertype = models.CharField(max_length=10,choices=UserType.choices, default=UserType.user)
    class Meta:
        db_table = ''

class Artist(models.Model):
    name = models.CharField(max_length=100)
    first_release_year = models.IntegerField(null=False)
    no_of_album_release = models.IntegerField(null=False)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10,choices=Gender.choices,null=True)
    address = models.CharField(max_length=100, null=True)
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'artists'


class Music(models.Model):
    title = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name='music')
    genre = models.CharField(max_length=20,choices=Genre)
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'music'
