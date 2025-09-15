from django.contrib import admin
from .models import FinanceRecord


@admin.register(FinanceRecord)
class FinanceRecordAdmin(admin.ModelAdmin):
    list_display = ('record_type', 'amount', 'category', 'date', 'owner')
    list_filter = ('record_type', 'category')
