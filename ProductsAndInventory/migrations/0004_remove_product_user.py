# Generated by Django 5.0.6 on 2024-05-31 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsAndInventory', '0003_rename_product_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]