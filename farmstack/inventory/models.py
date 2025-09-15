from django.db import models
from django.conf import settings


class InventoryItem(models.Model):
    INPUT = 'input'
    OUTPUT = 'output'
    CATEGORY_CHOICES = [
        (INPUT, 'Input'),
        (OUTPUT, 'Output'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    quantity = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    unit = models.CharField(max_length=20, default='kg')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inventory_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.category})"


class InventoryTransaction(models.Model):
    IN = 'in'
    OUT = 'out'
    DIRECTION_CHOICES = [
        (IN, 'In'),
        (OUT, 'Out'),
    ]

    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='transactions')
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='inventory_transactions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.direction} {self.quantity} {self.item.name}"

# Create your models here.
