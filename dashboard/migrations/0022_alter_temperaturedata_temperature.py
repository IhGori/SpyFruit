# Generated by Django 4.1.5 on 2023-01-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_alter_temperaturedata_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturedata',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
