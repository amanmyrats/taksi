# Generated by Django 2.2 on 2021-03-27 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taksist', '0027_auto_20210327_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etrapobalary',
            name='taxi_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='taksist.TaxiProfile'),
        ),
        migrations.AlterField(
            model_name='saherara',
            name='taxi_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='taksist.TaxiProfile'),
        ),
        migrations.AlterField(
            model_name='saherici',
            name='taxi_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='taksist.TaxiProfile'),
        ),
    ]