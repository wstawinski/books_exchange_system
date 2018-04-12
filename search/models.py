from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from user_panel.models import BookType


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booktype = models.ForeignKey(BookType, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=1000)



