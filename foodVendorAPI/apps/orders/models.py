from django.db import models
from apps.users.models import Vendor, Customer
from apps.menus.models import Menu


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default='')
    description = models.TextField()
    items_ordered = models.ManyToManyField(Menu)
    amount_due = models.FloatField(default=0.00)
    amount_paid = models.FloatField(default=0.00)
    oustanding = models.FloatField(default=0.00)
    ORDER_STATUS_CHOICES = (
        ('created', 'Created'),
        ('preparing', 'Preparing'),
        ('completed', 'Completed')
    )
    order_status = models.CharField(max_length=120,
                                    choices=ORDER_STATUS_CHOICES,
                                    default='created')
    created_at = models.DateTimeField(auto_now_add=True)
