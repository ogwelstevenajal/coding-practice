from django.contrib import admin
from .models import PlantingSchedule, CropRotation, PestControlActivity, IrrigationActivity


@admin.register(PlantingSchedule)
class PlantingScheduleAdmin(admin.ModelAdmin):
    list_display = ('crop_name', 'start_date', 'end_date', 'owner', 'notify_via_sms')
    list_filter = ('notify_via_sms',)


@admin.register(CropRotation)
class CropRotationAdmin(admin.ModelAdmin):
    list_display = ('field_name', 'season', 'crop_name', 'owner')


@admin.register(PestControlActivity)
class PestControlActivityAdmin(admin.ModelAdmin):
    list_display = ('crop_name', 'date', 'pesticide', 'owner')


@admin.register(IrrigationActivity)
class IrrigationActivityAdmin(admin.ModelAdmin):
    list_display = ('field_name', 'date', 'duration_minutes', 'method', 'owner')
