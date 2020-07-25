from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Customer, Vendor


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_customer', 'is_vendor', 'is_staff',
                    'is_admin')
    list_filter = ('is_customer', 'is_vendor', 'is_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_customer', 'is_vendor', 'is_admin',
                                    'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class CustomerAdmin(admin.ModelAdmin):
    pass


class VendorAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)
