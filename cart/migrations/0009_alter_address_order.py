# Generated by Django 5.1.2 on 2024-12-03 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_address_send_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cartorder'),
        ),
    ]
