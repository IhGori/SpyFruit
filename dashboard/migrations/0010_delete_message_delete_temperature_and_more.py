# Generated by Django 4.1.5 on 2023-01-21 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Temperature',
        ),
        migrations.DeleteModel(
            name='TemperatureData',
        ),
    ]
