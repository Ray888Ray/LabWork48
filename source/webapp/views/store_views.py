from django.shortcuts import reverse
from django.urls import reverse_lazy
from webapp.models import Store
from webapp.forms import StoreForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# Create your views here.


# def index_view(request):
#     store = Store.objects.order_by('status', 'name').filter(remainder__gt=0)
#     return render(request, 'index.html', {'store': store})


class IndexView(ListView):
    template_name = 'goods/index.html'
    context_object_name = 'store'
    model = Store

    def get_queryset(self):
        filter = Store.objects.filter(remainder__gt=0)
        return filter


# def info_views(request, pk):
#     store = get_object_or_404(Store, pk=pk)
#     return render(request, 'info.html', {'store':store})


class InfoView(DetailView):
    template_name = 'goods/info.html'
    model = Store

# def add_views(request):
#     if request.method == "GET":
#         form = StoreForm()
#         return render(request, "add.html", {'form': form, 'status': CATEGORY})
#     elif request.method == "POST":
#         form = StoreForm(data=request.POST)
#         if form.is_valid():
#             new_todo = Store.objects.create(
#                 name=form.cleaned_data['name'],
#                 description=form.cleaned_data['description'],
#                 status=form.cleaned_data['status'],
#                 price=form.cleaned_data['price'],
#                 remainder=form.cleaned_data['remainder']
#             )
#             return redirect('info', pk=new_todo.pk)
#         else:
#             return render(request, 'add.html', {'form': form, 'status': CATEGORY})


class AddView(CreateView):

    template_name = 'goods/add.html'
    model = Store
    form_class = StoreForm

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pk})


# def update_view(request, pk):
#     store = get_object_or_404(Store, pk=pk)
#     if request.method == 'GET':
#         form = StoreForm(initial={'name': store.name, 'description': store.description, 'price': store.price, 'remainder':store.remainder})
#         return render(request, 'update.html', {'form': form, 'status': CATEGORY})
#     elif request.method == "POST":
#         form = StoreForm(data=request.POST)
#         if form.is_valid():
#             store.name = form.cleaned_data.get('name')
#             store.description = form.cleaned_data.get('description')
#             store.price = form.cleaned_data.get('price')
#             store.remainder = form.cleaned_data.get('remainder')
#             store.status = form.cleaned_data.get('status')
#             store.save()
#             return redirect('info', pk=store.pk)
#         else:
#             return render(request, 'update.html', {'status': CATEGORY, 'form': form})

class UpdateView(UpdateView):
    model = Store
    template_name = 'update.html'
    form_class = StoreForm
    context_key = 'store'

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pk})


# def delete_view(request, pk):
#     store = get_object_or_404(Store, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'delete.html', {'store': store})
#     elif request.method == 'POST':
#         store.delete()
#         return redirect('index')

class DeleteView(DeleteView):
    template_name = 'delete.html'
    model = Store
    context_object_name = 'store'
    success_url = reverse_lazy('index')
