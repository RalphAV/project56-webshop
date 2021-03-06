# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20170929_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Customer addresses'},
        ),
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='orderdetails',
            options={'verbose_name_plural': 'Order details'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='productdetails',
            options={'verbose_name_plural': 'Product details'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='productdetails',
            name='pubDatum',
            field=models.CharField(default='1 januari, 1990', max_length=30),
        ),
    ]
