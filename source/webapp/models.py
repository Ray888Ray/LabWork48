from django.db import models
CATEGORY = [('other', 'Разное'), ('Speakers', 'Колонки'), ('Keyboard', 'Клавиатура'),  ('monitor', 'Монитор')]
# Create your models here.


class GoodInCart(models.Model):
    good = models.ForeignKey('webapp.Store', related_name='good', on_delete=models.CASCADE, verbose_name='Good')
    quantity = models.PositiveIntegerField( null=True, blank=True, verbose_name='Quantity')

    def total_price(self):
        return self.good.price * self.quantity

    def __str__(self):
        return self.good


class Store(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    status = models.CharField(max_length=15, choices=CATEGORY, default=CATEGORY[0][0], verbose_name='Status')
    remainder = models.PositiveIntegerField( verbose_name='Remainder')
    price = models.IntegerField(verbose_name='Price')

    def __str__(self):
        return self.name


class StoreOrder(models.Model):
    order = models.ForeignKey('webapp.Order', related_name='order', on_delete=models.CASCADE, verbose_name='Order')
    store = models.ForeignKey('webapp.Store', related_name='store', on_delete=models.CASCADE, verbose_name='Store')
    qty = models.PositiveIntegerField()


class Order(models.Model):
    customer_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Name')
    phone_number = models.CharField(max_length=10, null=False, blank=False, verbose_name='Phone')
    address = models.CharField(max_length=100, null=False, blank=False, verbose_name='Address')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.customer_name






