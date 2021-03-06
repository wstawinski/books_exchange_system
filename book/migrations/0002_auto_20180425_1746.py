# Generated by Django 2.0.3 on 2018-04-25 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='initiator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exchange_when_initiator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exchange',
            name='initiators_book',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exchange_when_initiators_book', to='search.Book'),
        ),
        migrations.AddField(
            model_name='exchange',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exchange_when_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exchange',
            name='receivers_book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exchange_when_receivers_book', to='search.Book'),
        ),
    ]
