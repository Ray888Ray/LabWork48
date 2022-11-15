from django.contrib import admin
from webapp.models import Store
# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'remainder', 'price']
    list_display_links = ['name']
    list_filter = ['description']
    search_fields = ['name', 'description']
    exclude = []
    readonly_fields = ['price', 'remainder']


admin.site.register(Store, StoreAdmin)
