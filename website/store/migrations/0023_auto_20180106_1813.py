# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-06 17:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20171214_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name_plural': 'Dates',
            },
        ),
        migrations.CreateModel(
            name='UserVisits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.IntegerField(default=0)),
                ('is_staff', models.BooleanField()),
                ('visits', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'User Visits',
            },
        ),
        migrations.AddField(
            model_name='dates',
            name='customerID',
            field=models.ForeignKey(db_column='customerID', on_delete=django.db.models.deletion.CASCADE, to='store.UserVisits'),
        ),
    ]