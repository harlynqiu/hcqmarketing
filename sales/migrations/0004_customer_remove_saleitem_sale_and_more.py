# Generated by Django 5.1.1 on 2024-11-28 04:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_purchase_price'),
        ('sales', '0003_saleitem_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='saleitem',
            name='sale',
        ),
        migrations.RemoveField(
            model_name='saleitem',
            name='product',
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sales_code', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50)),
                ('payment_status', models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid'), ('Partially Paid', 'Partially Paid')], default='Unpaid', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card'), ('Bank Transfer', 'Bank Transfer')], default='Cash', max_length=50)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Completed', max_length=50)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='sales.sales')),
            ],
        ),
        migrations.CreateModel(
            name='SalesItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price_per_item', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.sales')),
            ],
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.DeleteModel(
            name='SaleItem',
        ),
    ]
