# Generated by Django 4.1.3 on 2022-12-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_alter_goodincart_quantity_alter_storeorder_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodincart',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, max_length=90, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='storeorder',
            name='qty',
            field=models.PositiveIntegerField(),
        ),
    ]