from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Store, CATEGORY
from webapp.forms import StoreForm
# Create your views here.


def index_view(request):
    store = Store.objects.order_by('status', 'name').filter(remainder__gt=0)
    return render(request, 'index.html', {'store': store})


def info_views(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'info.html', {'store':store})


def add_views(request):
    if request.method == "GET":
        form = StoreForm()
        return render(request, "add.html", {'form': form, 'status': CATEGORY})
    elif request.method == "POST":
        form = StoreForm(data=request.POST)
        if form.is_valid():
            new_todo = Store.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                price=form.cleaned_data['price'],
                remainder=form.cleaned_data['remainder']
            )
            return redirect('info', pk=new_todo.pk)
        else:
            return render(request, 'add.html', {'form': form, 'status': CATEGORY})


def update_view(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'GET':
        form = StoreForm(initial={'name': store.name, 'description': store.description, 'price': store.price, 'remainder':store.remainder})
        return render(request, 'update.html', {'form': form, 'status': CATEGORY})
    elif request.method == "POST":
        form = StoreForm(data=request.POST)
        if form.is_valid():
            store.name = form.cleaned_data.get('name')
            store.description = form.cleaned_data.get('description')
            store.price = form.cleaned_data.get('price')
            store.remainder = form.cleaned_data.get('remainder')
            store.status = form.cleaned_data.get('status')
            store.save()
            return redirect('info', pk=store.pk)
        else:
            return render(request, 'update.html', {'status': CATEGORY, 'form': form})


def delete_view(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'store': store})
    elif request.method == 'POST':
        store.delete()
        return redirect('index')