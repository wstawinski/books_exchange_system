# Generated by Django 2.0.3 on 2018-05-01 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180425_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='initiators_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exchange_when_initiators_book', to='search.Book'),
        ),
    ]
