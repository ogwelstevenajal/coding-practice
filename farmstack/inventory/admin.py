from django.contrib import admin
from .models import InventoryItem, InventoryTransaction


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'unit', 'owner', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(InventoryTransaction)
class InventoryTransactionAdmin(admin.ModelAdmin):
    list_display = ('item', 'direction', 'quantity', 'date', 'created_by')
    list_filter = ('direction',)
