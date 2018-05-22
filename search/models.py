from django.db import models
from django.contrib.auth.models import User
from user_panel.models import BookType


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booktype = models.ForeignKey(BookType, on_delete=models.DO_NOTHING)
    is_available = models.BooleanField(default=True)


class Images(models.Model):
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField()


class Tag(models.Model):
    tag = models.CharField(unique=True, max_length=50)


class BookTag(models.Model):
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
    tagId = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)


