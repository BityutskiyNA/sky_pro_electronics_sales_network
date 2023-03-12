# Generated by Django 4.1.7 on 2023-03-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterparty',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='counterparty',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='counterparty',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='counterparty',
            name='house_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='house_number'),
        ),
        migrations.AlterField(
            model_name='counterparty',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='street'),
        ),
    ]
