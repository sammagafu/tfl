# Generated by Django 3.2 on 2021-11-01 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyacar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyacar',
            options={'verbose_name': 'Place a car to sell', 'verbose_name_plural': 'Place a cars to sell'},
        ),
        migrations.AlterModelOptions(
            name='carfeatures',
            options={'verbose_name': 'Car Feature', 'verbose_name_plural': 'Car Features'},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={'verbose_name': 'Car Brand', 'verbose_name_plural': 'Car Brands'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Motors Category(bike,car ..)', 'verbose_name_plural': 'Motors Category(bike,car ..)'},
        ),
    ]
