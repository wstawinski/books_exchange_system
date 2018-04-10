from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    location = models.CharField(max_length=50)


@receiver(post_save, sender=Book)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Book.objects.create(book=instance)
    else:
        instance.profile.save()
