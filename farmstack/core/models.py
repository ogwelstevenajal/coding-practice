from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        FARMER = 'farmer', 'Farmer'
        AGENT = 'agent', 'Agent'

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.FARMER)
    phone_number = models.CharField(max_length=20, blank=True)
    preferred_language = models.CharField(max_length=5, default='en')

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"


class OfflineSyncRecord(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='offline_sync_records')
    payload = models.JSONField()
    status = models.CharField(max_length=20, default='queued')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"OfflineSyncRecord #{self.pk} by {self.user_id}"

# Create your models here.
