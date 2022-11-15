from django.db import models
CATEGORY = [('other', 'Разное'), ('Speakers', 'Колонки'), ('Keyboard', 'Клавиатура'),  ('monitor', 'Монитор')]
# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    status = models.CharField(max_length=15, choices=CATEGORY, default=CATEGORY[0][0], verbose_name='Status')
    remainder = models.PositiveIntegerField( verbose_name='Remainder')
    price = models.IntegerField(verbose_name='Price')




