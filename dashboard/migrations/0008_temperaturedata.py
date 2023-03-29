# Generated by Django 4.1.5 on 2023-01-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
