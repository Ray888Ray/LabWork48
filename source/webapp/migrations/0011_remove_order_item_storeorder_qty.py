# Generated by Django 4.1.3 on 2022-12-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_storeorder_alter_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='storeorder',
            name='qty',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
