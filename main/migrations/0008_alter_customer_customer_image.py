# Generated by Django 4.2 on 2023-04-22 12:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_brand_logo_alter_customer_customer_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='customer_image'),
        ),
    ]
