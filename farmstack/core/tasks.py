from celery import shared_task
from .sms import send_sms


@shared_task
def send_planting_schedule_sms(phone_number: str, message: str) -> None:
    send_sms(phone_number, message)

