# Generated by Django 5.0.6 on 2024-06-05 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsAndInventory', '0004_remove_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]
