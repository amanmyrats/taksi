# Generated by Django 3.2.6 on 2021-09-21 07:09

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('taksist', '0003_auto_20210917_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxiprofile',
            name='test',
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='car_photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='car_photo/default_car.png', force_format='PNG', keep_meta=True, null=True, quality=75, size=[200, 200], upload_to='car_photos/'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taksist.category'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taksist.status'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='user_photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='user_photo/default_taksist.png', force_format='PNG', keep_meta=True, null=True, quality=75, size=[200, 200], upload_to='user_photos/'),
        ),
    ]