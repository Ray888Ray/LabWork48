from django import forms
from django.forms import widgets
from webapp.models import Store, GoodInCart
CATEGORY = [('Other', 'Разное'), ('Speakers', 'Колонки'), ('Keyboard', 'Клавиатура'),  ('Monitor', 'Монитор')]


# class StoreForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True, label='Name')
#     description = forms.CharField(max_length=2000, required=False, label='Description', widget=widgets.Textarea)
#     status = forms.ChoiceField(choices=CATEGORY)
#     price = forms.DecimalField(max_digits=9999999, min_value=0, decimal_places=2, required=True, label='Price'
#     , widget=widgets.NumberInput)
#     remainder = forms.IntegerField(min_value=0, required=True, label='Remainder', widget=widgets.NumberInput)

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


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")