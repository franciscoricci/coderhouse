# Generated by Django 4.1.2 on 2022-11-28 19:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
