from django import forms
from django.forms import widgets
from webapp.models import Store, GoodInCart, Order
CATEGORY = [('Other', 'Разное'), ('Speakers', 'Колонки'), ('Keyboard', 'Клавиатура'),  ('Monitor', 'Монитор')]



class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description', 'status', 'price', 'remainder']
        widgets = {'remainder': widgets.NumberInput, 'price': widgets.NumberInput, 'description': widgets.Textarea}


class GoodInCartForm(forms.ModelForm):

    class Meta:
        model = GoodInCart
        fields = ['good', 'quantity']
        widgets = {'quantity': widgets.NumberInput}


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = []


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")