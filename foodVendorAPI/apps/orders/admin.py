from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_status', 'customer', 'vendor')
    search_fields = ('id', 'order_status')


admin.site.register(Order, OrderAdmin)
