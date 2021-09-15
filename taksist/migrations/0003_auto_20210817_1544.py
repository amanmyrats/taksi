# Generated by Django 3.2.6 on 2021-08-17 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taksist', '0002_alter_taxiprofile_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxiprofile',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('1', '2')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='taksist.category'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='nira',
            field=models.ForeignKey(blank=True, choices=[('ag', 'mr')], null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nira1', to='taksist.city'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='nireden',
            field=models.ForeignKey(blank=True, choices=[('ag', 'mr')], null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nireden1', to='taksist.city'),
        ),
        migrations.AlterField(
            model_name='taxiprofile',
            name='status',
            field=models.ForeignKey(blank=True, choices=[('1', '2')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='taksist.status'),
        ),
    ]
