from django.db import models
from django.conf import settings


class PlantingSchedule(models.Model):
    crop_name = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    field_name = models.CharField(max_length=120, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='planting_schedules')
    notify_via_sms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.crop_name} ({self.start_date})"


class CropRotation(models.Model):
    field_name = models.CharField(max_length=120)
    season = models.CharField(max_length=50)
    crop_name = models.CharField(max_length=120)
    notes = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='crop_rotations')
    created_at = models.DateTimeField(auto_now_add=True)


class PestControlActivity(models.Model):
    crop_name = models.CharField(max_length=120)
    date = models.DateField()
    pesticide = models.CharField(max_length=120)
    notes = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pest_controls')
    created_at = models.DateTimeField(auto_now_add=True)


class IrrigationActivity(models.Model):
    field_name = models.CharField(max_length=120)
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    method = models.CharField(max_length=50, default='drip')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='irrigations')
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
