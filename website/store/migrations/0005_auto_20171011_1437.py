# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20171011_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='prodNum',
            field=models.ForeignKey(db_column='prodNum', on_delete=django.db.models.deletion.CASCADE, to='store.Products'),
        ),
    ]
