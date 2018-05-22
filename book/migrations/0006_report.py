# Generated by Django 2.0.5 on 2018-05-20 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_book_is_available'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0005_auto_20180505_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='search.Book')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]