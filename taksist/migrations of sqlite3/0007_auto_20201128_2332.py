# Generated by Django 3.0.8 on 2020-11-29 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taksist', '0006_auto_20201128_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxicategory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='taxistatus',
            name='id',
        ),
        migrations.AddField(
            model_name='taxicategory',
            name='user_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taxistatus',
            name='user_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='car_photo',
            field=models.ImageField(upload_to='car_photos/'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='user_photo',
            field=models.ImageField(upload_to='user_photos/'),
        ),
    ]
