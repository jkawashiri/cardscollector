# Generated by Django 4.2.5 on 2023-09-14 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_related_product_alter_bid_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Related_Product',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='related_products',
            new_name='products',
        ),
    ]
