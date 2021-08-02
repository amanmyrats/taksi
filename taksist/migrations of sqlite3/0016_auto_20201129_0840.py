# Generated by Django 3.0.8 on 2020-11-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taksist', '0015_auto_20201129_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxiprofile',
            name='car_photo',
            field=models.ImageField(blank=True, default='car_photo/default_car.png', upload_to='car_photos/'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='user_photo',
            field=models.ImageField(blank=True, default='user_photo/default_taksist.png', upload_to='user_photos/'),
        ),
    ]