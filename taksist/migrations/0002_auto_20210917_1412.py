# Generated by Django 3.2.6 on 2021-09-17 09:12

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('taksist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxiprofile',
            name='car_photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='car_photo/default_car.png', force_format='PNG', keep_meta=True, quality=75, size=[200, 200], upload_to='car_photos/'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='category',
            field=models.ForeignKey(blank=True, choices=[(1, 'Şäher Içi'), (2, 'Etrap Obalary'), (3, 'Şäher Ara')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='taksist.category'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='nira',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nira', to='taksist.city'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='nireden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nireden', to='taksist.city'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='status',
            field=models.ForeignKey(blank=True, choices=[(1, 'Dynçda'), (2, 'Işde')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='taksist.status'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='user_photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='user_photo/default_taksist.png', force_format='PNG', keep_meta=True, quality=75, size=[200, 200], upload_to='user_photos/'),
        ),
    ]