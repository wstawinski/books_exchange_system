from django.db import models
from django.contrib.auth.models import User
from search.models import Book


class ExchangeStatus(models.Model):
    name = models.CharField(max_length=500)


class Exchange(models.Model):
    initiator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_when_initiator', default=1)
    initiators_book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null=True, related_name='%(class)s_when_initiators_book')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_when_receiver', default=1)
    receivers_book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='%(class)s_when_receivers_book', default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(null=True)
    status = models.ForeignKey(ExchangeStatus, on_delete=models.DO_NOTHING)



