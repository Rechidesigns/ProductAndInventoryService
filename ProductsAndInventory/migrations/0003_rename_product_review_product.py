# Generated by Django 5.0.6 on 2024-05-31 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsAndInventory', '0002_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Product',
            new_name='product',
        ),
    ]
