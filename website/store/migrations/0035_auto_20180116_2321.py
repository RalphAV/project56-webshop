# Generated by Django 2.0.1 on 2018-01-16 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_auto_20180116_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='prodNum',
            field=models.ForeignKey(db_column='productNum', on_delete=django.db.models.deletion.CASCADE, to='store.Products'),
        ),
    ]
