from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Create default groups: admin, farmer, agent with baseline permissions.'

    def handle(self, *args, **options):
        for name in ['admin', 'farmer', 'agent']:
            Group.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Groups ensured.'))

