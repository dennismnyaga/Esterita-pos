# Generated by Django 4.0.4 on 2023-12-10 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0022_alter_stockproperty_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockproperty',
            name='size',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
