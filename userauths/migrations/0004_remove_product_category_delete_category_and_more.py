# Generated by Django 5.1.2 on 2024-11-04 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
