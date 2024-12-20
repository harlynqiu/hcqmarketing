# Generated by Django 5.1.3 on 2024-11-21 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('purchases', '0003_purchase_status_purchaseitem_delivered_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('delivered_quantity', models.PositiveIntegerField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_history', to='inventory.inventory')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.purchase')),
            ],
        ),
    ]
