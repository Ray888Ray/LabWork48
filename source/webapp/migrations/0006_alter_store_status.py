# Generated by Django 4.1.3 on 2022-11-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_store_rot_store_remainder_alter_store_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='status',
            field=models.CharField(choices=[('other', 'Разное'), ('Speakers', 'Колонки'), ('Keyboard', 'Клавиатура'), ('monitor', 'Монитор')], default='other', max_length=15, verbose_name='Status'),
        ),
    ]
