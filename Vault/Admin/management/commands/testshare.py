import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from Admin.disk import DiskManager
from FileManager.models import File


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('share_name', type=str)

    def handle(self, *args, **options):
        dm = DiskManager()
        f = File()

        data = "Cool Text Bruh"
        f.size = len(data)
        f.opened = datetime.datetime.now()
        f.edited = datetime.datetime.now()

        u = User.objects.get(username="NielsVM")
        f.owner = u
        dm.upload_new_file(f, data)
