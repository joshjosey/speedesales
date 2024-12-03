# Generated by Django 5.1.2 on 2024-12-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_category_image_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Placeholder', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='Speed-e-sales Product', max_length=100),
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
    ]