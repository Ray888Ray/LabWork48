# Generated by Django 4.1.3 on 2022-12-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_remove_order_item_storeorder_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodincart',
            name='quantity',
            field=models.PositiveIntegerField(default=23, verbose_name='Quantity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storeorder',
            name='qty',
            field=models.PositiveIntegerField(verbose_name='Qty'),
        ),
    ]