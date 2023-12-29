# Generated by Django 4.0.4 on 2023-08-30 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WorkInProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('fabric', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('size', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('complete', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.employees')),
            ],
        ),
        migrations.CreateModel(
            name='StockProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=200)),
                ('num_of_rolls', models.IntegerField()),
                ('size', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_stocked', models.DateField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.material')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.color')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.productsize')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expence_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('date_issued', models.DateTimeField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_of_payment', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField()),
                ('to_be_delivered_to', models.CharField(blank=True, max_length=200, null=True)),
                ('no_to_be_delivered', models.IntegerField(blank=True, null=True)),
                ('fully_payed', models.BooleanField(default=True)),
                ('deposited', models.IntegerField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pos.productpro')),
            ],
        ),
    ]
