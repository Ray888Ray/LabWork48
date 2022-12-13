"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views.store_views import IndexView, InfoView, AddView, UpdateView, DeleteView
from webapp.views.cart_views import CartIndexView, CartList, CartDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('store/<int:pk>/', InfoView.as_view(), name='info'),
    path('store/add/', AddView.as_view(), name='add'),
    path('store/<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('store/<int:pk>/delete/', DeleteView.as_view(), name='delete'),

    path('cart/<int:pk>/list/', CartIndexView.as_view(), name='cart_index'),
    path('cart/list/', CartList.as_view(), name='cart_list'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete'),

]
