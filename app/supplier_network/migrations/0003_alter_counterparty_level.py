# Generated by Django 4.1.7 on 2023-03-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier_network', '0002_alter_counterparty_city_alter_counterparty_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterparty',
            name='level',
            field=models.IntegerField(default=0, verbose_name='Уровень'),
        ),
    ]
