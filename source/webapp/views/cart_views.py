from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from webapp.models import GoodInCart, Store
from django.views.generic import View, ListView, DeleteView


# Create your views here.


class CartIndexView(View):

    model = GoodInCart

    def get(self, *args, **kwargs):
        item = get_object_or_404(Store, pk=kwargs.get('pk'))
        if GoodInCart.objects.filter(good_id=item.pk):
            cart = GoodInCart.objects.get(good=item)
            if item.remainder > 0:
                cart.quantity += 1
                cart.save()
                item.remainder -= 1
                item.save()
                return redirect('index')
            elif item.remainder == 0:
                pass
        else:
            cart = GoodInCart.objects.create(good=item)
            cart.quantity = 1
            cart.save()
            item.remainder -= 1
            item.save()
            return redirect('index')


class CartList(ListView):
    template_name = 'cart/list.html'
    context_object_name = 'cart'
    model = GoodInCart


class CartDeleteView(DeleteView):
    template_name = 'cart/delete.html'
    model = GoodInCart
    context_object_name = 'cart'
    success_url = reverse_lazy('cart_list')


