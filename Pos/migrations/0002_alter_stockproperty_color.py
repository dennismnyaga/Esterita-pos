# Generated by Django 4.0.4 on 2023-08-31 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockproperty',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.color'),
        ),
    ]
