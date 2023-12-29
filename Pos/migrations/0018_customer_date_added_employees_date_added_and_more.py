# Generated by Django 4.0.4 on 2023-10-19 07:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0017_productpro_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 10, 19, 7, 58, 34, 87577, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 10, 19, 7, 58, 49, 6351, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 10, 19, 7, 58, 56, 700261, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productsize',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 10, 19, 7, 59, 3, 492684, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
