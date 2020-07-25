from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'vendor')
    search_fields = ('name', 'vendor')


admin.site.register(Menu, MenuAdmin)
