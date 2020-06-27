import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from Admin.cron import UpdateDanglingFiles


class Command(BaseCommand):
    def handle(self, *args, **options):
        UpdateDanglingFiles()
