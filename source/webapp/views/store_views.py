from django.shortcuts import reverse
from django.urls import reverse_lazy
from webapp.models import Store
from webapp.forms import StoreForm, SimpleSearchForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode
# Create your views here.


class IndexView(ListView):
    template_name = 'goods/index.html'
    context_object_name = 'store'
    model = Store

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        if self.form.is_valid():
            self.search_value = self.form.cleaned_data['search']
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
            return queryset
        if not self.search_value:
            filter = Store.objects.exclude(remainder=0).order_by('name')
            return filter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class InfoView(DetailView):
    template_name = 'goods/info.html'
    model = Store


class AddView(CreateView):

    template_name = 'goods/add.html'
    model = Store
    form_class = StoreForm

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pk})


class UpdateView(UpdateView):
    model = Store
    template_name = 'update.html'
    form_class = StoreForm
    context_key = 'store'

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pk})


class DeleteView(DeleteView):
    template_name = 'delete.html'
    model = Store
    context_object_name = 'store'
    success_url = reverse_lazy('index')
