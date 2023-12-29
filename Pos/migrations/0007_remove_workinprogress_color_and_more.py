# Generated by Django 4.0.4 on 2023-09-02 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0006_cart_delivered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workinprogress',
            name='color',
        ),
        migrations.RemoveField(
            model_name='workinprogress',
            name='fabric',
        ),
        migrations.RemoveField(
            model_name='workinprogress',
            name='product_name',
        ),
        migrations.AddField(
            model_name='workinprogress',
            name='stock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Pos.stockproperty'),
            preserve_default=False,
        ),
    ]