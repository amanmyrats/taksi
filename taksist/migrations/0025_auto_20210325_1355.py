# Generated by Django 2.2 on 2021-03-25 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taksist', '0024_auto_20210324_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='saherara',
            name='city2',
            field=models.ForeignKey(choices=[(1, 'Sarahs'), (2, 'Mary'), (3, 'Balkanabat'), (4, 'Tejen'), (5, 'Aşgabat'), (6, 'Daşoguz'), (7, 'Çärjew')], default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nira', to='taksist.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='saherara',
            name='city1',
            field=models.ForeignKey(choices=[(1, 'Sarahs'), (2, 'Mary'), (3, 'Balkanabat'), (4, 'Tejen'), (5, 'Aşgabat'), (6, 'Daşoguz'), (7, 'Çärjew')], on_delete=django.db.models.deletion.CASCADE, related_name='nireden', to='taksist.City'),
        ),
    ]
