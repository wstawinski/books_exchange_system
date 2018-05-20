from django.db import models
from django.contrib.auth.models import User


class BookType(models.Model):
    pass
    type = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type}, {self.description}'
