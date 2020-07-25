from django.db import models
from apps.users.models import Vendor


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(
        help_text='Enter quantity of food', null=True)
    created_at = models.DateField(auto_now_add=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    is_recurring = models.BooleanField(default=False)
    RECURRENCE_CHOICES = (
        (0, 'None'),
        (1, 'Daily'),
        (7, 'Weekly'),
        (14, 'Biweekly'),
        (30, 'Monthly')
    )
    frequency = models.IntegerField(choices=RECURRENCE_CHOICES)
