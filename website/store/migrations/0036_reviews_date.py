# Generated by Django 2.0.1 on 2018-01-17 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0035_auto_20180116_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
