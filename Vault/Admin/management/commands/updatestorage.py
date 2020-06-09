import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from Admin.models import Share, LogMessage

class Command(BaseCommand):
    def handle(self, *args, **options):
        for s in Share.objects.all():
            try:
                s.updateAvailableStorage()
                s.save()
            except FileNotFoundError:
                lm = LogMessage()
                lm.setMessage("Share '{}' could not be found, the path, '{}', might be invalid" ,[s.server_name, s.directory])
                lm.warning_level = LogMessage.LVL_ERR
                lm.save()