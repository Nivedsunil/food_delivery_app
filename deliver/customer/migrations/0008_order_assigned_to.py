# Generated by Django 5.0.7 on 2024-08-14 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_orderitem'),
        ('deliveryusers', '0002_deliveryuser_restaurant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='deliveryusers.deliveryuser'),
        ),
    ]
