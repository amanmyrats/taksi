# Generated by Django 3.1.7 on 2021-03-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taksist', '0020_category_city_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='city1',
            field=models.CharField(choices=[('Sarahs', 'Sarahs'), ('Mary', 'Mary'), ('Balkanabat', 'Balkanabat'), ('Tejen', 'Tejen'), ('Aşgabat', 'Aşgabat'), ('Daşoguz', 'Daşoguz'), ('Çärjew', 'Çärjew'), ('Etrap obalary', 'Etrap obalary'), ('Şäher ara', 'Şäher ara'), ('Şäher içi', 'Şäher içi')], max_length=20),
        ),
    ]
