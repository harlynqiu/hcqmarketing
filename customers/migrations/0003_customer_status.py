# Generated by Django 5.1.1 on 2024-11-28 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_dateedit'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20),
        ),
    ]
