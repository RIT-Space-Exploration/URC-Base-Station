# Generated by Django 2.2.5 on 2020-01-05 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rover_base_station', '0007_auto_20200105_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='img',
            field=models.TextField(blank=True),
        ),
    ]
